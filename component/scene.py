
from util import Node

class Scene:
    def __init__(self):
        self._root = Node()

    def add_object(self, obj):
        self._root.add_child(obj)

    @property
    def root(self):
        return self._root

    @property
    def get_mobs(self):
        return self._root.children

# scene.py
