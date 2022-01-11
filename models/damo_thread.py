import json
import math
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from dm.damo import Damo
from utils.getSize import GetSize, get_img_str
import time
import random

class Damo_thread(QtCore.QObject):
    signal_log = QtCore.pyqtSignal(str)
    signal_pixmap = QtCore.pyqtSignal()
    signal_get_detect = QtCore.pyqtSignal(bytes)
    __MAP_SCALE = .0625
    __ONLY_SPACE = 0
    __ABLE_SPACE = 1
    __DISABLE_SPACE = 2
    __DIVIATION_Y = 100
    __TICK = .25
    JUMP_KEY = 'x'
    def __init__(self):
        super().__init__()
        self.dm = None
        self.__sent_log('線程啟動成功')
        self.is_running = False
        self.character_position = (0, 0)
        self.atk = None
        self.move = []
        self.sups = []
        self.map = None
        self.platform_now = None
        self.platform_next = None
        self.diraction = 1
        self.diraction_text = ['', 'right', 'left']

    def set_damo(self):
        self.dm = Damo(self.__sent_log)
        self.dm.bind_window()
        self.is_running = True
        
    def __sent_log(self, log):
        self.signal_log.emit('大漠執行線程： ' + log)

    def get_map(self, map1):
        if self.dm:
            self.dm.minimap_start_x = 0
            self.dm.minimap_start_y = 0
            self.dm.minimap_end_x = 800
            self.dm.minimap_end_y = 600
            img_b64 = self.dm.screen_shot()
            self.__sent_log('啟動小地圖選擇器')
            get_size = GetSize(self.get_map_xy)
            get_size.show_img(img_b64)
            self.map = map1
            
    
    def get_map_xy(self, x1, y1, x2, y2):
        print('get xy')
        self.dm.minimap_start_x = x1
        self.dm.minimap_start_y = y1
        self.dm.minimap_end_x = x2
        self.dm.minimap_end_y = y2
        self.signal_pixmap.emit()
        self.signal_log.emit(f'截取小地圖完成，坐標：{x1}, {y1}, {x2}, {y2}')

    def set_character_position(self, x, y, first=False):
        x = x / self.__MAP_SCALE
        y = y / self.__MAP_SCALE
        self.character_position = (int(x), int(y))
        print(self.character_position)
        for platform in self.map['platform']:
            if platform['start_x'] <= x and platform['end_x'] >= x and abs(y - platform['start_y']) <= self.__DIVIATION_Y and self.platform_next == None:
                self.platform_now = platform
                print(f'set platform now {self.platform_now["start_x"]} {self.platform_now["start_y"]}')
                break
        if first:
            p = math.ceil(self.map['size']['x'] / 2)
            self.diraction_judge(p)
            # self.next()

    def __key_press(self, key):
        if type(key) == str:
            self.dm.KeyPressChar(key)
        else:
            self.dm.KeyPress(key)

    def __key_down(self, key):
        if type(key) == str:
            self.dm.KeyDownChar(key)
        else:
            self.dm.KeyDown(key)

    def __key_up(self, key):
        if type(key) == str:
            self.dm.KeyUpChar(key)   
        else:
            self.dm.KeyUp(key)

    def key_press_handle(self, skill):
        is_cold = time.time() - skill['last_press']
        if is_cold > skill['cd_count']:
            delay = max(round(random.random() / 10, 2), skill['delay'] / 1000)
            if skill['space'] == self.__ONLY_SPACE: self.__jump()
            self.__key_press(skill['key'])
            skill['last_press'] = time.time()
            time.sleep(delay)

    def __change_diraction(self): self.__key_press(self.diraction_text[self.diraction])

    def __jump(self): self.__key_press(self.JUMP_KEY) 

    def __jump_forward(self):
        delay = round(random.random() / 10, 2)
        self.__key_down(self.diraction_text[self.diraction])
        self.__key_press(self.JUMP_KEY) 
        time.sleep(delay)
        self.__key_up(self.diraction_text[self.diraction])

    def __jump_down(self):
        delay = round(random.random() / 10, 2)
        self.__key_down('down')
        self.__key_press(self.JUMP_KEY) 
        time.sleep(delay)
        self.__key_up('down')

    def bind_skills(self, skills):
        for skill in skills:
            if skill['type'] == 'atk':
                self.atk = skill
            elif skill['type'] == 'move':
                self.move.append(skill)
            else:
                self.sups.append(skill)

    def release(self): 
        if self.dm:
            self.dm.release()

    def __calculate_steps(self, num1, num2, n:int, range):
        p = self.character_position[n]
        temp = min(abs(num1 - p), abs(num2 - p))
        return math.ceil(temp / abs(range))

    def __next_platform(self, move_x_range, move_y_range):
        result = None
        target = (200, 200)
        for platform in self.map['platform']:
            if self.platform_now != platform and platform['hasMob']:
                steps = (self.__calculate_steps(platform['start_x'], platform['end_x'], 0, move_x_range), self.__calculate_steps(platform['start_y'], platform['end_y'], 1, move_y_range))
                print(f'steps: {target} {platform["start_x"]} {platform["start_y"]}')
                if steps < target: 
                    result = platform
                    target = steps
        return result
        
    def sent_minimap(self):
        img_b64 = self.dm.screen_shot()
        img = get_img_str(img_b64)
        self.signal_get_detect.emit(img)

    def diraction_judge(self, p):
        if self.character_position[0] > p:
            self.diraction = -1
        else:
            self.diraction = 1
        self.__change_diraction()

    def next(self):
        temp = list(map(lambda e: {
            'y': e['start_y'] - self.character_position[1],
            'start_x': e['start_x'],
            'end_x': e['end_x']
        } if (e['start_y'] - self.character_position[1]) >= 0 else {
            'y': 999,
            'start_x': e['start_x'],
            'end_x': e['end_x']
        }, self.map['platform']))
        y = min(temp, key=lambda e: e['y'])
        print(y)
        if y['y'] >= self.__DIVIATION_Y:
            time.sleep(self.__TICK)
            print(f"空中判定 {self.platform_now['start_y']} {self.character_position[1]}")
            return self.sent_minimap()
        move_x_range = 0
        move_x = None
        move_y_range = 0
        move_y = None
        type = 0
        for skill in self.move:
            if skill['diraction'] == 'x':
                if skill['range'] > move_x_range:
                    move_x_range = skill['range']
                    move_x = skill
            else:
                if skill['range'] > move_y_range:
                    move_y_range = skill['range']
                    move_y = skill
        move_x_range = move_x_range * self.diraction
        move_y_range = move_y_range * self.diraction
        jump = 150 * self.diraction
        print(f'顯示條件： {self.character_position[0]} {move_x_range} {jump} {self.platform_now["start_x"]} {self.platform_now["end_x"]}')
        if int(self.character_position[0] + move_x_range) in range(self.platform_now['start_x'], self.platform_now['end_x']) and not self.platform_next:
            type = 1
            print('normal move')
            # 123
            self.key_press_handle(move_x)
        elif int(self.character_position[0] + jump) in range(self.platform_now['start_x'], self.platform_now['end_x']) and not self.platform_next:
            type = 2
            print('jump')
            self.__jump_forward()
        else:
            type = 3
            print('next platform')
            if not self.platform_next:
                self.platform_next = self.__next_platform(move_x_range, move_y_range)
                print(f'下一個平台： {self.platform_next["start_x"]} {self.platform_next["start_y"]}')
            else:
                self.diraction_judge(self.platform_next['start_x'])
                if self.character_position[0] not in range(self.platform_next['start_x'], self.platform_next['end_x']):
                    # 123
                    self.key_press_handle(move_x)
                elif abs(self.character_position[1] - self.platform_next['start_y']) > self.__DIVIATION_Y:
                    if self.character_position[1] <= (self.platform_next['start_y'] + self.__DIVIATION_Y):
                        self.__jump_down()
                    else:
                        # 123
                        self.key_press_handle(move_y)
                else:                    
                    self.platform_now = self.platform_next
                    self.platform_next = None
                    mid = math.ceil((self.platform_now['start_x'] + self.platform_now['end_x']) / 2)
                    self.diraction_judge(mid)
                # for y in range(steps[1]):
                #     for x in range(steps[0]):
                #         self.key_press_handle(move_x)
                #     self.key_press_handle(move_y)
                # self.platform_now = platform
        if type != 3: self.key_press_handle(self.atk)
        # if time.time() - self.move_tick < self.tick:
        #     time.sleep(1 - (time.time() - self.move_tick))
        #     self.move_tick = 0
        print('------')
        self.sent_minimap()

    def test(self, key):
        self.dm.dm.KeyPress(70)