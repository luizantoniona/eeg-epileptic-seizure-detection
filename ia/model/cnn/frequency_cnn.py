"""
Module: frequency_cnn

This module provides CNN models for frequency domain
"""

from ia.model.cnn.base_cnn import BaseCNN
import tensorflow as tf

class FrequencyCNN( BaseCNN ):
    """
    CNN Model for frequency data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.GlobalMaxPooling1D())
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def name(self):
        return "frequency_cnn"
