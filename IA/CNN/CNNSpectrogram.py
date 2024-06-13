from IA.BaseNN import BaseNN
import tensorflow as tf

class CNNSpectrogram( BaseNN ):
    """
    CNN Model for Spectrogram data training
    """
    def __init__(self, input_shape):
        super().__init__()
        self.model.add(tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=input_shape))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu'))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2)))
        self.model.add(tf.keras.layers.Conv2D(64, (2, 2), activation='relu'))
        self.model.add(tf.keras.layers.Conv2D(128, (1, 1), activation='relu'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.GlobalMaxPooling2D())
        self.model.add(tf.keras.layers.Dense(128, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(64, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(32, activation='relu'))
        self.model.add(tf.keras.layers.Dropout(0.5))
        self.model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    def name(self):
        """
        Return the name of the model.
        """
        return "CNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        return "spectogram"
