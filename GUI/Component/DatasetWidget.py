import Dataset.DatasetConfigure as DatasetConfigure
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class DatasetWidget(QWidget):
    currentIndexChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.checked: bool = False
        self.dataset: str = ""
        self.label = QLabel("Dataset:")

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.configure_button = QPushButton("Configure")
        self.configure_button.setEnabled(False)
        self.configure_button.clicked.connect(self.configure_dataset)

        self.combo_box = QComboBox()
        self.combo_box.currentIndexChanged.connect(self.on_selected)
        self.combo_box.addItems(
            [
                "Select Dataset",
                "CHBMIT",
            ]
        )

        self.custom_layout = QVBoxLayout()
        self.custom_layout.addWidget(self.separator)
        self.custom_layout.addWidget(self.label)
        self.custom_layout.addWidget(self.combo_box)
        self.custom_layout.addWidget(self.configure_button)
        self.setLayout(self.custom_layout)

    def get_checked(self):
        return self.checked

    def on_selected(self):
        if self.combo_box.currentIndex() > 0 and self.check_dataset_configured(self.combo_box.currentText()):
            self.checked = True
            self.dataset = self.combo_box.currentText()

        else:
            self.checked = False

        self.currentIndexChanged.emit()

    def check_dataset_configured(self, dataset_name):
        DatasetConfigure.configure(dataset_type=dataset_enum_by_name(dataset_name))

    def configure_dataset(self, dataset_name):
        DatasetConfigure.configure(dataset_type=dataset_enum_by_name(dataset_name))
