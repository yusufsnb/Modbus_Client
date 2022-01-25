import window
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
pencere = window.Pencere()
pencere.setWindowTitle("Python Modbus")
pencere.show()
sys.exit(app.exec_())
