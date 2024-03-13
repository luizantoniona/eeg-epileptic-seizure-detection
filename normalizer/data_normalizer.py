"""
Module: data_normalizer

This module provides functions to normalize data.
"""
from model.summary_model import SummaryModel
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize_time_data(summaries: list[SummaryModel]):
    """
    Normalize the time data in each summary.
    """
    scaler = MinMaxScaler()
    for summary in summaries:
        all_samples = np.concatenate(summary.signal.time_segments)
        scaler.fit_transform(all_samples)
        summary.signal.time_segments = [scaler.transform(sample) for sample in summary.signal.time_segments]
