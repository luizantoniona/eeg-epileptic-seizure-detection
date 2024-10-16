"""
Module: Trainer
"""

import keras_tuner as kt
import IA.NeuralNetworkModelFactory as NNModelFactory
from Dataset.DatasetTypeEnum import DatasetTypeEnum
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Metric.Metric import Metric

NR_EPOCHS = 100
BATCH_SIZE = 32
#TODO K-FOLD
#TODO CORRIGIR ERROS DEVIDO A TROCA DE data e labels

class Trainer:
    @staticmethod
    def train(dataset_type: DatasetTypeEnum, model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum,
            window_length: int, data, labels):


        def build(hp):
            neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, data[0].shape, window_length)
            neural_network_model.construct_model(hp)
            neural_network_model.compile(hp)
            return neural_network_model.model
        
        tuner = kt.BayesianOptimization(build,
                                        objective='val_accuracy',
                                        max_trials=20,
                                        directory='data/Tuner',
                                        project_name=signal_type.name + "/" + str(window_length) + "_" + model_type.name)
        
        tuner.search_space_summary()
        tuner.search(data, labels, epochs=50, batch_size=BATCH_SIZE, validation_data=(X_val, y_val))
        best_hps = tuner.get_best_hyperparameters()[0]

        neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, data[0].shape, window_length)
        neural_network_model.construct_model(best_hps)
        neural_network_model.compile(best_hps)
        neural_network_model.summary()
        neural_network_model.fit(X_train, y_train, num_epochs=NR_EPOCHS, batch_size=BATCH_SIZE, val_data=X_val, val_labels=y_val)
        neural_network_model.plot_train_val()
        neural_network_model.predict(X_test)
        #neural_network_model.print_predictions(y_test)

        metric = Metric(y_test, neural_network_model.predictions,
                        dataset_name=dataset_type.name, model_name=neural_network_model.name(),
                        model_data_domain=signal_type.name, model_window_length=window_length)
        metric.all_metrics()
        metric.metrics_to_database()
        # metric.plot_roc_auc(y_test, neural_network_model.predictions)

        model_filepath = f'data/Models/{signal_type.name}/{str(window_length)}/{model_type.name}_{str(metric.accuracy)}.keras'
        neural_network_model.save_model(filepath=model_filepath)
