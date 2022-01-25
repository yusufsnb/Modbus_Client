from msilib.schema import Error
from tkinter import E
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import Ui_modbus
import easymodbus.modbusClient


class Pencere(QMainWindow, Ui_modbus.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ip = self.txtIpv1.text() + self.txtIpv2.text() + \
            self.txtIpv3.text() + self.txtIpv4.text()
        self.btnConnect.clicked.connect(self.connectToPLC)
        self.btnRead.clicked.connect(self.readDataFromPLC)
        self.btnWrite.clicked.connect(self.writeDataToPLC)

    def connectToPLC(self):
        print(self.ip)
        modbus_client = easymodbus.modbusClient.ModbusClient(
            '192.168.1.1', 700)
        self.modbusClient = modbus_client
        try:
            if modbus_client.is_connected :
                modbus_client.close()
            modbus_client.connect()
        except Error:
            msg = QMessageBox()
            QMessageBox.setText("Bir hata oluştu", Error.name)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if(modbus_client.is_connected):
            for i in range(0, 50):
                self.comRead.addItem(str(i))
                self.comWrite.addItem(str(i))

    def writeDataToPLC(self):
        if(self.modbusClient.is_connected):
            self.modbusClient.write_single_register(
                int(self.comWrite.currentText()), int(self.txtWrite.text()))

    def readDataFromPLC(self):
        if(self.modbusClient.is_connected):
            input_registers = self.modbusClient.read_holdingregisters(
                int(self.comRead.currentText()), 1)
            self.txtRead.setText(str(input_registers[0]))
