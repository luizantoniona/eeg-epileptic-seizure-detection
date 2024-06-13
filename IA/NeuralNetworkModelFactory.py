"""
Module: NeuralNetworkModelFactory
"""
from IA.NNBase import NNBase
import IA.CNN.ConvolutionalNNFactory as ConvolutionalNNFactory
import IA.RNN.RecurrentNNFactory as RecurrentNNFactory
import IA.CRNN.ConvolutionalRecurrentNNFactory as ConvolutionalRecurrentNNFactory
import IA.SNN.SiameseNNFactory as SiameseNNFactory
import IA.ViT.VisionTransformerFactory as VisionTransformerFactory

def model_by_type(model_type: str, signal_type: str, input_shape) -> NNBase:

    if model_type == "CNN":
        return ConvolutionalNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape)
    
    elif model_type == "RNN":
        return RecurrentNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape)

    elif model_type == "CRNN":  
        return ConvolutionalRecurrentNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape)
    
    elif model_type == "SNN":
        return SiameseNNFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape)

    elif model_type == "ViT":
        return VisionTransformerFactory.model_by_signal_type(signal_type=signal_type, input_shape=input_shape)

    else:
        return NNBase()