"""
Module: rnn

This module provides RNN models for each data domain
"""

import tensorflow as tf

class TimeRNN:
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

class TimeFrequencyRNN:
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

#SimpleRNN: a fully-connected RNN where the output from previous timestep is to be fed to next timestep
#GRU: As GRUs são uma versão melhorada da rede neural recorrente padrão.
#LSTM: processar e prever séries temporais com intervalos de tempo de duração desconhecida.