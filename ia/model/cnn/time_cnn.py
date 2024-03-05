"""
Module: time_cnn

This module provides CNN models for time domain
"""

from ia.model.cnn.base_cnn import BaseCNN
import tensorflow as tf

class TimeCNN( BaseCNN ):
    """
    CNN Model for time data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=(input_shape)))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
