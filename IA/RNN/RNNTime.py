import keras
import keras_tuner as kt
from IA.RNN.RNNBase import RNNBase

class RNNTime( RNNBase ):
    """
    RNN Model for time data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self, hyper_param: kt.HyperParameters):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))
        
        self.model.add(keras.layers.LSTM(
            hyper_param.Int(name='lstm_units_1', min_value=8, max_value=128, step=8, default=32),
            return_sequences=True)
        )
        self.model.add(keras.layers.LSTM(
            hyper_param.Int(name='lstm_units_2', min_value=8, max_value=128, step=8, default=16))
        )
        self.model.add(keras.layers.Flatten())

        super().create_dense(hyper_param=hyper_param)

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "time"
