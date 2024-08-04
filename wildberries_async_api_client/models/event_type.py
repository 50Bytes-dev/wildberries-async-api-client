from enum import Enum


class EventType(str, Enum):

    MESSAGE = "message"
    REFUND = "refund"
