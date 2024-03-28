"""
Module: frequency_normalizer

This module provides functions to normalize frequency data.
"""
from model.summary_model import SummaryModel
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize_frequency_data(summaries: list[SummaryModel]):
    """
    Normalize the frequency data in each summary.
    """
    scaler = MinMaxScaler()
    for summary in summaries:
        all_samples = np.concatenate(summary.signal.freq_segments)
        scaler.fit_transform(all_samples)
        summary.signal.freq_segments = [scaler.transform(sample) for sample in summary.signal.freq_segments]
