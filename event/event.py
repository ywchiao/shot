
class Event:
    def __init__(self, event_type, target, source, **kwargs):
        self._type = event_type
        self._target = target
        self._source = source
        self._kwargs = kwargs

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target

    @property
    def type(self):
        return self._type

# event.py
