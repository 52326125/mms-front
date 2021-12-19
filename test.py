import win32gui
import autoit
import win32api
import win32con
import time

result = None
time.sleep(2)
def getWindow(hwnd, ctx):
  global result
  if win32gui.GetWindowText(hwnd) == 'MapleStory':
    result = hwnd

win32gui.EnumWindows(getWindow, None)

print(result)
t = win32api.PostMessage(result, win32con.WM_CHAR, 0x44, 0)
print(t)