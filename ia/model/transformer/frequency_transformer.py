"""
Module: frequency_transformer

This module provides Transformer's models for frequency domain
"""

import tensorflow as tf

class FrequnecyTransformer:
    """
    Transformer Model for time data training
    """
    def __init__(self):
        self.model = tf.keras.Sequential()