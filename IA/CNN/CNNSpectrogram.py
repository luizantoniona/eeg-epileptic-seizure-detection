from IA.CNN.CNNBase import CNNBase
import tensorflow as tf

class CNNSpectrogram( CNNBase ):
    """
    CNN Model for Spectrogram data training
    """

    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape, padding='same'))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
        self.model.add(tf.keras.layers.MaxPooling2D((2, 2), padding='same'))
        self.model.add(tf.keras.layers.BatchNormalization())
        self.model.add(tf.keras.layers.GlobalMaxPooling2D())
        super().create_dense()

    def name(self):
        return super().name()
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        return "spectrogram"
