# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_map = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_map.setObjectName("pushButton_map")
        self.gridLayout.addWidget(self.pushButton_map, 0, 1, 1, 1)
        self.scrollArea_sup = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_sup.setMinimumSize(QtCore.QSize(230, 50))
        self.scrollArea_sup.setMaximumSize(QtCore.QSize(600000, 50))
        self.scrollArea_sup.setWidgetResizable(True)
        self.scrollArea_sup.setObjectName("scrollArea_sup")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 374, 48))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_sup.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea_sup, 5, 0, 1, 1)
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setObjectName("log")
        self.gridLayout.addWidget(self.log, 6, 0, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 7, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_sup = QtWidgets.QLabel(self.centralwidget)
        self.label_sup.setObjectName("label_sup")
        self.horizontalLayout_4.addWidget(self.label_sup)
        self.pushButton_sup_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sup_add.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_sup_add.setObjectName("pushButton_sup_add")
        self.horizontalLayout_4.addWidget(self.pushButton_sup_add)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_movable = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_movable.setObjectName("checkBox_movable")
        self.horizontalLayout_2.addWidget(self.checkBox_movable)
        self.label_move = QtWidgets.QLabel(self.centralwidget)
        self.label_move.setObjectName("label_move")
        self.horizontalLayout_2.addWidget(self.label_move)
        self.pushButton_move = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_move.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_move.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_move.setText("")
        self.pushButton_move.setIconSize(QtCore.QSize(66, 87))
        self.pushButton_move.setObjectName("pushButton_move")
        self.horizontalLayout_2.addWidget(self.pushButton_move)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_atk = QtWidgets.QLabel(self.centralwidget)
        self.label_atk.setObjectName("label_atk")
        self.horizontalLayout_3.addWidget(self.label_atk)
        self.pushButton_atk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_atk.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_atk.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_atk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_atk.setText("")
        self.pushButton_atk.setObjectName("pushButton_atk")
        self.horizontalLayout_3.addWidget(self.pushButton_atk)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_job = QtWidgets.QLabel(self.centralwidget)
        self.label_job.setObjectName("label_job")
        self.horizontalLayout.addWidget(self.label_job)
        self.comboBox_job = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_job.setToolTip("")
        self.comboBox_job.setCurrentText("")
        self.comboBox_job.setObjectName("comboBox_job")
        self.horizontalLayout.addWidget(self.comboBox_job)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 250))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_skill_1 = QtWidgets.QWidget()
        self.tab_skill_1.setObjectName("tab_skill_1")
        self.formLayout_skill_1 = QtWidgets.QFormLayout(self.tab_skill_1)
        self.formLayout_skill_1.setObjectName("formLayout_skill_1")
        self.tabWidget.addTab(self.tab_skill_1, "")
        self.tab_skill_2 = QtWidgets.QWidget()
        self.tab_skill_2.setObjectName("tab_skill_2")
        self.formLayout_skill_2 = QtWidgets.QFormLayout(self.tab_skill_2)
        self.formLayout_skill_2.setObjectName("formLayout_skill_2")
        self.tabWidget.addTab(self.tab_skill_2, "")
        self.tab_skill_3 = QtWidgets.QWidget()
        self.tab_skill_3.setObjectName("tab_skill_3")
        self.formLayout_skill_3 = QtWidgets.QFormLayout(self.tab_skill_3)
        self.formLayout_skill_3.setObjectName("formLayout_skill_3")
        self.tabWidget.addTab(self.tab_skill_3, "")
        self.tab_skill_4 = QtWidgets.QWidget()
        self.tab_skill_4.setObjectName("tab_skill_4")
        self.formLayout_skill_4 = QtWidgets.QFormLayout(self.tab_skill_4)
        self.formLayout_skill_4.setObjectName("formLayout_skill_4")
        self.tabWidget.addTab(self.tab_skill_4, "")
        self.tab_skill_hyper = QtWidgets.QWidget()
        self.tab_skill_hyper.setObjectName("tab_skill_hyper")
        self.formLayout_skill_hyper = QtWidgets.QFormLayout(self.tab_skill_hyper)
        self.formLayout_skill_hyper.setObjectName("formLayout_skill_hyper")
        self.tabWidget.addTab(self.tab_skill_hyper, "")
        self.tab_skill_5 = QtWidgets.QWidget()
        self.tab_skill_5.setObjectName("tab_skill_5")
        self.formLayout_skill_6 = QtWidgets.QFormLayout(self.tab_skill_5)
        self.formLayout_skill_6.setObjectName("formLayout_skill_6")
        self.tabWidget.addTab(self.tab_skill_5, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 1, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MMS"))
        self.pushButton_map.setText(_translate("MainWindow", "載入地圖設定"))
        self.pushButton_start.setText(_translate("MainWindow", "啟動"))
        self.label_sup.setText(_translate("MainWindow", "輔助技能："))
        self.pushButton_sup_add.setText(_translate("MainWindow", "增加技能位"))
        self.checkBox_movable.setText(_translate("MainWindow", "移動中使用"))
        self.label_move.setText(_translate("MainWindow", "移動技能："))
        self.label_atk.setText(_translate("MainWindow", "主攻技能："))
        self.label_job.setText(_translate("MainWindow", "職業："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skill_1), _translate("MainWindow", "Ⅰ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skill_2), _translate("MainWindow", "Ⅱ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skill_3), _translate("MainWindow", "Ⅲ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skill_4), _translate("MainWindow", "Ⅳ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skill_hyper), _translate("MainWindow", "Hyper"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_skill_5), _translate("MainWindow", "Ⅴ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())