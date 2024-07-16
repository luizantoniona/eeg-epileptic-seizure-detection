from IA.ViT.ViTBase import ViTBase
import tensorflow as tf

class ViTTime( ViTBase ):
    """
    Vision Transformer Model for time-series data training
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        #TODO: Contruct ViT Model
        return super().construct_model()

    def name(self):
        return super().name()

    def signal(self):
        """
        Return the signal type of the model.
        """
        return "time"
