from enum import Enum


class NeuralNetworkTypeEnum(Enum):
    NONE = 0
    RNN = 1
    CNN = 2
    CRNN = 3


def neural_network_enum_by_name(neural_network_name: str) -> NeuralNetworkTypeEnum:
    dataset_map = {
        "RNN": NeuralNetworkTypeEnum.RNN,
        "CNN": NeuralNetworkTypeEnum.CNN,
        "CRNN": NeuralNetworkTypeEnum.CRNN,
    }

    if neural_network_name in dataset_map:
        return dataset_map[neural_network_name]

    print(f"NeuralNetworkTypeEnum [NOT_MAPPED]: {neural_network_name}")
    return NeuralNetworkTypeEnum.NONE
