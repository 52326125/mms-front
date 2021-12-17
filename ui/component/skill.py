

from PyQt5 import QtCore, QtGui, QtWidgets

class SkillWidget(QtWidgets.QWidget):
    __WIDTH = 40
    __HEIGHT = 40
    def __init__(self, info, parent):
        super().__init__(parent)
        self.__init_widget()
        self.skill = info
        self.skill_level = 0

        pixmap = QtGui.QPixmap(self.skill['icon'])
        pixmap = pixmap.scaled(self.__WIDTH, self.__HEIGHT)
        self.icon.setPixmap(pixmap)

        self.name.setText(self.skill['name'])
        self.level.setText(str(self.skill['level']))

        # self.setLayout(self.Form)

    def set_skill(self, info):
        self.skill = info

        pixmap = QtGui.QPixmap(self.skill['icon'])
        pixmap = pixmap.scaled(self.__WIDTH, self.__HEIGHT)
        self.icon.setPixmap(pixmap)

        self.name.setText(self.skill['name'])
        self.level.setText(str(self.skill['level']))
        pass

    def __add_level(self):
        self.skill_level = self.skill_level + 1
        self.level.setText(str(self.skill_level))

    def __init_widget(self):
        # self.Form = QtWidgets.QWidget()
        self.setObjectName("Form")
        self.resize(400, 52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 52))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.add = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setMaximumSize(QtCore.QSize(16, 16))
        self.add.setBaseSize(QtCore.QSize(16, 16))
        self.add.clicked.connect(self.__add_level)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 1, 2, 1, 1)
        self.name = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 2)
        self.level = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.level.sizePolicy().hasHeightForWidth())
        self.level.setSizePolicy(sizePolicy)
        self.level.setObjectName("level")
        self.gridLayout.addWidget(self.level, 1, 1, 1, 1)
        self.icon = QtWidgets.QLabel(self)
        self.icon.setMaximumSize(QtCore.QSize(40, 40))
        self.icon.setBaseSize(QtCore.QSize(40, 40))
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 0, 0, 2, 1)
        self.__retranslateUi()
    
    def __retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "↑"))
        self.name.setText(_translate("Form", "name"))
        self.level.setText(_translate("Form", "level"))
        self.icon.setText(_translate("Form", "icon"))
