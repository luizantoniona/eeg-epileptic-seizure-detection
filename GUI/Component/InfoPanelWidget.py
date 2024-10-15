from PyQt5.QtCore import Q_ARG
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class InfoPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.info_panel = QTextEdit()
        self.info_panel.setReadOnly(True)

        self.author_label = QLabel('<a href="https://github.com/luizantoniona">Author: Luiz Antonio Nicolau Anghinoni</a>')
        self.author_label.setOpenExternalLinks(True)

        self.custom_layout = QVBoxLayout()
        self.custom_layout.addWidget(self.info_panel)
        self.custom_layout.addWidget(self.author_label)
        self.setLayout(self.custom_layout)

    def write(self, message):
        QMetaObject.invokeMethod(self.info_panel, "insertPlainText", Qt.ConnectionType.AutoConnection, Q_ARG(str, message))

    def clear(self):
        self.info_panel.clear()

    def flush(self):
        pass
