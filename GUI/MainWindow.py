import sys
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from GUI.Component.DatabaseWidget import DatabaseWidget
from GUI.Component.DatasetWidget import DatasetWidget
from GUI.Component.DomainWidget import DomainWidget
from GUI.Component.InfoPanelWidget import InfoPanelWidget
from GUI.Component.NeuralNetworkWidget import NeuralNetworkWidget
from GUI.Component.WindowSizeWidget import WindowSizeWidget
from Metric.Evaluator import Evaluator
from Preprocessor.Preprocessor import Preprocessor
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name

TITLE = "EEG Aplication"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.setGeometry(100, 100, 800, 800)

        self.database_widget = DatabaseWidget()

        self.dataset_widget = DatasetWidget()
        self.dataset_widget.currentIndexChanged.connect(self.check_conditions)

        self.network_widget = NeuralNetworkWidget()
        self.network_widget.currentIndexChanged.connect(self.check_conditions)

        self.domain_widget = DomainWidget()
        self.domain_widget.currentIndexChanged.connect(self.check_conditions)

        self.window_widget = WindowSizeWidget()
        self.window_widget.currentIndexChanged.connect(self.check_conditions)

        self.info_panel_widget = InfoPanelWidget()
        sys.stdout = self.info_panel_widget

        self.train_button = QPushButton("Train")
        self.train_button.setEnabled(False)
        self.train_button.clicked.connect(self.train_model)

        self.evaluate_button = QPushButton("Evaluate")
        self.evaluate_button.setEnabled(False)
        self.evaluate_button.clicked.connect(self.evaluate_model)

        self.mainLayout = QHBoxLayout()
        self.selectionLayout = QVBoxLayout()
        self.infoLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.selectionLayout.addWidget(self.database_widget)
        self.selectionLayout.addWidget(self.dataset_widget)
        self.selectionLayout.addWidget(self.network_widget)
        self.selectionLayout.addWidget(self.domain_widget)
        self.selectionLayout.addWidget(self.window_widget)

        self.infoLayout.addWidget(self.info_panel_widget)

        self.buttonLayout.addWidget(self.train_button)
        self.buttonLayout.addWidget(self.evaluate_button)

        self.selectionLayout.addLayout(self.buttonLayout)
        self.mainLayout.addLayout(self.selectionLayout)
        self.mainLayout.addLayout(self.infoLayout)

        self.setLayout(self.mainLayout)

    def check_conditions(self):
        if self.database_widget.get_checked() and self.dataset_widget.get_checked() and self.network_widget.get_checked() and self.domain_widget.get_checked() and self.window_widget.get_checked():
            self.train_button.setEnabled(True)
            self.evaluate_button.setEnabled(True)

        else:
            self.train_button.setEnabled(False)
            self.evaluate_button.setEnabled(False)

    def evaluate_model(self):
        self.info_panel_widget.clear()
        DATASET = dataset_enum_by_name(self.dataset_widget.dataset)
        MODEL = neural_network_enum_by_name(self.network_widget.network)
        DOMAIN = signal_enum_by_name(self.domain_widget.domain)
        WINDOW = self.window_widget.window_size
        model_evaluation = Evaluator(dataset_type=DATASET, model_type=MODEL, signal_type=DOMAIN, window_length=WINDOW)

        try:
            model_evaluation.info()
            model_evaluation.samples()
            model_evaluation.report()

        except:
            self.info_panel_widget.clear()
            model_evaluation.info()
            print("MODEL NOT TRAINED")

    def train_model(self):
        self.info_panel_widget.clear()
        DATASET = dataset_enum_by_name(self.dataset_widget.dataset)
        MODEL = neural_network_enum_by_name(self.network_widget.network)
        DOMAIN = signal_enum_by_name(self.domain_widget.domain)
        WINDOW = self.window_widget.window_size

        print("PREPROCESSOR STARTED")
        data, labels = Preprocessor.preprocess(dataset_type=DATASET, model_type=MODEL, signal_type=DOMAIN, window_length=WINDOW)
