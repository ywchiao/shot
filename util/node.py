
class Node:
    def __init__(self, value=None):
        self._cache = []

        self._value = value

    def add_child(self, node):
        self._cache.append(node)

    def remove_child(self, node):
        self._cache.remove(node)

    @property
    def children(self):
        return tuple(self._cache)

    @property
    def first_child(self):
        if self._cache:
            node = self._cache[0]
        else:
            node = None

        return node

    @property
    def last_child(self):
        if self._cache:
            node = self._cache[-1]
        else:
            node = None

        return node

    @property
    def value(self):
        return self._value

# node.py
