"""
Module: ConvolutionalRecurrentNNFactory
"""

from Object.Signal.SignalTypeEnum import SignalTypeEnum
from IA.CRNN.CRNNBase import CRNNBase
from IA.CRNN.CRNNTime import CRNNTime
from IA.CRNN.CRNNPSD import CRNNPSD
from IA.CRNN.CRNNSpectogram import CRNNSpectrogram


def model_by_signal_type(signal_type: SignalTypeEnum, input_shape, window_length: int) -> CRNNBase:
    match signal_type:
        case SignalTypeEnum.Time:
            return CRNNTime(input_shape=input_shape, window_length=window_length)

        case SignalTypeEnum.PSD:
            return CRNNPSD(input_shape=input_shape, window_length=window_length)

        case SignalTypeEnum.Spectrogram:
            return CRNNSpectrogram(input_shape=input_shape, window_length=window_length)

        case _:
            return CRNNBase(input_shape=input_shape, window_length=window_length)
