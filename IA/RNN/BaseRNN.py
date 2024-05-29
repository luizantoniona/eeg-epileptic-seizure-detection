"""
Module: base_rnn

This module provides base class model for RNN's
"""

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

class BaseRNN:
    """
    RNN Basic Model methods
    """
    def __init__(self):
        self.model = tf.keras.models.Sequential()

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        self.history = self.model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size, validation_data=(val_data, val_labels))

    def summary(self):
        self.model.summary()

    def plot_train_val(self):
        plt.plot(self.history.history['accuracy'], label='accuracy')
        plt.plot(self.history.history['val_accuracy'], label = 'val_accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.ylim([0.5, 1])
        plt.legend(loc='lower right')

    def predict(self, X_test):
        predictions = self.model.predict(X_test)
        self.predictions = np.array([prediction > 0.5 for prediction in predictions])

    def print_predictions(self, y_test):
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
