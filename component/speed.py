
class Speed:
    def __init__(self):
        self._cache = {}

    def get_value(self, entity):
        value = 0

        if entity in self._cache:
            value = self._cache[entity]

        return value

    def update(self, entity, value):
        self._cache[entity] = value

# speed.py
