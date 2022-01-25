from PyQt5.QtWidgets import QMainWindow
import Ui_modbus

class Pencere(QMainWindow, Ui_modbus.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

