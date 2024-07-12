import keras
from IA.NNBase import NNBase

class CRNNBase( NNBase ):
    """
    CRNN Base Model
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        """
        Construct the model for the CRNN
        """
        raise NotImplementedError()

    def name(self):
        """
        Return the name of the model.
        """
        return "CRNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()

    def create_dense(self):
        self.model.add(keras.layers.Dense(128, activation='relu'))
        self.model.add(keras.layers.Dropout(0.5))
        self.model.add(keras.layers.Dense(64, activation='relu'))
        self.model.add(keras.layers.Dropout(0.5))
        self.model.add(keras.layers.Dense(32, activation='relu'))
        self.model.add(keras.layers.Dropout(0.5))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))
