
from util import Node

class Scene:
    def __init__(self, title):
        self._title = title

        self._root = Node()

    def add_object(self, obj):
        self._root.add_child(obj)

    @property
    def root(self):
        return self._root

    @property
    def title(self):
        return self._title

# scene.py
