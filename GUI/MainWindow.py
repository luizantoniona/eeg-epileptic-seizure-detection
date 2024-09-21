from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from GUI.Component.DomainBox import DomainBox
from GUI.Component.NetworkBox import NetworkBox
from GUI.Component.WindowSizeBox import WindowSizeBox

TITLE = "EEG Aplication"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(TITLE)
        self.setGeometry(100, 100, 500, 500)

        mainLayout = QHBoxLayout()
        
        trainLayout = QVBoxLayout()
        testLayout = QVBoxLayout()
        

        networkWidget = NetworkBox()
        domainWidget = DomainBox()
        windowWidget = WindowSizeBox()

        trainLayout.addWidget(networkWidget)
        trainLayout.addWidget(domainWidget)
        trainLayout.addWidget(windowWidget)

        mainLayout.addLayout(testLayout)
        mainLayout.addLayout(trainLayout)

        self.setLayout(mainLayout)