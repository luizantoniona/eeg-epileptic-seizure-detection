import keras
import keras_tuner as kt
import matplotlib.pyplot as plt
import numpy as np

class NNBase:
    """
    Neural Network Basic Model methods
    """
    def __init__(self, input_shape, window_length: int):
        self.input_shape = input_shape
        self.window_length = window_length
        self.model: keras.Model = None
        self.dense_count: int = 0
        self.dropout_count: int = 0

    def create_dense_layer(self, hyper_param: kt.HyperParameters,
                           min_value: int, max_value: int, step_value: int, default_value: int):
        dense_layer = keras.layers.Dense(
            hyper_param.Int(name=f"dense_{self.dense_count}",
                            min_value=min_value, max_value=max_value,
                            step=step_value, default=default_value),
            activation='relu'
        )
        self.dense_count = self.dense_count + 1
        return dense_layer

    def create_dropout_layer(self, hyper_param: kt.HyperParameters,
                             min_value: int, max_value: int, step_value: int, default_value: int):
        dropout_layer = keras.layers.Dropout(
            hyper_param.Float(name=f"dropout_{self.dense_count}",
                              min_value=min_value, max_value=max_value,
                              step=step_value, default=default_value)
        )
        self.dropout_count = self.dropout_count + 1
        return dropout_layer

    def compile(self, hyper_param: kt.HyperParameters):
        optimizer = keras.optimizers.Adam(
            hyper_param.Float("learning_rate", min_value=1e-5, max_value=1e-3, sampling="log", default=1e-3)
        )
        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        """
        Train the model with the provided training data and labels.
        """
        self.history = self.model.fit(train_data, train_labels,
                                      epochs=num_epochs,
                                      batch_size=batch_size,
                                      validation_data=(val_data, val_labels),
                                      #verbose=0,
                                      )

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
        plt.plot(self.history.history['accuracy'], label='accuracy')
        plt.plot(self.history.history['val_accuracy'], label = 'val_accuracy')
        plt.xlabel('Epoch')
        plt.xlim(left=0)
        plt.ylabel('Accuracy')
        plt.ylim([0.5, 1])
        plt.legend(loc='lower right')

    def predict(self, X_test):
        """
        Make predictions on the test data.
        """
        predictions = self.model.predict(X_test)
        self.predictions = np.array([prediction > 0.5 for prediction in predictions])

    def print_predictions(self, y_test):
        """
        Print predicted and real labels for the test set.
        """
        for i in range(len(y_test)):
            print("PREDICTION: " + str(self.predictions[i]) + " | " +  "REAL: " + str(y_test[i]))

    def save_model(self, filepath):
        """
        Save the model to the specified filepath.
        """
        self.model.save(filepath)

    def load_model(self, filepath):
        """
        Load the model from the specified filepath.
        """
        self.model = keras.models.load_model(filepath)
