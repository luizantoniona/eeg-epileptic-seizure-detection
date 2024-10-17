from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
from Preprocessor.Preprocessor import Preprocessor
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name
from Trainer.Trainer import Trainer


class TrainThread(QThread):
    finished = pyqtSignal()

    def __init__(self, dataset_name, network_name, signal_name, window_size):
        super().__init__()
        self.DATASET = dataset_enum_by_name(dataset_name)
        self.MODEL = neural_network_enum_by_name(network_name)
        self.DOMAIN = signal_enum_by_name(signal_name)
        self.WINDOW = window_size

    def run(self):
        print("PREPROCESSOR STARTED")
        data, labels = Preprocessor.preprocess(dataset_type=self.DATASET, model_type=self.MODEL, signal_type=self.DOMAIN, window_length=self.WINDOW)
        print("PREPROCESSOR FINISHED")

        print("TRAINING STARTED")
        Trainer.train(dataset_type=self.DATASET, model_type=self.MODEL, signal_type=self.DOMAIN, window_length=self.WINDOW, data=data, labels=labels)
        print("TRAINING FINISHED")

        self.finished.emit()
