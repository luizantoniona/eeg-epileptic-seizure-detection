from IA.BaseNN import BaseNN
import tensorflow as tf

class TimeRNN( BaseNN ):
    """
    RNN Model for time data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.GRU(256, return_sequences=True, input_shape=input_shape))
        self.model.add(tf.keras.layers.SimpleRNN(128, return_sequences=True))
        self.model.add(tf.keras.layers.LSTM(128))
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(64, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(32, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def name(self):
        """
        Return the name of the model.
        """
        return "time_rnn"
