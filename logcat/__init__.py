
from pathlib import Path

import json
import logging
import logging.config

from config import CONFIG

from .logcat import LogCat

config = Path(CONFIG.LOG_CONFIG)

if config.is_file():
    with config.open() as fin:
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

# __init__.py
