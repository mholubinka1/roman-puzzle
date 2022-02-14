from argparse import ArgumentError
from typing import List

from helpers import Sides
from symbol_type import SymbolType

class Symbol:
    def __init__(self, symbol_type: SymbolType, half: int):
        self.type = symbol_type
        self.half = half
    
    def is_match(self, other) -> bool:
        if other == None:
            return True
        if other.type != self.type:
            return False
        if other.half + self.half != 0:
            return False
        return True
        

class Card:
    def __init__(self, card_number: int, symbols, orientation = 0):
        self.card_number = card_number
        if len(symbols) != 4:
            raise ArgumentError("A card must have 4 sides.")
        self.sides = symbols
        self.orientation = orientation

    def rotate(self, clockwise: bool = True, rotation_angle: int = 90) -> None:
        allowed_angles = [0, 90, 180, 270]
        if rotation_angle not in allowed_angles:
            raise ArgumentError(f"Card cannot be rotated to that angle: {}".format(rotation_angle))
        right_angle_count = rotation_angle / 90
        self.orientation = (self.orientation + rotation_angle) if clockwise else (self.orientation - rotation_angle)
        self.sides = self.rotate_symbols(self.sides, clockwise, right_angle_count)
        return
    
    def rotate_symbols(sides: List[int], clockwise: bool = True, right_angle_count: int = 1) -> List[int]:
        x = right_angle_count
        if clockwise:
            return sides[-x:] + sides[:-x]
        else:
            return sides[x:] + sides[:x]
        
    def is_match(self, matching_symbols: List[Symbol]) -> bool:
        if len(matching_symbols) != 4:
            raise ArgumentError("Matching list of symbols should be of length 4.")
        for side in Sides:
            if not self.sides[side.value].is_match:
                return False
        return True
        
        
        