
class Status:
    def __init__(self):
        self._fps = 0

    def set_fps(self, fps):
        self._fps = fps

    @property
    def fps(self):
        return self._fps

# status.py
