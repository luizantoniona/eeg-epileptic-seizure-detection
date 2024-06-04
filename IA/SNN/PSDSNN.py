from IA.BaseNN import BaseNN
import tensorflow as tf

class PSDSNN(BaseNN):
    """
    Siamese Network for PSD data
    """
    def __init__(self, input_shape, embedding_dim=128):
        super().__init__()
        self.input_shape = input_shape
        self.embedding_dim = embedding_dim

        self.build_model()

    def build_model(self):
        """
        Build the Siamese Network model.
        """
        # Define the shared LSTM network
        input = tf.keras.layers.Input(shape=self.input_shape)
        x = tf.keras.layers.LSTM(64)(input)
        x = tf.keras.layers.Dense(self.embedding_dim, activation='relu')(x)
        shared_network = tf.keras.models.Model(inputs=input, outputs=x)

        # Create the inputs for the Siamese network
        input_a = tf.keras.layers.Input(shape=self.input_shape)
        input_b = tf.keras.layers.Input(shape=self.input_shape)

        # Generate the encodings (feature vectors) for the two inputs
        encoding_a = shared_network(input_a)
        encoding_b = shared_network(input_b)

        # Compute the distance between the encodings
        distance = tf.keras.layers.Lambda(lambda tensors: tf.abs(tensors[0] - tensors[1]))([encoding_a, encoding_b])
        output = tf.keras.layers.Dense(1, activation='sigmoid')(distance)

        # Create the Siamese network
        self.model = tf.keras.models.Model(inputs=[input_a, input_b], outputs=output)

    def name(self):
        """
        Return the name of the model.
        """
        return "psd_snn"