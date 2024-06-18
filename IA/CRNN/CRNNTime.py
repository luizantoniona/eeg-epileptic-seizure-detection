from IA.CRNN.CRNNBase import CRNNBase
import tensorflow as tf

class CRNNTime( CRNNBase ):
    """
    CRNN Model for time data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling1D(2))
        self.model.add(tf.keras.layers.Conv1D(128, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(2))
        self.model.add(tf.keras.layers.LSTM(128, return_sequences=True))
        self.model.add(tf.keras.layers.GRU(64))
        super().create_dense()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "time"
