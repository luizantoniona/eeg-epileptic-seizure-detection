from Object.Summary import Summary
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Normalizer:
    """
    Class: Normalizer

    This class provides functions to normalize data.
    """

    @staticmethod
    def normalize(data: np.ndarray):
        """
        Normalize the provided data using MinMaxScaler.
        """
        scaler = MinMaxScaler()

        if data.ndim == 2:
            data[:] = scaler.fit_transform(data)

        elif data.ndim == 3:
            for i in range(data.shape[0]):
                data[i] = scaler.fit_transform(data[i])

        elif data.ndim == 4:
            samples, channels, _, _ = data.shape

            for i in range(samples):
                for j in range(channels):
                    data[i, j] = scaler.fit_transform(data[i, j])
        else:
            raise ValueError(f"Unsupported data shape: {data.shape}")
