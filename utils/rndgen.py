import random

class RandomNumberGenerator:

    def __init__(self, mn, mx):
        self.mn = mn
        self.mx = mx

    def return_uniform(self):
        return random.uniform(self.mn, self.mx)

    def set_min(self, mn):
        self.mn = mn

    def set_max(self, mx):
        self.mx = mx

