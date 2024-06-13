from IA.NNBase import NNBase
import tensorflow as tf

class CNNBase( NNBase ):
    """
    CNN Base Model
    """
    def __init__(self):
        super().__init__()

    def name(self):
        """
        Return the name of the model.
        """
        return "CNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()
    
    def create_dense(self):
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(64, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(32, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
