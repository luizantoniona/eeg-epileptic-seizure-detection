import gc
import mne
import numpy as np
from Object.Summary import Summary
from sklearn.preprocessing import LabelEncoder
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
from Dataset.DatasetTypeEnum import DatasetTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum
from Preprocessor.Balancer.Balancer import Balancer
from Preprocessor.Loader.Loader import Loader
from Preprocessor.Normalizer.Normalizer import Normalizer
from Preprocessor.Transposer.Transposer import Transposer


class Preprocessor:
    """
    The Preprocessor class provides static methods to handle the end-to-end data preprocessing pipeline,
    including data loading, normalization, balancing, and transposition.
    """

    @staticmethod
    def preprocess(dataset_type: DatasetTypeEnum, signal_type: SignalTypeEnum, model_type: NeuralNetworkTypeEnum, window_length: int):
        """
        Preprocess the data by loading, normalizing, balancing, and transposing it.

        Args:
            dataset_type (DatasetTypeEnum): Type of dataset to load.
            signal_type (SignalTypeEnum): Type of signal to load.
            model_type (NeuralNetworkTypeEnum): Type of neural network model to use for data adaptation.
            window_length (int): Length of the window used for segmenting the data.

        Returns:
            tuple: Processed data and corresponding labels.
        """
        mne.utils.set_log_level("CRITICAL")

        summaries = Loader.load_anomalous_summaries(dataset_type=dataset_type)

        Loader.load_segmented_data(summaries, signal_type=signal_type, window_length=window_length)

        Normalizer.normalize(summaries=summaries)

        data, labels = Preprocessor.prepare(summaries=summaries)
        data, labels = Balancer.balance(data=data, labels=labels)

        print("DATA SHAPE:", data.shape)

        Transposer.transpose(signal_type=signal_type, model_type=model_type, data=data)

        del summaries
        gc.collect()

        return data, labels

    @staticmethod
    def prepare(summaries: list[Summary]):
        """
        Prepares data by concatenating segmented data and labels from the provided summaries.

        Args:
            summaries (list[Summary]): List of Summary objects containing data segments and labels.

        Returns:
            tuple: A tuple containing the concatenated segmented data (ndarray) and encoded labels (ndarray).
        """

        all_segmented_data = np.concatenate([summary.signal.get_data_segmented() for summary in summaries])
        all_segmented_label = np.concatenate([summary.signal.get_label_segmented() for summary in summaries])

        label_encoder = LabelEncoder()
        label_encoder.fit(all_segmented_label)
        all_segmented_label = label_encoder.transform(all_segmented_label)

        return all_segmented_data, all_segmented_label
