"""
Module: CNNFactory
"""
from IA.BaseNN import BaseNN
from IA.CRNN.CRNNTime import CRNNTime
from IA.CRNN.CRNNPSD import CRNNPSD

def model_by_signal_type(signal_type: str, input_shape) -> BaseNN:
    if signal_type == "time":
        return CRNNTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return CRNNPSD(input_shape=input_shape)
    
    #TODO: Spectogram CRNN
    
    else:
        return BaseNN()