from enum import Enum


class SignalTypeEnum(Enum):
    NONE = 0
    Time = 1
    PSD = 2
    Spectrogram = 3


def signal_enum_by_name(signal_name: str) -> SignalTypeEnum:
    dataset_map = {
        "Time": SignalTypeEnum.Time,
        "PSD": SignalTypeEnum.PSD,
        "Spectrogram": SignalTypeEnum.Spectrogram,
    }

    if signal_name in dataset_map:
        return dataset_map[signal_name]

    print(f"Unknown signal name: {signal_name}")
    return SignalTypeEnum.NONE
