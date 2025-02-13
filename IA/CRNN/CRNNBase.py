import keras
import keras_tuner as kt
from IA.NNBase import NNBase


class CRNNBase(NNBase):
    """
    CRNN Base Model
    """

    def __init__(self, input_shape, window_length: int):
        super().__init__(input_shape, window_length)
        self.convolution_counter: int = 0
        self.lstm_count: int = 0
        self.gru_count: int = 0

    def name(self):
        """
        Return the name of the model.
        """
        return "CRNN"

    def create_dropout_layer(self, hyper_param: kt.HyperParameters, min_value: float, max_value: float, step_value: float, default_value: float):
        return super().create_dropout_layer(hyper_param, min_value, max_value, step_value, default_value)

    def create_convolution_layer(self, hyper_param: kt.HyperParameters, min_value: int, max_value: int, step_value: int, default_value: int, padding: str = "valid"):
        convolution_layer = keras.layers.Conv2D(hyper_param.Int(name=f"conv_{self.convolution_counter}", min_value=min_value, max_value=max_value, step=step_value, default=default_value), kernel_size=(3, 3), activation="relu", padding=padding)
        self.convolution_counter = self.convolution_counter + 1
        return convolution_layer

    def create_lstm_layer(self, hyper_param: kt.HyperParameters, min_value: int, max_value: int, step_value: int, default_value: int, return_sequences: bool = False):
        lstm_layer = keras.layers.LSTM(
            units=hyper_param.Int(name=f"lstm_{self.lstm_count}", min_value=min_value, max_value=max_value, step=step_value, default=default_value),
            return_sequences=return_sequences,
        )
        self.lstm_count = self.lstm_count + 1
        return lstm_layer

    def create_gru_layer(self, hyper_param: kt.HyperParameters, min_value: int, max_value: int, step_value: int, default_value: int, return_sequences: bool = False):
        gru_layer = keras.layers.GRU(
            units=hyper_param.Int(name=f"gru_{self.gru_count}", min_value=min_value, max_value=max_value, step=step_value, default=default_value),
            return_sequences=return_sequences,
        )
        self.gru_count += 1
        return gru_layer

    def create_dense(self, hyper_param: kt.HyperParameters):
        self.model.add(super().create_dense_layer(hyper_param, min_value=32, max_value=256, step_value=8, default_value=128))
        self.model.add(super().create_dropout_layer(hyper_param, min_value=0.1, max_value=0.8, step_value=0.1, default_value=0.5))

        self.model.add(super().create_dense_layer(hyper_param, min_value=16, max_value=128, step_value=8, default_value=64))
        self.model.add(super().create_dropout_layer(hyper_param, min_value=0.1, max_value=0.8, step_value=0.1, default_value=0.5))

        self.model.add(keras.layers.Dense(1, activation="sigmoid"))
