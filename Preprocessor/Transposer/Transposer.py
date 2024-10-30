import numpy as np
from IA.NeuralNetworkTypeEnum import NeuralNetworkTypeEnum
from Object.Signal.SignalTypeEnum import SignalTypeEnum


class Transposer:
    @staticmethod
    def transpose(signal_type: SignalTypeEnum, model_type: NeuralNetworkTypeEnum, data):
        """
        Transposes the input data based on the type of signal and model being used.

        Parameters:
        - dataset_type (DatasetTypeEnum): Type of dataset being used.
        - signal_type (SignalTypeEnum): Type of signal being processed.
        - model_type (NeuralNetworkTypeEnum): Type of neural network model being used.
        - data: Data to be transposed (typically a NumPy array or similar structure).
        """

        if signal_type == SignalTypeEnum.Time:
            data = np.transpose(data, axes=(0, 2, 1))

            if model_type != NeuralNetworkTypeEnum.RNN:
                data = np.expand_dims(data, axis=-1)

        elif signal_type == SignalTypeEnum.PSDWelch or signal_type == SignalTypeEnum.PSDMultitaper:
            if model_type != NeuralNetworkTypeEnum.RNN:
                data = np.expand_dims(data, axis=-1)

        elif signal_type == SignalTypeEnum.Spectrogram:
            data = np.transpose(data, axes=(0, 3, 2, 1))

        else:
            print("TRANSPOSER - Não implementado")

        return data
