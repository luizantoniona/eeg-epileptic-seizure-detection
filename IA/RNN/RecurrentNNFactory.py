"""
Module: RecurrentNNFactory
"""
from IA.RNN.RNNBase import RNNBase
from IA.RNN.RNNTime import RNNTime
from IA.RNN.RNNPSD import RNNPSD
from IA.RNN.RNNSpectogram import RNNSpectrogram

def model_by_signal_type(signal_type: str, input_shape) -> RNNBase:
    if signal_type == "time":
        return RNNTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return RNNPSD(input_shape=input_shape)
    
    elif signal_type == "spectrogram":
        return RNNSpectrogram(input_shape=input_shape)
    
    else:
        return RNNBase()
