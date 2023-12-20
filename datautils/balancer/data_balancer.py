"""
Module: data_balancer
"""
import numpy as np

def balance(data, labels) -> None:
    """
    
    """

    unique_labels, counts = np.unique(labels, return_counts=True)

    min_count = np.min(counts)

    balanced_features = []
    balanced_labels = []

    for label in unique_labels:
        indices = np.where(labels == label)[0]
        
        selected_indices = np.random.choice(indices, size=min_count, replace=False)
        selected_indices = np.array(selected_indices, dtype=int)
        
        balanced_features.extend(data[selected_indices])
        balanced_labels.extend(labels[selected_indices])

    balanced_features = np.array(balanced_features)
    balanced_labels = np.array(balanced_labels)

    return balanced_features, balanced_labels