"""
Module: time_rnn

This module provides RNN models for time domain
"""

from ia.rnn.base_rnn import BaseRNN
import tensorflow as tf

class TimeRNN( BaseRNN ):
    """
    RNN Model for time data training
    """
    def __init__(self):
        super().__init__()
        self.model.add(tf.keras.layers.GRU(256, return_sequences=True))
        self.model.add(tf.keras.layers.SimpleRNN(128, return_sequences=True))
        self.model.add(tf.keras.layers.LSTM(128))
        self.model.add(tf.keras.layers.Dense(10))

    def name(self):
        return "time_rnn"
