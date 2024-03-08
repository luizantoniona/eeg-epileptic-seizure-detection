"""
Module: time_frequency_cnn

This module provides CNN models for time-frequency domain
"""

from ia.model.cnn.base_cnn import BaseCNN
import tensorflow as tf

class TimeFrequencyCNN( BaseCNN ):
    """
    CNN Model for time-frequency data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv2D(64, (2,2), activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling2D((2,2)))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv2D(128, (2,2), activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling2D((2,2)))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.GlobalMaxPooling2D())
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(256, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def name(self):
        return "time_frequency_cnn"
