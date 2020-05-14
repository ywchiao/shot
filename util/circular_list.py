
class CircularList:
    def __init__(self, items=[]):
        self._cache = tuple(items)

        self._length = len(self._cache)
        self._idx = self._length - 1

    @property
    def length(self):
        return self._length

    @property
    def next(self):
        if self._length:
            self._idx = (self._idx + 1) % self._length

            item = self._cache[self._idx]
        else:
            item = None

        return item

    @property
    def items(self):
        return self._cache

# circular_list.py
