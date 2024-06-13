from IA.NNBase import NNBase

class CRNNBase( NNBase ):
    """
    CRNN Base Model
    """
    def __init__(self):
        super().__init__()

    def name(self):
        """
        Return the name of the model.
        """
        return "CRNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()
