import keras
import keras_tuner as kt
import matplotlib.pyplot as plt
import numpy as np
from IA.TrainingDropMonitor import TrainingDropMonitor


class NNBase:
    """
    Neural Network Basic Model methods
    """

    def __init__(self, input_shape, window_length: int):
        self.input_shape = input_shape
        self.window_length = window_length
        self.model: keras.Model
        self.dense_count: int = 0
        self.dropout_count: int = 0
        self.callbacks = []
        self.predictions: np.ndarray

    def construct_model(self, hyper_param: kt.HyperParameters):
        raise NotImplementedError()

    def name(self):
        raise NotImplementedError()

    def signal(self):
        raise NotImplementedError()

    def create_dense_layer(self, hyper_param: kt.HyperParameters, min_value: int, max_value: int, step_value: int, default_value: int):
        dense_layer = keras.layers.Dense(hyper_param.Int(name=f"dense_{self.dense_count}", min_value=min_value, max_value=max_value, step=step_value, default=default_value), activation="relu")
        self.dense_count = self.dense_count + 1
        return dense_layer

    def create_dropout_layer(self, hyper_param: kt.HyperParameters, min_value: float, max_value: float, step_value: float, default_value: float):
        dropout_layer = keras.layers.Dropout(hyper_param.Float(name=f"dropout_{self.dropout_count}", min_value=min_value, max_value=max_value, step=step_value, default=default_value))
        self.dropout_count = self.dropout_count + 1
        return dropout_layer

    def compile(self, hyper_param: kt.HyperParameters):
        optimizer = keras.optimizers.Adam(hyper_param.Float(name="learning_rate", min_value=1e-5, max_value=1e-3, sampling="log", default=1e-3))
        self.model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy"])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        """
        Train the model with the provided training data and labels.
        """
        self.add_callbacks()
        self.history = self.model.fit(
            train_data,
            train_labels,
            epochs=num_epochs,
            batch_size=batch_size,
            validation_data=(val_data, val_labels),
            callbacks=self.callbacks,
            # verbose=0,
        )

    def add_callbacks(self, monitor="val_accuracy", patience=5, min_delta=0.2):
        """
        Add callbacks for training.
        - EarlyStopping: Stops training when the validation accuracy drops by more than `min_delta` (20% by default) after `patience` epochs.

        Parameters:
        - monitor: The metric to monitor, default is 'val_accuracy'.
        - patience: The number of epochs to wait before stopping if no improvement, default is 1.
        - min_delta: The minimum change to qualify as an improvement, here used to define the 20% drop.
        """

        if not hasattr(self, "callbacks") or self.callbacks is None:
            self.callbacks = []

        drop_monitor = TrainingDropMonitor(monitor=monitor, min_delta=min_delta, patience=patience)

        self.callbacks.extend([drop_monitor])

    def summary(self):
        """
        Print the summary of the model.
        """
        self.model.summary()

    def plot_train_val(self):
        """
        Plot training and validation accuracy over epochs.
        """
        plt.title(self.name() + " " + self.signal() + " " + str(self.window_length))
        plt.plot(self.history.history["accuracy"], label="accuracy")
        plt.plot(self.history.history["val_accuracy"], label="val_accuracy")
        plt.xlabel("Epoch")
        plt.xlim(left=0)
        plt.ylabel("Accuracy")
        plt.ylim([0.5, 1])
        plt.legend(loc="lower right")

    def predict_classes(self, X_test):
        """ """
        predictions = self.model.predict(X_test)
        self.predictions = np.array([prediction > 0.5 for prediction in predictions])

    def predict(self, X_test):
        """
        Make predictions on the test data.
        """
        predictions = self.model.predict(X_test)
        self.predictions = predictions

    def print_predictions(self, y_test):
        """
        Print predicted and real labels for the test set.
        """
        for i in range(len(y_test)):
            print("PREDICTION: " + str(self.predictions[i]) + " | " + "REAL: " + str(y_test[i]))

    def save_model(self, filepath: str):
        """
        Save the model to the specified filepath.
        """
        self.model.save(filepath)

    def load_model(self, filepath: str):
        """
        Load the model from the specified filepath.
        """
        self.model = keras.models.load_model(filepath)
