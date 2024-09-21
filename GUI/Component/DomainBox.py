from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QWidget

class DomainBox(QWidget):
    def __init__(self):
        super().__init__()
        self.domain : str = ""

        horizontalLine = QHBoxLayout()

        self.radioTime = QRadioButton("time", self)
        self.radioPSD = QRadioButton("PSD", self)
        self.radioSpectrogram = QRadioButton("spectrogram", self)

        self.radioTime.toggled.connect(self.on_selected)
        self.radioPSD.toggled.connect(self.on_selected)
        self.radioSpectrogram.toggled.connect(self.on_selected)

        horizontalLine.addWidget(self.radioTime)
        horizontalLine.addWidget(self.radioPSD)
        horizontalLine.addWidget(self.radioSpectrogram)

        self.setLayout(horizontalLine)

    def on_selected(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.domain = selected_button.text()