# -*- coding: UTF-8 -*-
import win32com
import win32com.client
from pynput.keyboard import Key, Controller

class MSKeyboardHelper:
    """
    Class responsible for sending keyboard signal to active
    win32 window
    """
    def __init__(self):
        self.shell = win32com.client.Dispatch("WScript.Shell")

        # initialize keyboard controller
        self.keyboard = Controller()

    def sendKey(self, key):
        self.shell.SendKeys(key)

    def activate(self):
        self.shell.AppActivate(u"冒险岛2 - 尬萌不限号")

    def pressKey(self, key):
        self.keyboard.press(key)

    def releaseKey(self, key):
        self.keyboard.release(key)

