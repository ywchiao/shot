
from util import Node

from entity import Entity

class Scene(Entity):
    def __init__(self):
        super().__init__()

        self._root = Node()

    @property
    def root(self):
        return self._root

    @property
    def children(self):
        return self._root.children

    def add_object(self, obj):
        self._root.add_child(obj)

# scene.py
