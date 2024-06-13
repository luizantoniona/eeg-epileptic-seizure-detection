from IA.NNBase import NNBase

class RNNBase( NNBase ):
    """
    RNN Base Model
    """
    def __init__(self):
        super().__init__()

    def name(self):
        """
        Return the name of the model.
        """
        return "RNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()
