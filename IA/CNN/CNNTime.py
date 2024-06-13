from IA.CNN.CNNBase import CNNBase
import tensorflow as tf

class CNNTime( CNNBase ):
    """
    CNN Model for time data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv1D(16, 3, activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv1D(32, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(3))
        self.model.add(tf.keras.layers.Conv1D(64, 1, activation='relu'))
        self.model.add(tf.keras.layers.Conv1D(128, 1, activation='relu'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.GlobalMaxPooling1D())
        self.model.add(tf.keras.layers.Flatten())
        super().create_dense()

    def name(self):
        return super().name()
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        return "time"
