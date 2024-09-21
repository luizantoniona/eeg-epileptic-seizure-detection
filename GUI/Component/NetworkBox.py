from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QWidget

class NetworkBox(QWidget):
    def __init__(self):
        super().__init__()
        self.network : str = ""

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

        self.setLayout(horizontalLine)

    def on_selected(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.network = selected_button.text()