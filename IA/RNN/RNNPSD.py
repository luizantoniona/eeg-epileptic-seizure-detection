from IA.RNN.RNNBase import RNNBase
import tensorflow as tf

class RNNPSD( RNNBase ):
    """
    RNN Model for PSD data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.LSTM(128, return_sequences=True, input_shape=self.input_shape))
        self.model.add(tf.keras.layers.GRU(64))
        super().create_dense()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "PSD"
