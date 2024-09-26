from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import  QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from GUI.Component.DomainWidget import DomainWidget
from GUI.Component.NeuralNetworkWidget import NeuralNetworkWidget
from GUI.Component.WindowSizeWidget import WindowSizeWidget

TITLE = "EEG Aplication"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.setGeometry(100, 100, 500, 500)

        mainLayout = QVBoxLayout()
        
        selectionLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        self.network_widget = NeuralNetworkWidget()
        self.domain_widget = DomainWidget()
        self.window_widget = WindowSizeWidget()

        selectionLayout.addWidget(self.network_widget)
        selectionLayout.addWidget(self.domain_widget)
        selectionLayout.addWidget(self.window_widget)

        self.train_button = QPushButton("Train")
        self.test_button = QPushButton("Test")
        self.evaluate_button = QPushButton("Evaluate")

        self.train_button.clicked.connect(self.train_model)
        self.test_button.clicked.connect(self.test_model)
        self.evaluate_button.clicked.connect(self.evaluate_model)

        buttonLayout.addWidget(self.train_button)
        buttonLayout.addWidget(self.test_button)
        buttonLayout.addWidget(self.evaluate_button)

        mainLayout.addLayout(selectionLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

    def train_model(self):
        print("Training the model...")

    def test_model(self):
        print("Testing the model...")

    def evaluate_model(self):
        print("Evaluating the model...")