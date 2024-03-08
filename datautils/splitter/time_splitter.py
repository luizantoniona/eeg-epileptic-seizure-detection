"""
Module: time_splitter

This module provides functions to split summary data into training and validation sets based on time-domain.
"""

import model.summary_model as sm
import datautils.splitter.summary_splitter as splitter
import numpy as np

def segmented_time_data_splitter(summaries: list[sm.SummaryModel], split_size=0.2):
    """
    Split segmented summaries into training and validation sets based on time-domain data.
    """
    X_train, X_val = splitter.summaries_data_splitter(summaries, split_size)

    y_train = np.concatenate([summary.signal.get_label_segments() for summary in X_train])
    y_val = np.concatenate([summary.signal.get_label_segments() for summary in X_val])

    X_train_segmented_time_data = np.concatenate([summary.signal.get_time_segmented_data() for summary in X_train])
    X_val_segmented_time_data = np.concatenate([summary.signal.get_time_segmented_data() for summary in X_val])

    return X_train_segmented_time_data, X_val_segmented_time_data, y_train, y_val
