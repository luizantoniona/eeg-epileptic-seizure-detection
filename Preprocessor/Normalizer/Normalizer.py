"""
Module: Normalizer

This module provides functions to normalize data.
"""
from Object.Summary import Summary
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize(summaries: list[Summary]):
    """
    Normalize the time data in each summary.
    """
    scaler = MinMaxScaler()

    for summary in summaries:
        all_samples = np.concatenate(summary.signal.data_segmented)
        scaler.fit_transform(all_samples)
        summary.signal.data_segmented = [scaler.transform(sample) for sample in summary.signal.data_segmented]
