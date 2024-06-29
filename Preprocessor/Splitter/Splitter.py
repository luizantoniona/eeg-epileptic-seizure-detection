"""
Module: Splitter

This module provides functions to split data into training, validation and test sets.
"""
from Object.Summary import Summary
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np

def split(summaries: list[Summary], train_size, val_size, test_size, random_state=42):
    """
    Splits data into training, validation, and test subsets.

    Parameters:
    - summaries (list): List of Summary to split.
    - train_size (float): Proportion of the data to include in the training set.
    - val_size (float): Proportion of the data to include in the validation set.
    - test_size (float): Proportion of the data to include in the test set.
    - random_state (int, optional): Controls the shuffling applied to the data before splitting.

    Returns:
    - X_train (list): Training data subset.
    - y_train (list): Training labels subset.
    - X_validation (list): Validation data subset.
    - y_validation (list): Validation labels subset.
    - X_test (list): Test data subset.
    - y_test (list): Test labels subset.
    """

    all_segmented_data = np.concatenate([summary.signal.get_data_segmented() for summary in summaries])
    all_segmented_label = np.concatenate([summary.signal.get_label_segmented() for summary in summaries])

    label_encoder = LabelEncoder()
    label_encoder.fit(all_segmented_label)
    all_segmented_label = label_encoder.transform(all_segmented_label)

    total_size = train_size + val_size + test_size
    if not abs(total_size - 1.0) < 1e-9:
        print(train_size + val_size + test_size)
        raise ValueError("train_size, val_size, and test_size must sum to 1.0")

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        all_segmented_data, all_segmented_label, test_size=test_size, random_state=random_state)

    val_relative_size = val_size / (train_size + val_size)

    X_train, X_validation, y_train, y_validation = train_test_split(
        X_train_val, y_train_val, test_size=val_relative_size, random_state=random_state)

    return X_train, y_train, X_validation, y_validation, X_test, y_test
