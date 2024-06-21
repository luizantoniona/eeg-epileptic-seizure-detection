"""
Module: Trainer
"""
import IA.NeuralNetworkModelFactory as NNModelFactory
from Metric.Metric import Metric

NR_EPOCHS = 100 #TODO: Use Keras Turner
BATCH_SIZE = 256 #TODO: Use Keras Turner

def train(X_train, y_train, X_val, y_val, X_test, y_test, model_type: str, signal_type: str):

    neural_network_model = NNModelFactory.model_by_type(model_type, signal_type, X_train[0].shape)

    print(neural_network_model.name())
    print(signal_type)

    neural_network_model.compile()

    neural_network_model.fit(X_train, y_train, num_epochs=NR_EPOCHS, batch_size=BATCH_SIZE, val_data=X_val, val_labels=y_val)

    #neural_network_model.plot_train_val()

    neural_network_model.predict(X_test)
    #neural_network_model.print_predictions(y_test)

    metric = Metric(y_test, neural_network_model.predictions, neural_network_model.name(), signal_type)
    metric.all_metrics()
    # metric.metrics_to_database()

    metric.plot_roc_auc(y_test, neural_network_model.predictions)
