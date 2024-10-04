import Database.DatabaseConfiguration as DatabaseConfiguration
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

class DatabaseWidget(QWidget):
    currentIndexChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.checked: bool = False
        self.domain : str = ""
        self.label = QLabel("Database:")

        self.configure_button = QPushButton("Configure")
        self.configure_button.setEnabled(False)
        self.configure_button.clicked.connect(self.on_clicked)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.custom_layout = QVBoxLayout()
        self.custom_layout.addWidget(self.separator)
        self.custom_layout.addWidget(self.label)
        self.custom_layout.addWidget(self.configure_button)
        self.setLayout(self.custom_layout)

        self.check_is_configured()

    def get_checked(self):
        return self.checked

    def on_clicked(self):
        DatabaseConfiguration.configure()
        self.check_is_configured()

    def check_is_configured(self):
        self.configure_button.setEnabled(not DatabaseConfiguration.is_configured())
        self.checked = DatabaseConfiguration.is_configured()
