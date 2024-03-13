"""
Module: time_splitter

This module provides functions to split summary data into training, validation and test sets based on time-domain.
"""

import model.summary_model as sm
import splitter.summary_splitter as splitter
import numpy as np
from sklearn.utils import shuffle

def test_segmented_time_data(summaries: list[sm.SummaryModel]):
    X_test = summaries

    y_test = np.concatenate([summary.signal.get_label_segments() for summary in X_test])

    X_test_segmented_time_data = np.concatenate([summary.signal.get_time_segmented_data() for summary in X_test])

    return X_test_segmented_time_data, y_test

def train_val_segmented_time_data(summaries: list[sm.SummaryModel], split_size=0.2):
    """
    Split segmented summaries into training and validation sets based on time-domain data.
    """
    X_train, X_val = splitter.summaries_data_splitter(summaries, split_size)

    y_train = np.concatenate([summary.signal.get_label_segments() for summary in X_train])
    y_val = np.concatenate([summary.signal.get_label_segments() for summary in X_val])

    X_train_segmented_time_data = np.concatenate([summary.signal.get_time_segmented_data() for summary in X_train])
    X_val_segmented_time_data = np.concatenate([summary.signal.get_time_segmented_data() for summary in X_val])

    X_train_segmented_time_data, y_train = shuffle(X_train_segmented_time_data, y_train, random_state=0)

    return X_train_segmented_time_data, X_val_segmented_time_data, y_train, y_val
