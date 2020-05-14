
import json

from pathlib import Path

class Config:
    def __init__(self):
        path = Path(f"./shot.json")

        if path.is_file():
            with path.open() as fin:
                 self._data = json.load(fin)
        else:
            self._data = {
                "path": {
                    "data": "./data",
                    "log": "./log"
                },
                "log": {
                    "config": "config.json",
                    "file": "shot.log"
                }
            }

    @property
    def LOG_CONFIG(self) -> str:
        return (
            f"{self._data['path']['log']}/"
            f"{self._data['log']['config']}"
        )

    @property
    def LOG_FILE(self) -> str:
        return (
            f"{self._data['path']['log']}/"
            f"{self._data['log']['file']}"
        )

# config.py
