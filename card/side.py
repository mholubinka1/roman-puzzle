from enum import IntEnum, unique

@unique
class Sides(IntEnum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4
    
def to_side(side_string: str):
    return Sides[side_string.upper()]

def circular_addition(x: int, y: int, mod: int = 4) -> int:
    return (x + y) % mod