"""
Module: Trainer
"""
import keras_tuner as kt
import os
import IA.NeuralNetworkModelFactory as NNModelFactory
from Metric.Metric import Metric

NR_EPOCHS = 100 #TODO: Use Keras Tuner
BATCH_SIZE = 256 #TODO: Use Keras Tuner

def train(X_train, y_train, X_val, y_val, X_test, y_test,
          model_type: str, signal_type: str, window_length: int,
          learning_rate: float = 0.001):

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    def build(hp):
        neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, X_train[0].shape, window_length)
        neural_network_model.construct_model(hp)
        neural_network_model.compile(learning_rate=learning_rate)
        return neural_network_model.model
    
    tuner = kt.BayesianOptimization(build,
                                    objective='val_accuracy',
                                    max_trials=20,
                                    directory='Tuner',
                                    project_name=model_type + "_" + signal_type + "_" + str(window_length))
    
    tuner.search_space_summary()
    tuner.search(X_train, y_train, epochs=50, validation_data=(X_val, y_val))
    best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

    neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, X_train[0].shape, window_length)
    neural_network_model.construct_model(best_hps)

    print(neural_network_model.name())
    print(neural_network_model.signal())

    neural_network_model.summary()
    neural_network_model.compile()
    neural_network_model.fit(X_train, y_train, num_epochs=NR_EPOCHS, batch_size=BATCH_SIZE, val_data=X_val, val_labels=y_val)
    neural_network_model.plot_train_val()
    neural_network_model.predict(X_test)
    #neural_network_model.print_predictions(y_test)

    metric = Metric(y_test, neural_network_model.predictions, neural_network_model.name(), signal_type, window_length)
    metric.all_metrics()
    metric.metrics_to_database()
    # metric.plot_roc_auc(y_test, neural_network_model.predictions)
