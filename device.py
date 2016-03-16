from enum import Enum, unique


@unique
class ScreenState(Enum):
    UNKNOWN = -1
    OFF = 0
    ON = 1
    USER_PRESENT = 2

    def is_on(self):
        return self == ScreenState.ON or self == ScreenState.USER_PRESENT

    def is_off(self):
        return self == ScreenState.OFF


@unique
class ScreenOrientation(Enum):
    UNKNOWN = -1
    ZERO = 0
    NINETY = 90
    ONE_EIGHTY = 180
    TWO_SEVENTY = 270

    def is_portrait(self):
        return self == ScreenOrientation.ZERO or self == ScreenOrientation.ONE_EIGHTY

    def is_landscape(self):
        return self == ScreenOrientation.NINETY or self == ScreenOrientation.TWO_SEVENTY


@unique
class PhoneState(Enum):
    UNKNOWN = -1
    IDLE = 0
    OFF_HOOK = 1
    RINGING = 2


class DeviceState:
    def __init__(self):
        self.screen_state = ScreenState.UNKNOWN
        self.screen_orientation = ScreenOrientation.UNKNOWN
        self.phone_state = PhoneState.UNKNOWN
