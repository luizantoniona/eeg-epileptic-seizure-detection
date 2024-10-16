from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import Dataset.DatasetConfigure as DatasetConfigure
from Dataset.DatasetTypeEnum import dataset_enum_by_name


class DatasetConfigurationThread(QThread):
    finished = pyqtSignal()

    def __init__(self, dataset_name):
        super().__init__()
        self.dataset_type = dataset_enum_by_name(dataset_name)

    def run(self):
        DatasetConfigure.configure(dataset_type=self.dataset_type)
        self.finished.emit()
