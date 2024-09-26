"""
Module: RecurrentNNFactory
"""
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from IA.RNN.RNNBase import RNNBase
from IA.RNN.RNNTime import RNNTime
from IA.RNN.RNNPSD import RNNPSD
from IA.RNN.RNNSpectogram import RNNSpectrogram

def model_by_signal_type(signal_type: SignalTypeEnum, input_shape, window_length: int) -> RNNBase:
    match signal_type:
        case SignalTypeEnum.Time:
            return RNNTime(input_shape=input_shape, window_length=window_length)

        case SignalTypeEnum.PSD:
            return RNNPSD(input_shape=input_shape, window_length=window_length)

        case SignalTypeEnum.Spectrogram:
            return RNNSpectrogram(input_shape=input_shape, window_length=window_length)

        case _:
            return RNNBase(input_shape=input_shape, window_length=window_length)
