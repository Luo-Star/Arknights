import win32com.client
import win32gui
import win32api
import win32con
import win32ui
from PIL import Image
hwnd_title = dict()


"""
    根据窗口句柄截取窗口视图
:param hwnd: 窗口句柄 一个整数
"""


def win_shot():
    hwnd = win32gui.FindWindow(None, "MuMu模拟器")
    bmpFileName = str(hwnd) + ".bmp"
    r = win32gui.GetWindowRect(hwnd)
    w = r[2] - r[0]
    h = r[3] - r[1]
    hwindc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, w, h)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (w, h), srcdc,
                 (0, 0), win32con.SRCCOPY)
    bmp.SaveBitmapFile(memdc, bmpFileName)


if __name__ == '__main__':
    win_shot()

import pytesseract
from PIL import Image
text = pytesseract.image_to_string(Image.open('2691716.bmp'),lang='chi_sim')  # chi_sim是简体中文训练包，如果想识别英文去掉lang选项即可
print(text)