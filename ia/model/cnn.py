"""
Module: cnn

This module provides CNN models for each data domain
"""

import tensorflow as tf
class TimeCNN:
    """
    CNN Model for time data training
    """
    def __init__(self, input_shape):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=(input_shape)))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        self.model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size, validation_data=(val_data, val_labels))

class FrequencyCNN:
    """
    CNN Model for frequency data training
    """
    def __init__(self, input_shape):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=(input_shape)))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        self.model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size, validation_data=(val_data, val_labels))

class TimeFrequencyCNN:
    """
    CNN Model for time-frequency data training
    """
    def __init__(self, input_shape):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu', input_shape=(input_shape)))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, train_data, train_labels, num_epochs, batch_size, val_data, val_labels):
        self.model.fit(train_data, train_labels, epochs=num_epochs, batch_size=batch_size, validation_data=(val_data, val_labels))