from enum import Enum


class DatasetTypeEnum(Enum):
    CHBMIT = 1


def dataset_enum_by_name(dataset_name: str) -> DatasetTypeEnum:
    dataset_map = {
        "CHBMIT": DatasetTypeEnum.CHBMIT,
    }

    if dataset_name in dataset_map:
        return dataset_map[dataset_name]

    raise ValueError(f"Unknown dataset name: {dataset_name}")
