from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QMouseEvent, QPixmap
from ui.main_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import json
from .component.skill import SkillWidget
from .component.error_handler import Error_handler
from .component.skill_btn import SkillButton

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.error_handler = Error_handler()
        with open('./job.json', 'r', encoding='utf-8') as jobs:
            jobs = json.load(jobs)
            for job in jobs:
                self.ui.comboBox_job.addItem(job['text'], job['value'])
        self.ui.comboBox_job.setCurrentIndex(-1)
        self.ui.comboBox_job.currentIndexChanged.connect(self.buid_skill_book)
        self.skillButton_atk = SkillButton()
        self.skillButton_move = SkillButton()
        self.ui.horizontalLayout_atk.addWidget(self.skillButton_atk)
        self.ui.horizontalLayout_move.addWidget(self.skillButton_move)
        self.skillButton_atk.clicked.connect(self.click)
        self.skillButton_move.clicked.connect(self.click)
        self.skillButton_atk.singnal_log.connect(self.log)
        self.skillButton_move.singnal_log.connect(self.log)
        self.ui.pushButton_sup_add.clicked.connect(self.add_sup_skill)

        self.skillButton_sups = []
        self.selected_skill = None
        self._log = ''

    def buid_skill_book(self):
        FORM_PREFIX = 'gridLayout_skill_'
        job = self.ui.comboBox_job.currentData()
        with open('./skills/hero.json', 'r', encoding='utf-8') as txt:
            skills = json.loads(txt.read())
        if not job in skills.keys():
            return self.error_handler.warning('warning', '沒有對應的職業技能', '')            
        for key in skills[job].keys(): 
            x = 0
            y = 0
            for skill in skills[job][key]:
                sw = SkillWidget(skill, self)
                sw.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sw.signal_click.connect(self.set_skill)
                exec('self.ui.{}.addWidget(sw, y, x, Qt.AlignmentFlag.AlignTop)'.format(FORM_PREFIX + key))
                x = x + 1
                if x == 2:
                    x = 0
                    y = y +1
            spacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            exec('self.ui.{}.addItem(spacer, y + 1, 0, 1, 2)'.format(FORM_PREFIX + key))

    def set_skill(self, skill:dict):
        self.log(f'已選擇技能：{skill["name"]}')
        self.selected_skill = skill

    def log(self, log:str):
        self._log = log + '\n' + self._log
        self.ui.log.setText(self._log)

    def click(self):
        btn = self.sender()
        if self.selected_skill is not None:
            btn.set_skill_hook(self.selected_skill)
            self.selected_skill = None
        else:
            self.error_handler.signal_key_press.connect(lambda key: btn.set_key_hook(key))
            self.error_handler.question('按鍵綁定', '請輸入綁定按鍵...', '')
            self.error_handler.signal_key_press.disconnect()

    def add_sup_skill(self):
        btn = SkillButton()
        btn.clicked.connect(self.click)
        btn.singnal_log.connect(self.log)
        self.ui.horizontalLayout_sup.addWidget(btn)
        self.log('新增輔助技能欄位')
