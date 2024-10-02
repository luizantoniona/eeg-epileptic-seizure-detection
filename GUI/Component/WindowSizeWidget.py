from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class WindowSizeWidget(QWidget):
    currentIndexChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.checked: bool = False
        self.window_size : int = 0
        self.label = QLabel("Window Size:")

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.combo_box = QComboBox()
        self.combo_box.currentIndexChanged.connect(self.on_selected)
        self.combo_box.addItems([
            "Select Window Size",
            "1",
            "2",
            "5",
            "10",
        ])

        self.custom_layout = QVBoxLayout()
        self.custom_layout.addWidget(self.separator)
        self.custom_layout.addWidget(self.label)
        self.custom_layout.addWidget(self.combo_box)
        self.setLayout(self.custom_layout)

    def getChecked(self):
        return self.checked

    def on_selected(self):
        if self.combo_box.currentIndex() > 0 :
            self.checked = True
            self.window_size = int(self.combo_box.currentText())

        else:
            self.checked = False

        self.currentIndexChanged.emit()
