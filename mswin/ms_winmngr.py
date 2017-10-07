import win32gui


class MSWindowManager:

    def __init__(self, name):
        self.name = name
        self._handle = None
        print("Initializing window manager.")

    def find_win(self):
        try:
            self._handle=win32gui.FindWindow(None, self.name)
        except win32gui.error, e:
            print("Error finding the window " + self.name)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_foreground(self):
        """Put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

    def set_foreground_with_name(self, name):
        self.name = name
        self.find_win()
        win32gui.SetForegroundwindow(self._handle)
