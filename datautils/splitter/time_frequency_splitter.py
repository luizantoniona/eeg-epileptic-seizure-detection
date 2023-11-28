"""
Module: time_frequency_splitter

This module provides functions to split summary data into training and validation sets based on time-frequency-domain.
"""

import model.summarymodel as sm
import datautils.splitter.summary_splitter as splitter
import numpy as np

def time_frequency_data_splitter(summaries: list[sm.SummaryModel]):
    """Split summaries into training and validation sets based on time-frequency data."""
    X_train, X_val, y_train, y_val = splitter.summaries_data_splitter(summaries)

    X_train_time_freq_data = [summary.signal.get_time_freq_data() for summary in X_train]
    X_val_time_freq_data = [summary.signal.get_time_freq_data() for summary in X_val]

    return X_train_time_freq_data, X_val_time_freq_data, y_train, y_val

def segmented_time_frequency_data_splitter(summaries: list[sm.SummaryModel]):
    """Split segmented summaries into training and validation sets based on time-frequency data."""
    X_train, X_val, y_train, y_val = splitter.segmented_summaries_data_splitter(summaries)

    X_train_segmented_time_freq_data = np.concatenate([summary.signal.get_time_freq_segmented_data() for summary in X_train])
    X_val_segmented_time_freq_data = np.concatenate([summary.signal.get_time_freq_segmented_data() for summary in X_val])

    return X_train_segmented_time_freq_data, X_val_segmented_time_freq_data, y_train, y_val