"""
Module: RecurrentNNFactory
"""
from IA.RNN.RNNBase import RNNBase
from IA.RNN.RNNTime import RNNTime
from IA.RNN.RNNPSD import RNNPSD
from IA.RNN.RNNSpectogram import RNNSpectrogram

def model_by_signal_type(signal_type: str, input_shape, window_length: int) -> RNNBase:
    if signal_type == "time":
        return RNNTime(input_shape=input_shape, window_length=window_length)
    
    elif signal_type == "PSD":
        return RNNPSD(input_shape=input_shape, window_length=window_length)
    
    elif signal_type == "spectrogram":
        return RNNSpectrogram(input_shape=input_shape, window_length=window_length)
    
    else:
        return RNNBase(input_shape=input_shape, window_length=window_length)
