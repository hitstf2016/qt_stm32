import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.connect_Button_clicked)
        self.list_ports()

    def connect_Button_clicked(self):
        serial_usb = serial.Serial(
            baudrate=115200,
            parity=serial.PARITY_NONE,
            bytesize=serial.EIGHTBITS,
            stopbits=serial.STOPBITS_ONE,
            timeout=1000,
            write_timeout=1000
        )
        serial_usb.open()


    def list_ports(self):
        port_list = list(serial.tools.list_ports.comports())
        port_list_0 = list(port_list[0])
        port_serial = port_list_0
        for port_name in port_serial:
            self.comboBox.addItem(port_name)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())

