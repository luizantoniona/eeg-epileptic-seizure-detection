import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

class BaseNN:
    """
    Neural Network Basic Model methods
    """
    def __init__(self):
        self.model = tf.keras.models.Sequential()

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        """
        Train the model with the provided training data and labels.
        """
        self.history = self.model.fit(train_data, train_labels,
                                      epochs=num_epochs,
                                      batch_size=batch_size,
                                      validation_data=(val_data, val_labels))

    def summary(self):
        """
        Print the summary of the model.
        """
        self.model.summary()

    def plot_train_val(self):
        """
        Plot training and validation accuracy over epochs.
        """
        plt.plot(self.history.history['accuracy'], label='accuracy')
        plt.plot(self.history.history['val_accuracy'], label = 'val_accuracy')
        plt.xlabel('Epoch')
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
        self.model = tf.keras.models.load_model(filepath)
