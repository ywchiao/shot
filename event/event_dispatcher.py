
from .event import Event
from .event_queue import EventQueue

from logcat import LogCat

class EventDispatcher:
    @LogCat.log_func
    def __init__(self):
        self._queue = EventQueue()

        self._handler = {}

    @LogCat.log_func
    def dispatch(self):
        for e in self._queue.get_events():
            if e.type in self._handler:
                for handler in self._handler[e.type]:
                    handler(e.target, **e.kwargs)
            else:
                pass

    @LogCat.log_func
    def emit(self, event_type, target, **kwargs):
        self._queue.append(Event(event_type, target, **kwargs))

    @LogCat.log_func
    def on(self, event_type, listener):
        if not event_type in self._handler:
            self._handler[event_type] = []

        self._handler[event_type].append(listener)

# event_dispatcher.py
