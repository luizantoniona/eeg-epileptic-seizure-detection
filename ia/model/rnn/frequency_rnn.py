"""
Module: frequency_rnn

This module provides RNN models for frequency domain
"""

import tensorflow as tf

class FrequencyRNN:
    """
    RNN Model for time data training
    """
    def __init__(self):

        self.model = tf.keras.Sequential()
        self.model.add(tf.keras.layers.Embedding(input_dim=1000, output_dim=64))
        self.model.add(tf.keras.layers.GRU(256, return_sequences=True))
        self.model.add(tf.keras.layers.SimpleRNN(128))
        self.model.add(tf.keras.layers.LSTM(128))
        self.model.add(tf.keras.layers.Dense(10))