from Database.DatabaseSummary import DatabaseSummary
from Dataset.DatasetTypeEnum import DatasetTypeEnum
import Dataset.CHBMIT.ConfigureCHBMIT as ConfigureCHBMIT


def configure(dataset_type: DatasetTypeEnum):
    match dataset_type:
        case DatasetTypeEnum.CHBMIT:
            ConfigureCHBMIT.download_and_process()
            return

        case _:
            print("Not Mapped")


def is_configured(dataset_type: DatasetTypeEnum) -> bool:
    match dataset_type:
        case DatasetTypeEnum.CHBMIT:
            return len(DatabaseSummary().summaries_with_anomaly(dataset_name=dataset_type.name)) >= 112

        case _:
            print("Not Mapped")
            return False
