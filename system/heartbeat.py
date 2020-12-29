
from component import status

from .system import System

from logcat import LogCat

class Heartbeat(System):
    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on("cmd_heartbeat", self._heartbeat)

    @LogCat.log_func
    def _heartbeat(self, e, ticks, fps):
        status.set_fps(fps)

# heartbeat.py
