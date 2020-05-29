
from entity import Entity

from event import EventDispatcher

class System:
    _dispatcher = EventDispatcher()

    def __init__(self):
        self._entity = Entity.next()

    def on(self, event, handler):
        self._dispatcher.on(event, handler)

    def emit(self, event_type, target, **kwargs):
        self._dispatcher.emit(event_type, target, **kwargs)

    @property
    def entity(self):
        return self._entity

# system.py
