import keras
import keras_tuner as kt
from IA.RNN.RNNBase import RNNBase

class RNNSpectrogram( RNNBase ):
    """
    RNN Model for Spectrogram data training
    """
    def __init__(self, input_shape, window_length: int):
        super().__init__(input_shape, window_length)

    def construct_model(self, hyper_param: kt.HyperParameters):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))
        
        self.model.add(keras.layers.TimeDistributed(keras.layers.Flatten()))

        self.model.add(super().create_lstm_layer(hyper_param, min_value=8, max_value=64, step_value=8, default_value=32, return_sequences=True))
        self.model.add(super().create_dropout_layer(hyper_param, min_value=0.1, max_value=0.8, step_value=0.1, default_value=0.5))

        self.model.add(super().create_lstm_layer(hyper_param, min_value=8, max_value=32, step_value=8, default_value=16))
        self.model.add(super().create_dropout_layer(hyper_param, min_value=0.1, max_value=0.8, step_value=0.1, default_value=0.5))

        self.model.add(keras.layers.Flatten())
        super().create_dense(hyper_param=hyper_param)

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "Spectrogram"
