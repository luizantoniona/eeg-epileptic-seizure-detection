from PyQt5.QtCore import Q_ARG
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class InfoPanelWidget(QWidget):
    def __init__(self, max_lines=100):
        super().__init__()
        self.max_lines = max_lines
        self.current_lines = 0
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
        QMetaObject.invokeMethod(self, "move_cursor_to_end", Qt.ConnectionType.AutoConnection)
        QMetaObject.invokeMethod(self, "check_line_count", Qt.ConnectionType.AutoConnection)

    @pyqtSlot()
    def move_cursor_to_end(self):
        self.info_panel.moveCursor(QTextCursor.End)

    @pyqtSlot()
    def check_line_count(self):
        self.current_lines = self.current_lines + 1
        if self.current_lines > self.max_lines:
            self.clear()
            self.current_lines = 0

    def clear(self):
        self.info_panel.clear()

    def flush(self):
        pass
