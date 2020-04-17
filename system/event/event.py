
class Event:
    def __init__(self, source, event_type, **kwargs):
        self._source = source
        self._type = event_type
        self._kwargs = kwargs

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def type(self):
        return self._type

# event.py
