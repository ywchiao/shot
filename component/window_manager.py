
from logcat import LogCat

class WindowManager:
    @LogCat.log_func
    def __init__(self):
        self._cache = {}

    def get_window(self, entity):
        win = None

        if entity in self._cache:
            win = self._cache[entity]

        return win

    def register(self, window):
        self._cache[window.entity] = window

# window_manager.py
