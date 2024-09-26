from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class WindowSizeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.window_size : int = 0
        self.label = QLabel("Window Size:")

        verticalLine = QVBoxLayout()
        verticalLine.addWidget(self.label)

        horizontalLine = QHBoxLayout()

        self.radioW1 = QRadioButton("1", self)
        self.radioW2 = QRadioButton("2", self)
        self.radioW5 = QRadioButton("5", self)
        self.radioW10 = QRadioButton("10", self)

        self.radioW1.toggled.connect(self.on_selected)
        self.radioW2.toggled.connect(self.on_selected)
        self.radioW5.toggled.connect(self.on_selected)
        self.radioW10.toggled.connect(self.on_selected)

        horizontalLine.addWidget(self.radioW1)
        horizontalLine.addWidget(self.radioW2)
        horizontalLine.addWidget(self.radioW5)
        horizontalLine.addWidget(self.radioW10)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        verticalLine.addLayout(horizontalLine)
        verticalLine.addWidget(line)
        self.setLayout(verticalLine)

    def on_selected(self):
        selected_button = self.sender()
        if selected_button.isChecked():
            self.window_size = int(selected_button.text())