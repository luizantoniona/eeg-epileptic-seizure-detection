import keras
import keras_tuner as kt
from IA.CRNN.CRNNBase import CRNNBase

class CRNNSpectrogram( CRNNBase ):
    """
    CRNN Model for Spectrogram data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self,  hyper_param: kt.HyperParameters):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))

        self.model.add(keras.layers.Conv2D(16, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((3, 3)))

        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))

        self.model.add(keras.layers.TimeDistributed(keras.layers.Flatten()))
        self.model.add(keras.layers.LSTM(16, return_sequences=True))
        self.model.add(keras.layers.GRU(8))
        
        super().create_dense(hyper_param=hyper_param)

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "spectrogram"
