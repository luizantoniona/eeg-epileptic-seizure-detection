"""
Module: CNNFactory
"""
from IA.BaseNN import BaseNN
from IA.SNN.SNNTime import SNNTime
from IA.SNN.SNNPSD import SNNPSD

def model_by_signal_type(signal_type: str, input_shape) -> BaseNN:
    if signal_type == "time":
        return SNNTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return SNNPSD(input_shape=input_shape)
    
    #TODO: Spectogram SNN
    
    else:
        return BaseNN()