from argparse import ArgumentError
from typing import List

from side import Sides, circular_addition
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
    def __init__(self, card_number: int, symbols: dict, orientation: int = 0):
        if len(symbols) != 4:
            raise ArgumentError("A card must have 4 sides.")
        remainder = orientation % 90
        if remainder != 0:
            raise ArgumentError("Card cannot be orientated at that angle: {}".format(orientation))
        self.card_number = card_number
        self.sides = symbols
        self.orientation = orientation

    def change_orientation(current_orientation: int, rotation_angle: int = 90, clockwise: bool = True) -> int:
        new_orientation = (current_orientation + rotation_angle) if clockwise else (current_orientation - rotation_angle)
        return new_orientation % 360
        
    def rotate(self, clockwise: bool = True, rotation_angle: int = 90) -> None:
        remainder = rotation_angle % 90
        if remainder != 0:
            raise ArgumentError("Card cannot be rotated to that angle: {}".format(rotation_angle))
        x = rotation_angle / 90
        x = x if clockwise else (360 - (x % 360))       
        self.sides = [{Sides[circular_addition(key.value, x)]: value} for (key, value) in self.sides]
        return
    
    def is_match(self, matching_symbols: dict) -> bool:
        if len(matching_symbols) != 4:
            raise ArgumentError("Matching list of symbols should be of length 4.")
        for side in Sides:
            if not self.sides[side].is_match(matching_symbols[side]):
                return False
        return True
        
        
        