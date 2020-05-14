
class Vector2D:
    def __init__(self, value=(0, 0)):
        self._x, self._y = value

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def value(self):
        return (self._x, self._y)

# vector_2d.py
