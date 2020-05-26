
from .element import Element

class Node(Element):
    def __init__(self):
        super().__init__()

        self._cache = []

        self._value = None

    def add_child(self, node):
        self._cache.append(node)

    def remove_child(self, node):
        self._cache.remove(node)

    @property
    def children(self, node):
        return tuple(self._cache)

# node.py
