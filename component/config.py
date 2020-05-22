
from pathlib import Path

import json
import logging
import logging.config

from logcat import LogCat

class Config:
    def __init__(self):
        config_path = Path(f"./shot.json")

        if config_path.is_file():
            with config_path.open() as fin:
                 self._cache = json.load(fin)
        else:
            self._cache = {
                "name": "Shot!",
                "window": {
                    "width": 1280,
                    "height": 1024,
                },
                "path": {
                    "data": "./data",
                    "log": "./log"
                },
                "log": {
                    "config": "config.json",
                    "file": "shot.log"
                }
            }

            self._config_logger()

    def _config_logger(self):
        path = Path(
            f"{self._cache['path']['log']}/"
            f"{self._cache['log']['config']}"
        )

        if path.is_file():
            with path.open() as fin:
                config = json.load(fin)

            logging.config.dictConfig(config)
        else:
            logging.basicConfig(
                filename=CONFIG.LOG_FILE,
                filemode="a",
                format="[%(asctime)s:%(msecs)d] [%(name)s] [%(levelname)s] %(module)s.%(funcName)s():%(lineno)d > %(message)s",
                datefmt="%H:%M:%S",
                level=logging.DEBUG
            )

        LogCat.log(f"Logger {LogCat.__name__} configured.")

    @property
    def name(self) -> str:
        return self._cache["name"]

    @property
    def height(self):
        return self._cache["window"]["height"]

    @property
    def width(self):
        return self._cache["window"]["width"]

# config.py
