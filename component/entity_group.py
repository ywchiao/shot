
class EntityGroup:
    def __init__(self):
        self._cache = set()

    def register(self, entity):
        self._cache.add(entity)

    def remove(self, entity):
        if entity in self._cache:
            self._cache.remove(entity)

    @property
    def entities(self):
        return tuple(self._cache)

# entity_group.py
