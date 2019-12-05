import sys
import threading
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    class myThread(threading.Thread):
        def __init__(self,func,threadID,name):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name

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

    def scan_Button_clicked(self,serial_usb,myThread,scan_board):
        if serial_usb.is_open:
            thread1 = myThread(scan_board,1,"Thread-1")
            thread1.start()

    def list_ports(self):
        port_list = list(serial.tools.list_ports.comports())
        port_list_0 = list(port_list[0])
        port_serial = port_list_0
        for port_name in port_serial:
            self.comboBox.addItem(port_name)

    def scan_board(self,serial_usb,thread1):
        serial_usb.write("acc_info")
        thread1.

if __name__== "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())

