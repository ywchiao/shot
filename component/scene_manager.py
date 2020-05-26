
from util import Node
from util import Table

from logcat import LogCat

class SceneManager(Table):
    @LogCat.log_func
    def __init__(self):
        super().__init__(Node)

    def get_scene(self, entity):
        return self.get_value(entity)

# scene_manager.py
