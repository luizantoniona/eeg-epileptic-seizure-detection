"""
Module: cnn

This module provides CNN models for each data domain
"""

import tensorflow as tf

class BaseCNN:
    """
    CNN Basic Model for common methods
    """
    def __init__(self):
        self.model = tf.keras.models.Sequential()

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        return self.model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size, validation_data=(val_data, val_labels))

    def summary(self):
        self.model.summary()

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

class FrequencyCNN( BaseCNN ):
    """
    CNN Model for frequency data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.GlobalMaxPooling1D())
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

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