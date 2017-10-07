import time

class Timer:
    def __init__(self, elapse):
        self.elapse = elapse

    def sleep(self):
        time.sleep(self.elapse)

    def set_elapes(self, elapse):
        self.elapse = elapse

    def get_elapse(self):
        return self.elapse

