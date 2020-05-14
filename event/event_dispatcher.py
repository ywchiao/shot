
from collections import deque

from .event import Event

from logcat import LogCat

class EventDispatcher:
    @LogCat.log_func
    def __init__(self):
        self._event_queue = deque()
        self._event_handler = {}

    @LogCat.log_func
    def add_listener(self, event_type, listener):
        self.on(event_type, listener)

    @LogCat.log_func
    def dispatch_event(self):
        events = list(self._event_queue)
        self._event_queue.clear()

        for e in events:
            if e.type in self._event_handler:
                for handler in self._event_handler[e.type]:
                    handler(e.target, **e.kwargs)
    #                listener.on_event(e, **e.kwargs)
            else:
                pass

    @LogCat.log_func
    def fire_event(self, event_type, target, **kwargs):
        self._event_queue.append(Event(event_type, target, **kwargs))

    @LogCat.log_func
    def on(self, event_type, listener):
        if not event_type in self._event_handler:
            self._event_handler[event_type] = []

        self._event_handler[event_type].append(listener)

# event_dispatcher.py
