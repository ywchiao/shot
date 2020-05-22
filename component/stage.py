
from util import Node

class Stage:
    def __init__(self):
        self._screens = {}

        self._scene = None

    def switch(self, scene):
        self._scene = self._screens[scene]

# stage.py
