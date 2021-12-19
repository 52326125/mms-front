from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMessageBox

class Error_handler(QMessageBox):
    signal_key_press = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    def warning(self, title: str, content: str, info: str):
        icon = self.Icon.Warning
        self.__set_msg(title=title, content=content, info=info, icon=icon)
        self.exec_()

    def question(self, title: str, content: str, info: str):
        icon = self.Icon.Question
        self.__set_msg(title=title, content=content, info=info, icon=icon)
        self.addButton(QMessageBox.Ok)
        self.button(QMessageBox.Ok).hide()
        self.keyPressEvent = self.key_press
        self.exec_()

    def key_press(self, event:QKeyEvent):
        self.signal_key_press.emit(event.key())
        self.accept()


    def __set_msg(self, **kargs):
        if kargs['title']: self.setWindowTitle(kargs['title'])
        if kargs['content']: self.setText(kargs['content'])
        if kargs['icon']: self.setIcon(kargs['icon'])
        if kargs['info']: self.setInformativeText(kargs['info'])
