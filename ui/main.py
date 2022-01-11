import base64
from io import BytesIO
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QIcon, QImage, QMouseEvent, QPixmap
from ui.main_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import json
from .component.skill import SkillWidget
from .component.error_handler import ErrorHandler
from .component.skill_btn import SkillButton
from models.damo_thread import Damo_thread
from models.socket_handler import Socketio_handler
import math
from PIL import Image

class MainWindow(QtWidgets.QMainWindow):
    __MINI_MAP_PATH = './mini_map.jpg'
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._log = ''
        self.error_handler = ErrorHandler()
        self.skills = []

        with open('./job.json', 'r', encoding='utf-8') as jobs:
            self.log('載入技能設定...')
            jobs = json.load(jobs)
            for job in jobs:
                self.ui.comboBox_job.addItem(job['text'], job['value'])
            self.log('載入成功')

        with open('./map/map.json', 'r', encoding='utf-8') as maps:
            self.log('載入地圖...')
            maps = json.load(maps)
            for map in maps:
                self.ui.comboBox_map_select.addItem(map['name'], map['name'])
            self.log('載入成功')

        for i in range(2, 9):
            self.ui.comboBox_atk_sp.addItem(str(i), i)

        self.ui.comboBox_job.setCurrentIndex(-1)
        self.ui.comboBox_map_select.setCurrentIndex(-1)
        self.ui.comboBox_atk_sp.setCurrentIndex(-1)
        self.ui.comboBox_job.currentIndexChanged.connect(self.buid_skill_book)
        self.ui.comboBox_map_select.currentIndexChanged.connect(self.get_map_data)
        self.skillButton_atk = SkillButton()
        self.ui.pushButton_move_add.clicked.connect(self.add_move_skill)
        self.ui.horizontalLayout_atk.addWidget(self.skillButton_atk)        
        self.skillButton_atk.clicked.connect(self.click)
        self.skillButton_atk.singnal_log.connect(self.log)
        self.ui.pushButton_sup_add.clicked.connect(self.add_sup_skill)
        self.ui.pushButton_dm.clicked.connect(self.set_damo)
        self.ui.pushButton_map.clicked.connect(self.get_map)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.dm = Damo_thread()
        self.sub_thread_dm = QThread(self)
        self.sub_thread_socket = QThread(self)
        self.dm.moveToThread(self.sub_thread_dm)
        self.dm.signal_log.connect(self.log)
        self.dm.signal_pixmap.connect(self.get_map_xy)
        self.dm.signal_get_detect.connect(self.sent_minimap)
        self.server_connect()
        self.first = True
        self.running = False

        self.skillButton_sups = []
        self.selected_skill = None

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
        if not btn in self.skills: self.skills.append(btn)
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

    def add_move_skill(self):
        btn = SkillButton()
        btn.clicked.connect(self.click)
        btn.singnal_log.connect(self.log)
        self.ui.horizontalLayout_move.addWidget(btn)
        self.log('新增移動技能欄位')

    def set_damo(self) -> None:
        if self.dm.is_running: self.log('大漠線程已經執行')
        else: 
            self.dm.set_damo()
            self.ui.pushButton_test.clicked.connect(lambda: self.dm.test('f'))

    def get_map(self):
        if not self.ui.comboBox_map_select.currentData():
            return self.error_handler.warning('warning', '尚未選擇地圖', '')
        self.dm.get_map(self.selected_map)

    def get_map_xy(self):
        pixmap = QPixmap(self.__MINI_MAP_PATH)
        self.ui.label_map.setPixmap(pixmap)
        with open(self.__MINI_MAP_PATH, 'rb') as b64:
            self.socket.sent_map(base64.b64encode(b64.read()))

    def sent_minimap(self, img_b64):
        self.socket.sent_map(img_b64)
        img = Image.open(BytesIO(base64.b64decode(img_b64)))
        pixmap = img.toqpixmap()
        self.ui.label_map.setPixmap(pixmap)

    def server_connect(self):
        self.socket = Socketio_handler('http://192.168.0.113:5000')
        self.socket.moveToThread(self.sub_thread_socket)
        self.socket.signal_log.connect(self.log)
        self.socket.signal_detected.connect(self.get_detected)
        self.socket.handler_connect()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.socket.handler_disconnect()
        self.dm.release()
        return super().closeEvent(a0)
        
    def get_detected(self, data):        
        for item in data:
            if item['name'] == 'me':
                self.dm.set_character_position(item['x'], item['y'], self.first)
                self.first = False
        if self.running: self.dm.next()

    def real_delay(self, delay): 
        return math.ceil(delay / 16 * (10 + self.ui.comboBox_atk_sp.currentData()) / 30) * 30

    def start(self):
        if not self.ui.comboBox_atk_sp.currentData():
            return self.error_handler.warning('warning', '未設定攻速', '')
        skills = list(map(lambda skill: {
            "cd_count": skill.skill_hook['cd_count'],
            'delay': self.real_delay(skill.skill_hook['delay']),
            'key': skill.key_hook,
            'type': skill.skill_hook['type'],
            'diraction': skill.skill_hook['diraction'] if 'diraction' in skill.skill_hook else '',
            'range': skill.skill_hook['range'] if 'range' in skill.skill_hook else 0,
            'space': skill.skill_hook['space'],
            'last_press': 0
        } , self.skills))
        self.dm.bind_skills(skills)
        self.running = True
        self.dm.next()

    def get_map_data(self):
        selected_map = self.ui.comboBox_map_select.currentData()
        with open('./map/map.json', 'r', encoding='utf-8') as maps:
            maps = json.load(maps)
            for map in maps:
                if selected_map == map['name']:
                    self.selected_map = map
                    break