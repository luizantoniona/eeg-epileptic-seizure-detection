"""
Module: summary_splitter

This module provides functions to split summary data into training and validation sets.
"""

import model.summary_model as sm
from sklearn.model_selection import train_test_split

def summaries_data_splitter(summaries: list[sm.SummaryModel], split_size=0.2) -> tuple[list[sm.SummaryModel], list[sm.SummaryModel]]:
    """
    Split summary data into training and validation sets for model training.
    """
    X_train, X_val = train_test_split(summaries, test_size=split_size, random_state=42)

    return X_train, X_val
