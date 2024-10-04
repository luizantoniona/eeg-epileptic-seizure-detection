from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class InfoPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.info_panel = QTextEdit()
        self.info_panel.setReadOnly(True)

        self.custom_layout = QVBoxLayout()
        self.custom_layout.addWidget(self.info_panel)
        self.setLayout(self.custom_layout)

    def write(self, message):
        self.info_panel.insertPlainText(message)

    def clear(self):
        self.info_panel.clear()

    def flush(self):
        pass
