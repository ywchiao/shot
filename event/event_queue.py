
from collections import deque

from .event import Event

from logcat import LogCat

class EventQueue:
    @LogCat.log_func
    def __init__(self):
        self._cache = deque()

    @LogCat.log_func
    def append(self, event):
        self._cache.append(event)

    @LogCat.log_func
    def get_events(self):
        events = tuple(self._cache)
        self._cache.clear()

        return events

# event_queue.py
