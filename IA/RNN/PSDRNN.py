from IA.BaseNN import BaseNN
import tensorflow as tf

class PSDRNN( BaseNN ):
    """
    RNN Model for time data training
    """
    def __init__(self):
        super().__init__()
        self.model.add(tf.keras.layers.GRU(256, return_sequences=True))
        self.model.add(tf.keras.layers.SimpleRNN(128, return_sequences=True))
        self.model.add(tf.keras.layers.LSTM(128))
        self.model.add(tf.keras.layers.Dense(1))

    def name(self):
        """
        Return the name of the model.
        """
        return "psd_rnn"
