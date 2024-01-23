"""
Module: data_normalizer

This module provides functions to normalize data.
"""

from sklearn.preprocessing import MinMaxScaler

def normalize(data):
    """
    """
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data.reshape(data.shape[0], -1)).reshape(data.shape)