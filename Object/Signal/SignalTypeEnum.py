from enum import Enum


class SignalTypeEnum(Enum):
    NONE = 0
    Time = 1
    PSDWelch = 2
    PSDMultitaper = 3
    Spectrogram = 4


def signal_enum_by_name(signal_name: str) -> SignalTypeEnum:
    dataset_map = {
        "Time": SignalTypeEnum.Time,
        "PSDWelch": SignalTypeEnum.PSDWelch,
        "PSDMultitaper": SignalTypeEnum.PSDMultitaper,
        "Spectrogram": SignalTypeEnum.Spectrogram,
    }

    if signal_name in dataset_map:
        return dataset_map[signal_name]

    print(f"SignalTypeEnum [NOT_MAPPED]: {signal_name}")
    return SignalTypeEnum.NONE
