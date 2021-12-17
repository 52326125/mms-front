from PyQt5 import QtWidgets, QtGui, QtCore
from ui.main import MainWindow

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())