
from util import Node

class Scene:
    def __init__(self, desc=None):
        super().__init__()

        self._root = Node()

        if desc:
            for i in range(desc["mob"]):
                self.add_object(Mob())

    def add_object(self, obj):
        self._root.add_child(obj)

    @property
    def root(self):
        return self._root

    @property
    def get_mobs(self):
        return self._root.children

# scene.py
