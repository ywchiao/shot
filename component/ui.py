
from util import Node

class UI:
    def __init__(self):
        self._root = Node()

    def add_widget(self, obj):
        self._root.add_child(obj)

    @property
    def root(self):
        return self._root

# ui.py
