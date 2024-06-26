from IA.NNBase import NNBase

class ViTBase( NNBase ):
    """
    ViT Base Model
    """
    def __init__(self, input_shape):
        super().__init__(input_shape)

    def construct_model(self):
        """
        Construct the model for the ViT
        """
        raise NotImplementedError()

    def name(self):
        """
        Return the name of the model.
        """
        return "ViT"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()