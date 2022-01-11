import os
from subprocess import Popen
from win32com.client import CDispatch, Dispatch

class DmReg():
    def __init__(self) -> None:
        pass

    def reg(self, path=None):
        if path is not None:
            sub = Popen(path)
        else:
            path = os.path.join(os.getcwd(), 'dm/registeDm.bat')
            print(path)
            sub = Popen(path)
        sub.communicate()
    
    def get_damo(self) -> CDispatch:
        try:
            dm = Dispatch('dm.dmsoft')
            print(type(dm))
            print('get damo sucess')
            return dm
        except:
            print('get damo fail')
            return None


if __name__ == '__main__':
    reg = DmReg()
    reg.reg('registeDM.bat')