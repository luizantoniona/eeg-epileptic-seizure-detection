from IA.CRNN.CRNNBase import CRNNBase
import tensorflow as tf

class CRNNSpectrogram( CRNNBase ):
    """
    CRNN Model for Spectrogram data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, padding='same'))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.TimeDistributed(tf.keras.layers.Flatten()))
        self.model.add(tf.keras.layers.LSTM(128, return_sequences=True))
        self.model.add(tf.keras.layers.GRU(64))
        self.create_dense()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "spectrogram"
