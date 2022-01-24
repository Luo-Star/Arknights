import win32com.client
import win32gui
import win32api
import win32con
import win32ui
import pytesseract
from PIL import Image


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