from IA.BaseNN import BaseNN
import tensorflow as tf

class ViTPSD(BaseNN):
    """
    Vision Transformer Model for PSD data training
    """
    def __init__(self, input_shape, num_classes, num_layers=8, d_model=64, num_heads=8, mlp_dim=128, dropout_rate=0.1):
        """
        Initialize the Vision Transformer with a specific architecture for PSD data.
        """
        super().__init__()
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.num_layers = num_layers
        self.d_model = d_model
        self.num_heads = num_heads
        self.mlp_dim = mlp_dim
        self.dropout_rate = dropout_rate

        self.build_model()

    def build_model(self):
        """
        Build the Vision Transformer model.
        """
        inputs = tf.keras.layers.Input(shape=self.input_shape)
        
        # Embed the input time-series data
        embedded_inputs = self.time_series_embedding(inputs)

        # Create transformer blocks
        for _ in range(self.num_layers):
            embedded_inputs = self.transformer_block(embedded_inputs)

        # Classification or regression head
        representation = tf.keras.layers.LayerNormalization(epsilon=1e-6)(embedded_inputs)
        representation = tf.keras.layers.Flatten()(representation)
        representation = tf.keras.layers.Dropout(self.dropout_rate)(representation)
        logits = tf.keras.layers.Dense(self.num_classes, activation='softmax')(representation)

        self.model = tf.keras.models.Model(inputs=inputs, outputs=logits)

    def time_series_embedding(self, inputs):
        """
        Embed the input time-series data with a dense layer.
        """
        embedded_inputs = tf.keras.layers.Dense(self.d_model)(inputs)
        # Adding positional encoding
        position_indices = tf.range(start=0, limit=inputs.shape[1], delta=1)
        position_embeddings = tf.keras.layers.Embedding(input_dim=inputs.shape[1], output_dim=self.d_model)(position_indices)
        embedded_inputs += position_embeddings
        return embedded_inputs

    def transformer_block(self, x):
        """
        Create a transformer block.
        """
        # Layer normalization 1
        norm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(x)
        # Multi-head self-attention
        attention_output = tf.keras.layers.MultiHeadAttention(num_heads=self.num_heads, key_dim=self.d_model)(norm1, norm1)
        # Skip connection 1
        x = tf.keras.layers.Add()([x, attention_output])
        
        # Layer normalization 2
        norm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)(x)
        # MLP
        mlp_output = self.mlp(norm2)
        # Skip connection 2
        x = tf.keras.layers.Add()([x, mlp_output])
        return x

    def mlp(self, x):
        """
        MLP block for the transformer.
        """
        x = tf.keras.layers.Dense(self.mlp_dim, activation=tf.nn.gelu)(x)
        x = tf.keras.layers.Dropout(self.dropout_rate)(x)
        x = tf.keras.layers.Dense(self.d_model)(x)
        x = tf.keras.layers.Dropout(self.dropout_rate)(x)
        return x

    def name(self):
        """
        Return the name of the model.
        """
        return "psd_vit"