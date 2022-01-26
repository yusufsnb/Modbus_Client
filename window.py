from email.charset import QP
from msilib.schema import Error
from operator import mod
from tkinter import E
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPalette
import Ui_modbus
import easymodbus.modbusClient


class Pencere(QMainWindow, Ui_modbus.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnConnect.clicked.connect(self.connectToPLC)
        self.btnRead.clicked.connect(self.readDataFromPLC)
        self.btnWrite.clicked.connect(self.writeDataToPLC)
        self.txtRead.setReadOnly(True)
        self.msg = QMessageBox()
        self.isConnected

    def connectToPLC(self):
        self.ip = self.txtIpv1.text() + '.' + self.txtIpv2.text() + \
            '.' + self.txtIpv3.text() + '.' + self.txtIpv4.text()
        self.port = self.txtPort.text()
        if(self.ip != '' and self.port != ''):
            modbus_client = easymodbus.modbusClient.ModbusClient(
                self.ip, int(self.port))
            self.modbusClient = modbus_client
            try:
                if modbus_client.is_connected():
                    modbus_client.close()
                modbus_client.connect()
                if(modbus_client.is_connected):
                    for i in range(0, 50):
                        self.comRead.addItem(str(i))
                        self.comWrite.addItem(str(i))
            except:
                self.msg.setText("Bir hata oluştu")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.show()
        else:
            self.msg.setText(
                "Lütfen Ip ve Port alanlarını doldurunuz")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()

    def writeDataToPLC(self):
        if(self.modbusClient.is_connected)():
            if self.txtWrite.text() != '':
                self.modbusClient.write_single_register(
                    int(self.comWrite.currentText()), int(self.txtWrite.text()))
            else:
                self.msg.setText("Yazılacak veri alanı boş bırakılamaz!")
                self.msg.setStandardButtons(
                    QMessageBox.Ok)
                self.msg.show()

    def readDataFromPLC(self):
        if(self.modbusClient.is_connected()):
            input_registers = self.modbusClient.read_holdingregisters(
                int(self.comRead.currentText()), 1)
            self.txtRead.setText(str(input_registers[0]))

    def isConnected(self):
        if self.modbusClient.is_connected():
            self.btnConnected.setStyleSheet(
                "background-color: red;border-radius:1px;border-width:1px")
        else:
            self.btnConnected.setStyleSheet(
                "background-color: green;border-radius:1px;border-width:1px")
