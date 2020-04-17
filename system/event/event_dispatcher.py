
from collections import deque

from .event import Event

class EventDispatcher:
    def __init__(self):
        self._event_queue = deque()
        self._event_handler = {}

    def add_listener(self, event_type, listener):
        self.on(event_type, listener)

    def dispatch_event(self):
        events = list(self._event_queue)
        self._event_queue.clear()

        for e in events:
            for listener in self._event_handler[e.type]:
                listener.on_event(e, **e.kwargs)

    def fire_event(self, source, event_type, **kwargs):
        self._event_queue.append(Event(source, event_type, **kwargs))

    def on(self, event_type, listener):
        if not event_type in self._event_handler:
            self._event_handler[event_type] = []

        self._event_handler[event_type].append(listener)

# event_dispatcher.py
