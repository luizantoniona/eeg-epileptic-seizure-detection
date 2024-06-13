"""
Module: CNNFactory
"""
from IA.BaseNN import BaseNN
from IA.CNN.CNNTime import CNNTime
from IA.CNN.CNNPSD import CNNPSD
from IA.CNN.CNNSpectogram import CNNSpectogram

def model_by_signal_type(signal_type: str, input_shape) -> BaseNN:
    if signal_type == "time":
        return CNNTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return CNNPSD(input_shape=input_shape)

    elif signal_type == "spectogram":
        return CNNSpectogram(input_shape=input_shape)
    
    else:
        return BaseNN()