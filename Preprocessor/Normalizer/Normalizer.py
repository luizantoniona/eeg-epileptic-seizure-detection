"""
Module: Normalizer

This module provides functions to normalize data.
"""
from Object.Summary import Summary
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def normalize(summaries: list[Summary]):
    """
    Normalize the time data in each summary.
    """
    scaler = MinMaxScaler()

    for summary in summaries:
        for i in range(len(summary.signal.data_segmented)):
            segment = summary.signal.data_segmented[i]
            
            if len(segment.shape) == 2:
                # Case: (18, 1281) - Data is already in the desired format
                normalized_segment = scaler.fit_transform(segment)
                summary.signal.data_segmented[i] = normalized_segment
            
            elif len(segment.shape) == 3:
                # Case: (18, 8, 1281) - Handle each sub-segment
                normalized_subsegments = []
                
                for subsegment in segment:
                    normalized_subsegment = scaler.fit_transform(subsegment)
                    normalized_subsegments.append(normalized_subsegment)
                
                summary.signal.data_segmented[i] = np.array(normalized_subsegments)
            
            else:
                raise ValueError(f"Unsupported data shape: {segment.shape}")
