"""
Module: ConvolutionalRecurrentNNFactory
"""
from IA.CRNN.CRNNBase import CRNNBase
from IA.CRNN.CRNNTime import CRNNTime
from IA.CRNN.CRNNPSD import CRNNPSD
from IA.CRNN.CRNNSpectogram import CRNNSpectrogram

def model_by_signal_type(signal_type: str, input_shape) -> CRNNBase:
    if signal_type == "time":
        return CRNNTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return CRNNPSD(input_shape=input_shape)
    
    elif signal_type == "spectrogram":
        return CRNNSpectrogram(input_shape=input_shape)
    
    else:
        return CRNNBase()