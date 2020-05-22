
from uuid import uuid4

class Entity:
    def __init__(self):
        self._entity = uuid4().hex

    @staticmethod
    def next():
        return uuid4().hex

    @property
    def entity(self):
        return self._entity

# entity.py
