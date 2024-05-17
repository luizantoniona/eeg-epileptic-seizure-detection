"""
Module: summary_splitter

This module provides functions to split summary data into training and validation sets.
"""

import Object.Summary as Summary
from sklearn.model_selection import train_test_split

def summaries_data_splitter(summaries: list[Summary.Summary], split_size=0.2) -> tuple[list[Summary.Summary], list[Summary.Summary]]:
    """
    Split summary data into training and validation sets for model training.
    """
    X_train, X_val = train_test_split(summaries, test_size=split_size, random_state=42)

    return X_train, X_val
