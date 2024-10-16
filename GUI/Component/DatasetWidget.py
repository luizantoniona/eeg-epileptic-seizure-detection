import Dataset.DatasetConfigure as DatasetConfigure
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from GUI.Thread.DatasetConfigurationThread import DatasetConfigurationThread
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
        self.configured_label = QLabel("Select Dataset")

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
        self.custom_layout.addWidget(self.configured_label)
        self.custom_layout.addWidget(self.configure_button)
        self.setLayout(self.custom_layout)

    def get_checked(self):
        return self.checked

    def on_selected(self):
        dataset_name = self.combo_box.currentText()

        if self.combo_box.currentIndex() > 0:
            if self.check_dataset_configured(dataset_name):
                self.configured_label.setText("Dataset Configured")
                self.checked = True
                self.dataset = dataset_name

            else:
                self.configured_label.setText("Dataset Not Configured")
                self.checked = False
                self.configure_button.setEnabled(True)

        else:
            self.configured_label.setText("Select Dataset")
            self.checked = False
            self.dataset = ""
            self.configure_button.setEnabled(False)

        self.currentIndexChanged.emit()

    def check_dataset_configured(self, dataset_name: str) -> bool:
        return DatasetConfigure.is_configured(dataset_type=dataset_enum_by_name(dataset_name))

    def configure_dataset(self):
        self.configuration_thread = DatasetConfigurationThread(self.combo_box.currentText())
        self.configuration_thread.finished.connect(self.on_configuration_finished)
        self.configure_button.setEnabled(False)
        self.combo_box.setEnabled(False)
        self.configuration_thread.start()

    def on_configuration_finished(self):
        self.combo_box.setEnabled(True)
        self.check_dataset_configured(self.combo_box.currentText())
