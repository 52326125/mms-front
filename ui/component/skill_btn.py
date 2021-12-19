from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton
from PIL import Image, ImageFont, ImageDraw


class SkillButton(QPushButton):
    __WIDTH = 32
    __HEIGHT = 32
    singnal_log = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.skill_hook = None
        self.key_hook = None
        self.skill_icon = None
        self.key_icon = None
        self.setupUi()

    def setupUi(self):
        self.setMinimumSize(QtCore.QSize(40, 40))
        self.setMaximumSize(QtCore.QSize(40, 40))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setText("")

    def set_skill_hook(self, skill):
        self.skill_hook = skill
        img = Image.open(skill['icon'])
        img.resize((self.__WIDTH, self.__HEIGHT))
        self.skill_icon = img
        self.build_icon('skill_icon')
        self.singnal_log.emit('綁定技能：{}'.format(skill['name']))

    def set_key_hook(self, key):
        self.key_hook = key
        border = Image.new('RGB', (16, 16), (0, 0, 0))
        img = Image.new('RGB', (14, 14), (255, 255, 255))
        dr = ImageDraw.Draw(img)
        font = ImageFont.truetype('./font/Consolas.ttf', 14)
        dr.text((3, 0), chr(key), font=font, fill="#000000")
        border.paste(img, (1, 1))
        self.key_icon = border
        self.build_icon('key_icon')
        self.singnal_log.emit('綁定按鍵：{}'.format(chr(key)))

    def build_icon(self, source):
        icon = getattr(self, source)
        if getattr(self, self.__another(source)) is not None:
            icon = self.skill_icon
            icon.paste(self.key_icon, 
                        (self.skill_icon.width - self.key_icon.width, 
                        self.skill_icon.height - self.key_icon.height))
        pixmap = icon.toqpixmap()
        icon = QIcon(pixmap)
        self.setIcon(icon)
        self.setIconSize(pixmap.rect().size())
        
    def __another(self, name:str) -> str:
        if name == 'key_icon': return 'skill_icon'
        if name == 'skill_icon': return 'key_icon'
            
        
        