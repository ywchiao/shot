
from entity import Entity

from event import dispatcher

class System:
    def __init__(self):
        self._entity = Entity.next()

    def on(self, event, handler):
        dispatcher.on(event, handler)

    def emit(self, event_type, target, **kwargs):
        dispatcher.emit(event_type, target, **kwargs)

    @property
    def entity(self):
        return self._entity

# system.py
