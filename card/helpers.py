from enum import IntEnum, unique

@unique
class Sides(IntEnum):
    TOP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3