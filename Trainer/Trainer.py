"""
Module: Trainer
"""
import keras_tuner as kt
import os
import tensorflow as tf
import IA.NeuralNetworkModelFactory as NNModelFactory
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Metric.Metric import Metric

NR_EPOCHS = 100 #TODO: Use Keras Tuner
BATCH_SIZE = 32 #TODO: Use Keras Tuner

def train(X_train, y_train, X_val, y_val, X_test, y_test,
          model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, window_length: int):

    os.environ['TF_GPU_ALLOCATOR'] = 'cuda_malloc_async'
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    def build(hp):
        neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, X_train[0].shape, window_length)
        neural_network_model.construct_model(hp)
        neural_network_model.compile(hp)
        return neural_network_model.model
    
    tuner = kt.BayesianOptimization(build,
                                    objective='val_accuracy',
                                    max_trials=20,
                                    directory='data/Tuner',
                                    project_name=signal_type.name + "/" + str(window_length) + "_" + model_type.name)
    
    tuner.search_space_summary()
    tuner.search(X_train, y_train, epochs=50, batch_size=BATCH_SIZE, validation_data=(X_val, y_val))
    best_hps = tuner.get_best_hyperparameters()[0]

    neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, X_train[0].shape, window_length)
    neural_network_model.construct_model(best_hps)
    neural_network_model.compile(best_hps)
    neural_network_model.summary()
    neural_network_model.fit(X_train, y_train, num_epochs=NR_EPOCHS, batch_size=BATCH_SIZE, val_data=X_val, val_labels=y_val)
    neural_network_model.plot_train_val()
    neural_network_model.predict(X_test)
    #neural_network_model.print_predictions(y_test)

    metric = Metric(y_test, neural_network_model.predictions, neural_network_model.name(), signal_type.name, window_length)
    metric.all_metrics()
    metric.metrics_to_database()
    # metric.plot_roc_auc(y_test, neural_network_model.predictions)

    model_filepath = f'data/Models/{signal_type.name}/{str(window_length)}/{model_type.name}_{str(metric.accuracy)}.keras'
    neural_network_model.save_model(filepath=model_filepath)
