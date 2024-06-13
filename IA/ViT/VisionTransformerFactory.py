"""
Module: VisionTransformerFactory
"""
from IA.ViT.ViTBase import ViTBase
from IA.ViT.ViTTime import ViTTime
from IA.ViT.ViTPSD import ViTPSD

def model_by_signal_type(signal_type: str, input_shape) -> ViTBase:
    if signal_type == "time":
        return ViTTime(input_shape=input_shape)
    
    elif signal_type == "PSD":
        return ViTPSD(input_shape=input_shape)
    
    #TODO: Spectogram ViT
    
    else:
        return ViTBase()