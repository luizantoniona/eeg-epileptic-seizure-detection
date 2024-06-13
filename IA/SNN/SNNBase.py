from IA.NNBase import NNBase

class SNNBase( NNBase ):
    """
    SNN Base Model
    """
    def __init__(self):
        super().__init__()

    def name(self):
        """
        Return the name of the model.
        """
        return "SNN"
    
    def signal(self):
        """
        Return the signal type of the model.
        """
        raise NotImplementedError()
