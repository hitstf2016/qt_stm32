import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import MainWindow

class MyMainWindow(QMainWindow, MainWindow):
        def __init__(self, parent=None):
            super(MyMainWindow, self).__init__(parent)
            self.setupUi(self)
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        w = MyMainWindow()
        w.show()
        sys.exit(app.exec_())
