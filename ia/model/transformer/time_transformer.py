"""
Module: time_transformer

This module provides Transformer's models for time domain
"""

import tensorflow as tf

class TimeTransformer:
    """
    Transformer Model for time data training
    """
    def __init__(self):
        self.model = tf.keras.Sequential()