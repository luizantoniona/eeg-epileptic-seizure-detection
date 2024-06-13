"""
Module: ConvolutionalNNFactory
"""
from IA.CNN.CNNBase import CNNBase
from IA.CNN.CNNTime import CNNTime
from IA.CNN.CNNPSD import CNNPSD
from IA.CNN.CNNSpectrogram import CNNSpectrogram

def model_by_signal_type(signal_type: str, input_shape) -> CNNBase:
    if signal_type == "time":
        return CNNTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return CNNPSD(input_shape=input_shape)

    elif signal_type == "spectrogram":
        return CNNSpectrogram(input_shape=input_shape)
    
    else:
        return CNNBase()