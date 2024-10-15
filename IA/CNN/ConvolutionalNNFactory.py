"""
Module: ConvolutionalNNFactory
"""

from Object.Signal.SignalTypeEnum import SignalTypeEnum
from IA.CNN.CNNBase import CNNBase
from IA.CNN.CNNTime import CNNTime
from IA.CNN.CNNPSD import CNNPSD
from IA.CNN.CNNSpectrogram import CNNSpectrogram


def model_by_signal_type(signal_type: SignalTypeEnum, input_shape, window_length: int) -> CNNBase:
    match signal_type:
        case SignalTypeEnum.Time:
            return CNNTime(input_shape=input_shape, window_length=window_length)

        case SignalTypeEnum.PSD:
            return CNNPSD(input_shape=input_shape, window_length=window_length)

        case SignalTypeEnum.Spectrogram:
            return CNNSpectrogram(input_shape=input_shape, window_length=window_length)

        case _:
            return CNNBase(input_shape=input_shape, window_length=window_length)
