from enum import Enum, unique


@unique
class EventType(Enum):
    UNKNOWN = 'unknown'
    PSEUDO = 'pseudo'
    # Trace File Events
    APP_LAUNCH = 'app_start'
    SCREEN = 'screen'
    SCREEN_ORIENTATION = 'screen_orientation'
    PHONE = 'phone'
    PACKAGE = 'package'

    # Notification events
    NOTIFICATION = 'notification'

    # Network Events
    NETWORK = 'network'

    # Battery Events
    BATTERY = 'battery'
    BATTERY_LEVEL = 'battery.level'
    BATTERY_TEMPERATURE = 'battery.temperature'
    BATTERY_STATUS = 'battery.status'
    BATTERY_PLUG_STATUS = 'battery.plug_status'
    BATTERY_ENERGY_STATE = 'battery.energy_state'

    STORAGE = 'storage'
    HEADSET = 'headset'
    DOCK = 'dock'
    BLUETOOTH = 'bluetooth'

    SYSTEM_MEMORY_SNAPSHOT = 'system.memory_snapshot'

    PRELOAD_APP = 'preload_app'

    # Simulator Events
    DEBUG = 'sim.debug'


class Event:
    def __init__(self,  timestamp, event_type):
        self.timestamp = timestamp
        self.type = event_type
        self.source = None
        self.dest = None

    def get_type(self):
        return self.type

    def get_timestamp(self):
        return self.timestamp

    def get_source(self):
        return self.source

    def get_dest(self):
        return self.dest

    def __repr__(self, *args, **kwargs):
        return '%s: %s' % (self.timestamp, self.type.value)


class AppLaunchEvent(Event):
    def __init__(self, timestamp, app_id, source_class):
        Event.__init__(self, event_type=EventType.APP_LAUNCH, timestamp=timestamp)
        self.app_id = app_id
        self.source_class = source_class

    def __repr__(self, *args, **kwargs):
        return '%s - %s' % (Event.__repr__(self, args, kwargs), self.app_id)


class ScreenEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.SCREEN, timestamp=timestamp)
        self.state = state


class ScreenOrientationEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.SCREEN_ORIENTATION, timestamp=timestamp)
        self.state = state


class PhoneEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.PHONE, timestamp=timestamp)
        self.state = state


class PackageEvent(Event):
    def __init__(self, timestamp, package_event, package=None):
        Event.__init__(self, event_type=EventType.PACKAGE, timestamp=timestamp)
        self.event = package_event
        self.package = package


class NotificationEvent(Event):
    def __init__(self, timestamp):
        Event.__init__(self, event_type=EventType.NOTIFICATION, timestamp=timestamp)


class NetworkEvent(Event):
    def __init__(self, timestamp):
        Event.__init__(self, event_type=EventType.NETWORK, timestamp=timestamp)


class BatteryEvent(Event):
    def __init__(self, timestamp):
        Event.__init__(self, event_type=EventType.BATTERY, timestamp=timestamp)


class StorageEvent(Event):
    def __init__(self, timestamp):
        Event.__init__(self, event_type=EventType.STORAGE, timestamp=timestamp)


class HeadsetEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.HEADSET, timestamp=timestamp)
        self.state = state


class DockEvent(Event):
    def __init__(self, timestamp, state):
        Event.__init__(self, event_type=EventType.DOCK, timestamp=timestamp)
        self.state = state


class BluetoothEvent(Event):
    def __init__(self, timestamp, bluetooth_event):
        Event.__init__(self, event_type=EventType.BLUETOOTH, timestamp=timestamp)
        self.event = bluetooth_event


class SystemMemorySnapshot(Event):
    def __init__(self, timestamp):
        Event.__init__(self, event_type=EventType.SYSTEM_MEMORY_SNAPSHOT, timestamp=timestamp)
