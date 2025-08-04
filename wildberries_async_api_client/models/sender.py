from enum import Enum


class Sender(str, Enum):

    CLIENT = "client"
    SELLER = "seller"
    WB = "wb"
