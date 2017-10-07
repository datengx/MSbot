# -*- coding: UTF-8 -*-
from mskb.ms_kbhelper import MSKeyboardHelper
from mswin.ms_winmngr import MSWindowManager
from utils.rndgen import RandomNumberGenerator
from utils.timer import Timer
import win32ui
import win32con
import win32api
from pykeyboard import PyKeyboard

# Find the desired window to send signal to
ms_winmngr = MSWindowManager(u"冒险岛2 - 尬萌不限号")
ms_winmngr.find_win()
ms_winmngr.set_foreground()

# Sending keyboard signal
ms_kbobj = MSKeyboardHelper()
# ms_kbobj.sendKey("{DOWN}")


rnd_gen = RandomNumberGenerator(0, 3)
tmr = Timer(2)

num_round = 20

k = PyKeyboard()
x = 810
y = 950

while num_round > 0:
    offset = rnd_gen.return_uniform()
    tmr.set_elapes(2 + offset)

    #ms_kbobj.activate()
    #k.tap_key('x')
    tmr.sleep()

    # simulating mouse event
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(x), y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(x), y, 0, 0)

    tmr.set_elapes(0.1)
    tmr.sleep()

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(x), y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(x), y, 0, 0)


    # ms_kbobj.sendKey("x")
    #pwin = win32ui.FindWindow(None,u"冒险岛2 - 尬萌不限号")
    #pwin.SendMessage(win32con.WM_KEYDOWN,68)

    num_round = num_round - 1
    print("Finish round " + str(num_round))