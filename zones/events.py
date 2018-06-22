from enum import Enum


class ZoneEvents(Enum):
    """ All possible zone events. """
    ENTER = "start_touch"
    EXIT = "end_touch"
    TRIGGER = "touch"
