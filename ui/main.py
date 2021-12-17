from ui.main_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import json
from .component.skill import SkillWidget

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.skill_widgets = {}
        self.buid_skill_book()

    def buid_skill_book(self):
        TAB_PREFIX = 'tab_skill_'
        FORM_PREFIX = 'formLayout_skill_'
        skills_str = open('./skill.json', 'r', encoding='utf-8').read()
        skills = json.loads(skills_str)
        for key in skills.keys(): 
            self.skill_widgets[key] = []
            for skill in skills[key]:
                print(skill)
                sw = SkillWidget(skill, self)
                self.skill_widgets[key].append(sw)
                self.ui.formLayout_skill_1.addRow(sw)
                # self.ui[FORM_PREFIX + key].addLayout(sw)
