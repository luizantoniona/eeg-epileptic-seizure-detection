from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class DomainWidget(QWidget):
    currentIndexChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.checked: bool = False
        self.domain: str = ""
        self.label = QLabel("Domain Type:")

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.combo_box = QComboBox()
        self.combo_box.currentIndexChanged.connect(self.on_selected)
        self.combo_box.addItems(
            [
                "Select Domain",
                "Time",
                "PSDWelch",
                "PSDMultitaper",
                "Spectrogram",
            ]
        )

        self.custom_layout = QVBoxLayout()
        self.custom_layout.addWidget(self.separator)
        self.custom_layout.addWidget(self.label)
        self.custom_layout.addWidget(self.combo_box)
        self.setLayout(self.custom_layout)

    def get_checked(self):
        return self.checked

    def on_selected(self):
        if self.combo_box.currentIndex() > 0:
            self.checked = True
            self.domain = self.combo_box.currentText()

        else:
            self.checked = False

        self.currentIndexChanged.emit()
