import base64
from PyQt5.QtWidgets import QWidget
from dm.dm_reg import DmReg
import time
import ctypes
from PIL import Image
from io import BytesIO

class Damo():
    __reg_res = {
        "-1": '網路連線錯誤',
        "-2": '未取得管理員權限',
        "0": "未知錯誤",
        "1": "啟動成功",
        "2":"餘額不足",
        "3":"餘額不足",
        "4":"註冊碼錯誤",
        "5":"無法使用",
        "6":"錯誤使用",
        "7":"帳號失效",
        "8":"餘額不足",
    }
    __WINDOW_NAME = 'MapleStory'
    __BING_WINDOW_DELAY = 5
    __CHANNELS = 4

    def __init__(self, log_hook=None) -> None:
        reg = DmReg()
        dm = reg.get_damo()
        self.log_hook = log_hook
        if dm:
            self.dm = dm
        else:
            # reg.reg('registeDM.bat')
            return self.__log('找不到大漠，請綁定後再使用')
        reg_code = dm.Reg('xf30557fc317f617eead33dfc8de3bdd4ab9043', 'xf6o76eua5fu700')
        self.minimap_start_x = 0
        self.minimap_start_y = 0
        self.minimap_end_x = 800
        self.minimap_end_y = 600

        if reg_code != 1: return self.__log(self.__reg_res[str(reg_code)])            
        self.__log('啟動成功')

    def bind_window(self) -> None:
        hwnd = self.dm.FindWindow('', self.__WINDOW_NAME)
        if hwnd:
            self.dm.SetWindowState(hwnd, 1) # bind with public mode: dx.public.active.message
            bind_code = self.dm.BindWindowEx(hwnd, 'dx', 'normal', 'dx', 'dx.public.active.api|dx.public.active.message', 0)
            if not bind_code :
                return self.__log('綁定失敗')
            time.sleep(self.__BING_WINDOW_DELAY)
            # self.dm.EnableKeypadSync(1, 200)
            # self.dm.SetKeypadDelay()
            self.dm.EnableRealKeypad(1)
        else:
            return self.__log('找不到目標程式')

    def screen_shot(self) -> str:
        width = self.minimap_end_x - self.minimap_start_x
        height = self.minimap_end_y - self.minimap_start_y
        address = self.dm.GetScreenData(self.minimap_start_x, self.minimap_start_y, self.minimap_end_x, self.minimap_end_y)
        dm_buffer = ctypes.string_at(address, width * height * self.__CHANNELS)
        img = Image.frombytes('RGBA', (width, height), dm_buffer)
        buffered = BytesIO()
        img = img.convert('RGB')
        img.save(buffered, format='JPEG')
        return base64.b64encode(buffered.getvalue())
            
    def release(self) -> None:
        self.dm.UnBindWindow()

    def __log(self, log) -> None:
        print(log)
        if self.log_hook:
            self.log_hook('大漠：' + log)

    def KeyPress(self, key): 
        print(f'按下按鍵 {chr(key)}')
        self.dm.KeyPress(key)

    def KeyPressChar(self, key): self.dm.KeyPressChar(key)

    def KeyDown(self, key): self.dm.KeyDown(key)

    def KeyDownChar(self, key): self.dm.KeyDownChar(key)

    def KeyUp(self, key): self.dm.KeyUp(key)

    def KeyUpChar(self, key): self.dm.KeyUpChar(key)

if __name__ == '__main__':
    dm = Damo()
    dm.bind_window()
    dm.screen_shot()
    dm.release()
    