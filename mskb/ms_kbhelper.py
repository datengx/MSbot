import win32com
import win32com.client

class MSKeyboardHelper:
    def __init__(self):
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def sendKey(self, key):
        self.shell.SendKeys(key)