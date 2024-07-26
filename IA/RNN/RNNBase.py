import keras
import keras_tuner as kt
from IA.NNBase import NNBase

class RNNBase( NNBase ):
    """
    RNN Base Model
    """
    def __init__(self, input_shape, window_length: int):
        super().__init__(input_shape, window_length)

    def construct_model(self):
        """
        Construct the model for the RNN
        """
        raise NotImplementedError()

    def name(self):
        """
        Return the name of the model.
        """
        return "RNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()

    def create_dense(self, hyper_param: kt.HyperParameters):
        self.model.add(keras.layers.Dense(
            hyper_param.Int(name='dense_1', min_value=32, max_value=256, step=32, default=128),
            activation='relu'
        ))
        self.model.add(keras.layers.Dropout(
            hyper_param.Float(name='dropout_1', min_value=0.3, max_value=0.7, step=0.1, default=0.5)
        ))
        self.model.add(keras.layers.Dense(
            hyper_param.Int(name='dense_2', min_value=16, max_value=128, step=16, default=64),
            activation='relu'
        ))
        self.model.add(keras.layers.Dropout(
            hyper_param.Float(name='dropout_2', min_value=0.3, max_value=0.7, step=0.1, default=0.5)
        ))
        self.model.add(keras.layers.Dense(
            hyper_param.Int(name='dense_3', min_value=8, max_value=64, step=8, default=32),
            activation='relu'
        ))
        self.model.add(keras.layers.Dropout(
            hyper_param.Float(name='dropout_3', min_value=0.3, max_value=0.7, step=0.1, default=0.5)
        ))
        self.model.add(keras.layers.Dense(1, activation='sigmoid'))
