from IA.RNN.RNNBase import RNNBase
import tensorflow as tf

class RNNSpectrogram( RNNBase ):
    """
    RNN Model for Spectrogram data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.LSTM(128, return_sequences=True, input_shape=input_shape))
        self.model.add(tf.keras.layers.GRU(64))
        super().create_dense()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "spectrogram"
