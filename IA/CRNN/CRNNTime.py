import keras
from IA.CRNN.CRNNBase import CRNNBase

class CRNNTime( CRNNBase ):
    """
    CRNN Model for time data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))

        self.model.add(keras.layers.Conv2D(16, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))

        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 2)))

        self.model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((2, 1)))

        self.model.add(keras.layers.TimeDistributed(keras.layers.Flatten()))
        self.model.add(keras.layers.LSTM(16, return_sequences=True))
        self.model.add(keras.layers.GRU(8))

        super().create_dense()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "time"
