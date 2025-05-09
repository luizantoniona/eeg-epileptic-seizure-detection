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

        del summaries
        gc.collect()

        data, labels = Balancer.balance(data=data, labels=labels)

        data = Transposer.transpose(signal_type=signal_type, model_type=model_type, data=data)
        print("DATA SHAPE:", data.shape)

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

    @staticmethod
    def preprocess_with_size(dataset_type: DatasetTypeEnum, signal_type: SignalTypeEnum, model_type: NeuralNetworkTypeEnum, window_length: int, nr_files: int = 0):
        """
        Preprocess the data by loading, normalizing, balancing, and transposing it.

        Args:
            dataset_type (DatasetTypeEnum): Type of dataset to load.
            signal_type (SignalTypeEnum): Type of signal to load.
            model_type (NeuralNetworkTypeEnum): Type of neural network model to use for data adaptation.
            window_length (int): Length of the window used for segmenting the data.
            nr_files (int): Number of files to preprocess.

        Returns:
            tuple: Processed data and corresponding labels.
        """

        mne.utils.set_log_level("CRITICAL")

        summaries = Loader.load_anomalous_summaries(dataset_type=dataset_type)[0:nr_files]

        Loader.load_segmented_data(summaries, signal_type=signal_type, window_length=window_length)

        Normalizer.normalize(summaries=summaries)

        data, labels = Preprocessor.prepare(summaries=summaries)

        del summaries
        gc.collect()

        data, labels = Balancer.balance(data=data, labels=labels)

        data = Transposer.transpose(signal_type=signal_type, model_type=model_type, data=data)

        return data, labels

    @staticmethod
    def preprocess_with_file_name(dataset_type: DatasetTypeEnum, signal_type: SignalTypeEnum, model_type: NeuralNetworkTypeEnum, window_length: int, overlap_shift_size: int, file_name: str = ""):
        """
        Preprocess the data by loading, normalizing, balancing, and transposing it.

        Args:
            dataset_type (DatasetTypeEnum): Type of dataset to load.
            signal_type (SignalTypeEnum): Type of signal to load.
            model_type (NeuralNetworkTypeEnum): Type of neural network model to use for data adaptation.
            window_length (int): Length of the window used for segmenting the data.
            file_name (str): Name of the file to preprocess.

        Returns:
            tuple: Processed data and corresponding labels.
        """

        mne.utils.set_log_level("CRITICAL")

        summaries = Loader.load_summary(dataset_type=dataset_type, file_name=file_name)

        Loader.load_segmented_data(summaries, signal_type=signal_type, window_length=window_length, overlap_shift_size=overlap_shift_size)

        Normalizer.normalize(summaries=summaries)

        data, labels = Preprocessor.prepare(summaries=summaries)

        del summaries
        gc.collect()

        data = Transposer.transpose(signal_type=signal_type, model_type=model_type, data=data)

        return data, labels
