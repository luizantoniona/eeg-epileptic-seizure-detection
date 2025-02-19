from Object.Summary import Summary
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Normalizer:
    """
    Class: Normalizer

    This class provides functions to normalize data using MinMaxScaler.
    """

    @staticmethod
    def normalize(summaries: list[Summary]):
        """
        Normalize the data in each summary.
        """
        scaler = MinMaxScaler()

        shape_size = len(summaries[0].signal.data_segmented[0].shape)

        if shape_size == 2:
            for summary in summaries:
                all_samples = np.concatenate(summary.signal.data_segmented)
                scaler.fit_transform(all_samples)
                summary.signal.data_segmented = [scaler.transform(sample) for sample in summary.signal.data_segmented]

        elif shape_size == 3:
            for summary in summaries:
                all_samples = np.concatenate([sample for segment in summary.signal.data_segmented for sample in segment])
                scaler.fit(all_samples)
                summary.signal.data_segmented = [[scaler.transform(sample) for sample in segment] for segment in summary.signal.data_segmented]

        else:
            raise ValueError(f"Unsupported data shape: {summaries[0].signal.data_segmented[0].shape}")
