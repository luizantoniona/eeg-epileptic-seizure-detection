"""
Module: base_rnn

This module provides base class model for RNN's
"""

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
        return self.model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size, validation_data=(val_data, val_labels))

    def summary(self):
        self.model.summary()