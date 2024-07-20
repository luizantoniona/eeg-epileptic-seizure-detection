import keras
import keras_tuner as kt
from IA.CRNN.CRNNBase import CRNNBase

class CRNNPSD( CRNNBase ):
    """
    CRNN Model for PSD data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self, hyper_param: kt.HyperParameters):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))

        self.model.add(keras.layers.Conv2D(
            hyper_param.Int(name='filters_1', min_value=8, max_value=128, step=8, default=16),
            kernel_size=(3, 3),
            activation='relu')
        )
        self.model.add(keras.layers.MaxPooling2D((2, 2)))

        self.model.add(keras.layers.Conv2D(
            hyper_param.Int(name='filters_2', min_value=8, max_value=128, step=8, default=16),
            kernel_size=(3, 3),
            activation='relu')
        )
        self.model.add(keras.layers.MaxPooling2D((2, 2)))

        self.model.add(keras.layers.Conv2D(
            hyper_param.Int(name='filters_3', min_value=8, max_value=128, step=8, default=16),
            kernel_size=(3, 3),
            activation='relu')
        )
        self.model.add(keras.layers.MaxPooling2D((2, 1)))

        self.model.add(keras.layers.TimeDistributed(keras.layers.Flatten()))
        self.model.add(keras.layers.LSTM(
            hyper_param.Int(name='lstm_units_1', min_value=8, max_value=128, step=8, default=16),
            return_sequences=True)
        )
        self.model.add(keras.layers.LSTM(
            hyper_param.Int(name='lstm_units_2', min_value=8, max_value=64, step=8, default=8))
        )

        super().create_dense(hyper_param=hyper_param)

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "PSD"
