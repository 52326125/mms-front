from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget
from ui.component.skill_ui import Ui_Form

class SkillWidget(QWidget):
    __WIDTH = 32
    __HEIGHT = 32
    signal_click = pyqtSignal(dict)
    def __init__(self, info, parent):
        super(SkillWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.skill = info
        exec("self.cd = " + f"{self.skill['cd_count']}")

        pixmap = QtGui.QPixmap(self.skill['icon'])
        pixmap = pixmap.scaled(self.__WIDTH, self.__HEIGHT)
        self.ui.icon.setPixmap(pixmap)

        self.ui.name.setText(self.skill['name'])
        self.ui.level.setText(str(self.skill['level']))
        self.ui.add.clicked.connect(self.__add_level)
        self.ui.icon.mousePressEvent = self.icon_click

    def __add_level(self):        
        self.skill['level'] = self.skill['level'] + 1
        self.ui.level.setText(str(self.skill['level']))
        exec("self.cd = " + self.skill['cd_count'])

    def icon_click(self, event):
        self.signal_click.emit(self.skill)