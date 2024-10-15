"""
Module: NeuralNetworkModelFactory
"""

from Object.Signal.SignalTypeEnum import SignalTypeEnum
from IA.NNBase import NNBase
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
import IA.CNN.ConvolutionalNNFactory as ConvolutionalNNFactory
import IA.RNN.RecurrentNNFactory as RecurrentNNFactory
import IA.CRNN.ConvolutionalRecurrentNNFactory as ConvolutionalRecurrentNNFactory


def model_by_type(model_type: NeuralNetworkTypeEnum, signal_type: SignalTypeEnum, input_shape, window_length: int) -> NNBase:

    match model_type:
        case NeuralNetworkTypeEnum.RNN:
            return RecurrentNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape, window_length=window_length)

        case NeuralNetworkTypeEnum.CNN:
            return ConvolutionalNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape, window_length=window_length)

        case NeuralNetworkTypeEnum.CRNN:
            return ConvolutionalRecurrentNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape, window_length=window_length)

        case _:
            return NNBase()
