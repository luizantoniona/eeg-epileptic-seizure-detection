import keras
from IA.CNN.CNNBase import CNNBase

class CNNPSD( CNNBase ):
    """
    CNN Model for PSD data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.InputLayer(shape=self.input_shape))

        self.model.add(keras.layers.Conv2D(16, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((3, 3)))
        self.model.add(keras.layers.BatchNormalization())

        self.model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(keras.layers.MaxPooling2D((3, 3)))
        self.model.add(keras.layers.BatchNormalization())
        
        self.model.add(keras.layers.Flatten())
        
        super().create_dense()
    
    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "PSD"
