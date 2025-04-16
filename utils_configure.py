import Database.DatabaseConfiguration as DBConfig
import Dataset.DatasetConfigure as DTConfig
from Dataset.DatasetTypeEnum import DatasetTypeEnum

if not DBConfig.is_configured():
    DBConfig.configure()


if not DTConfig.is_configured(DatasetTypeEnum.CHBMIT):
    DTConfig.configure(DatasetTypeEnum.CHBMIT)
