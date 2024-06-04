from IA.BaseNN import BaseNN
import tensorflow as tf

class PSDRCNN(BaseNN):
    """
    RCNN Model for PSD data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv1D(64, 3, activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling1D(2))
        self.model.add(tf.keras.layers.Conv1D(128, 3, activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling1D(2))
        self.model.add(tf.keras.layers.LSTM(128, return_sequences=True))
        self.model.add(tf.keras.layers.GRU(64))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def name(self):
        """
        Return the name of the model.
        """
        return "psd_rcnn"