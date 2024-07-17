import keras
from IA.RNN.RNNBase import RNNBase

class RNNPSD( RNNBase ):
    """
    RNN Model for PSD data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))

        self.model.add(keras.layers.LSTM(16, return_sequences=True))
        self.model.add(keras.layers.LSTM(8))
        self.model.add(keras.layers.Flatten())
        
        super().create_dense()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "PSD"
