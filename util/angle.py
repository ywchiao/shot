
import math

class Angle:
    def __init__(self, degree=0):
        self._degree = degree % 360

    @property
    def degree(self):
        return self._degree

    @property
    def radian(self):
        return (self._degree / 180) * math.pi

# angle.py
