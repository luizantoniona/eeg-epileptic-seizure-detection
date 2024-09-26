from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class NeuralNetworkWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.network : str = ""
        self.label = QLabel("Network Type:")

        verticalLine = QVBoxLayout()
        verticalLine.addWidget(self.label)

        horizontalLine = QHBoxLayout()

        self.radioRNN = QRadioButton("RNN", self)
        self.radioCNN = QRadioButton("CNN", self)
        self.radioCRNN = QRadioButton("CRNN", self)

        self.radioRNN.toggled.connect(self.on_selected)
        self.radioCNN.toggled.connect(self.on_selected)
        self.radioCRNN.toggled.connect(self.on_selected)

        horizontalLine.addWidget(self.radioRNN)
        horizontalLine.addWidget(self.radioCNN)
        horizontalLine.addWidget(self.radioCRNN)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        verticalLine.addLayout(horizontalLine)
        verticalLine.addWidget(line)
        self.setLayout(verticalLine)

    def on_selected(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.network = selected_button.text()