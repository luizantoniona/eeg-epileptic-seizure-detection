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


def is_configured(dataset_type: DatasetTypeEnum):
    match dataset_type:
        case DatasetTypeEnum.CHBMIT:
            """"""
        case _:
            print("Not Mapped")
