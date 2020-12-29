
from collections import deque

from .event import Event

from logcat import LogCat

class EventDispatcher:
    @LogCat.log_func
    def __init__(self):
        self._queue = deque()

        self._handler = {}

    @LogCat.log_func
    def dispatch(self):
        events = tuple(self._queue)
        self._queue.clear()

        for e in events:
            if e.type in self._handler:
                if e.target in self._handler[e.type]:
                    self._handler[e.type][e.target](e, **e.kwargs)
                else:
                    for _, handler in self._handler[e.type].items():
                        handler(e, **e.kwargs)
            else:
                pass

    @LogCat.log_func
    def emit(self, event_type, target, source, **kwargs):
        self._queue.append(Event(event_type, target, source, **kwargs))

    @LogCat.log_func
    def on(self, event_type, entity, listener):
        if not event_type in self._handler:
            self._handler[event_type] = {}

        self._handler[event_type][entity] = listener

# event_dispatcher.py
