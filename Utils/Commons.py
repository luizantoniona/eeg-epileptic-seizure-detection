from Dataset.DatasetTypeEnum import dataset_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name


def datasets():
    return dataset_enum_by_name("CHBMIT")


def signals():
    return [
        signal_enum_by_name("Time"),
        signal_enum_by_name("PSDWelch"),
        signal_enum_by_name("PSDMultitaper"),
        signal_enum_by_name("Spectrogram"),
    ]


def models():
    return [
        neural_network_enum_by_name("RNN"),
        neural_network_enum_by_name("CNN"),
        neural_network_enum_by_name("CRNN"),
    ]


def windows():
    return [
        1,
        2,
        5,
        10,
    ]
