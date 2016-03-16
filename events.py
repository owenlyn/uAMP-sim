from enum import Enum, unique
import abc


@unique
class EventType(Enum):
    UNKNOWN = 0
    # Trace File Events
    APP_START = 1
    SCREEN = 2
    SCREEN_ORIENTATION = 3
    PHONE = 4
    PACKAGE = 5
    NOTIFICATION = 6
    NETWORK = 7
    STORAGE = 8
    HEADSET = 9
    DOCK = 10
    BLUETOOTH = 11
    BATTERY = 12

    # Simulator Events
    PRELOAD_APP = 1000


class Event(metaclass=abc.ABCMeta):
    def __init__(self, event_type, timestamp):
        self.type = event_type
        self.timestamp = timestamp

    def get_type(self):
        return self.type

    def get_timestamp(self):
        return self.timestamp


class AppStartEvent(Event):
    def __init__(self, timestamp, app_id, app_name, source_class):
        Event.__init__(self, event_type=EventType.APP_START, timestamp=timestamp)
        self.app_id = app_id
        self.app_name = app_name
        self.source_class = source_class


class ScreenEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.SCREEN, timestamp=timestamp)
        self.state = state


class ScreenOrientationEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.SCREEN_ORIENTATION, timestamp=timestamp)
        self.state = state
