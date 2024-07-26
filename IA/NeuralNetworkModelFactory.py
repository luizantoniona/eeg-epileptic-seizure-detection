"""
Module: NeuralNetworkModelFactory
"""
from IA.NNBase import NNBase
import IA.CNN.ConvolutionalNNFactory as ConvolutionalNNFactory
import IA.RNN.RecurrentNNFactory as RecurrentNNFactory
import IA.CRNN.ConvolutionalRecurrentNNFactory as ConvolutionalRecurrentNNFactory

def model_by_type(model_type: str, signal_type: str, input_shape, window_length: int) -> NNBase:

    if model_type == "CNN":
        return ConvolutionalNNFactory.model_by_signal_type(signal_type=signal_type,
                                                           input_shape=input_shape,
                                                           window_length=window_length)
    
    elif model_type == "RNN":
        return RecurrentNNFactory.model_by_signal_type(signal_type=signal_type,
                                                       input_shape=input_shape,
                                                       window_length=window_length)

    elif model_type == "CRNN":  
        return ConvolutionalRecurrentNNFactory.model_by_signal_type(signal_type=signal_type,
                                                                    input_shape=input_shape,
                                                                    window_length=window_length)

    else:
        return NNBase()