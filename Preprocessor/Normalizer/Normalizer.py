from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Normalizer:
    """
    Class: Normalizer

    This class provides functions to normalize data using MinMaxScaler.
    """

    @staticmethod
    def normalize(data: np.ndarray) -> np.ndarray:
        """
        Normalize the provided data using MinMaxScaler, ensuring global scaling.

        Args:
            data (np.ndarray): Input data to normalize.

        Returns:
            np.ndarray: Normalized data.
        """
        scaler = MinMaxScaler()

        if data.ndim == 2:
            return scaler.fit_transform(data)

        elif data.ndim == 3:
            samples, features, channels = data.shape
            scaled_data = np.empty_like(data)

            for i in range(channels):
                scaled_data[:, :, i] = scaler.fit_transform(data[:, :, i])

            return scaled_data

        elif data.ndim == 4:
            samples, channels, height, width = data.shape
            scaled_data = np.empty_like(data)

            for i in range(channels):
                reshaped = data[:, i].reshape(samples, -1)
                scaled = scaler.fit_transform(reshaped)
                scaled_data[:, i] = scaled.reshape(samples, height, width)

            return scaled_data

        else:
            raise ValueError(f"Unsupported data shape: {data.shape}")
