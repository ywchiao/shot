
import json

from pathlib import Path

from logcat import LogCat

class LayoutManager:
    @LogCat.log_func
    def __init__(self):
        self._cache = {}

    @LogCat.log_func
    def get_layout(self, entity, prefix="."):
        if not entity in self._cache:
            layout = Path(f"{prefix}/{entity}.json")

            with layout.open() as fin:
                self._cache[entity] = json.load(fin)

        return self._cache[entity]

# layout_manager.py
