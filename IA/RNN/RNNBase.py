from IA.NNBase import NNBase
import tensorflow as tf

class RNNBase( NNBase ):
    """
    RNN Base Model
    """
    def __init__(self):
        super().__init__()

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
    
    def compile(self):
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

    def create_dense(self):
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(64, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(32, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
