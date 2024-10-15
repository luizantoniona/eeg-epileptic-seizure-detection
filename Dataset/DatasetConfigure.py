from Database.DatabaseSummary import DatabaseSummary
from Dataset.DatasetTypeEnum import DatasetTypeEnum
import Dataset.CHBMIT.DatabaserCHBMIT as DatabaserCHBMIT
import Dataset.CHBMIT.DownloaderCHBMIT as DownloaderCHBMIT


def configure(dataset_type: DatasetTypeEnum):
    match dataset_type:
        case DatasetTypeEnum.CHBMIT:
            DownloaderCHBMIT.download()
            DatabaserCHBMIT.execute()
            return

        case _:
            print("Not Mapped")


def is_configured(dataset_type: DatasetTypeEnum) -> bool:
    match dataset_type:
        case DatasetTypeEnum.CHBMIT:
            return len(DatabaseSummary().summaries_with_anomaly(dataset_name=dataset_type.name)) > 0

        case _:
            print("Not Mapped")
            return False
