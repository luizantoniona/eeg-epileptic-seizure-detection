"""
Module: frequency_splitter

This module provides functions to split summary data into training and validation sets based on frequency-domain.
"""

import Object.Summary as Summary
import numpy as np
import Preprocessor.Splitter.summary_splitter as splitter

def test_segmented_frequency_data(summaries: list[Summary.Summary]):
    X_test = summaries

    y_test = np.concatenate([summary.signal.get_label_segments() for summary in X_test])

    X_test_segmented_freq_data = np.concatenate([summary.signal.get_freq_segmented_data() for summary in X_test])

    return X_test_segmented_freq_data, y_test

def train_val_segmented_frequency_data(summaries: list[Summary.Summary], split_size=0.2):
    """
    Split segmented summaries into training and validation sets based on frequency-domain data.
    """
    X_train, X_val = splitter.summaries_data_splitter(summaries, split_size)

    y_train = np.concatenate([summary.signal.get_label_segments() for summary in X_train])
    y_val = np.concatenate([summary.signal.get_label_segments() for summary in X_val])

    X_train_segmented_freq_data = np.concatenate([summary.signal.get_freq_segmented_data() for summary in X_train])
    X_val_segmented_freq_data = np.concatenate([summary.signal.get_freq_segmented_data() for summary in X_val])

    return X_train_segmented_freq_data, X_val_segmented_freq_data, y_train, y_val
