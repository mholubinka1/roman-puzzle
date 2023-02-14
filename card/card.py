from argparse import ArgumentError
from typing import List

from side import Sides, circular_addition
from symbol_type import SymbolType


class Symbol:
    type: SymbolType
    half: int

    def __init__(self, symbol_type: SymbolType, half: int):
        if half not in [1, -1]:
            raise ArgumentError("A symbol half must be -1 or 1")
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
    card_number: int
    symbols: dict
    orientation: int

    def __init__(self, card_number: int, symbols: dict, orientation: int = 0):
        if len(symbols) != 4:
            raise ArgumentError("A card must have 4 sides.")
        if orientation % 90 != 0:
            raise ArgumentError(
                "Card cannot be orientated at that angle: {}".format(orientation)
            )
        self.card_number = card_number
        self.sides = symbols
        self.orientation = orientation

    def change_orientation(
        current_orientation: int, rotation_angle: int, clockwise: bool
    ) -> int:
        mod_angle = rotation_angle % 360
        mod_angle = mod_angle if clockwise else (360 - mod_angle)
        new_orientation = current_orientation + mod_angle
        return new_orientation % 360

    def rotate(self, clockwise: bool = True, rotation_angle: int = 90) -> None:
        if rotation_angle % 90 != 0:
            raise ArgumentError(
                "Card cannot be rotated by that angle: {}".format(rotation_angle)
            )
        self.orientation = self.change_orientation(
            self.orientation, rotation_angle, clockwise
        )
        x = (rotation_angle if clockwise else (360 - (x % 360))) / 90
        self.sides = [
            {Sides[circular_addition(key.value, x)]: value}
            for (key, value) in self.sides
        ]
        return

    def is_match(self, matching_symbols: dict) -> bool:
        if len(matching_symbols) != 4:
            raise ArgumentError("Matching list of symbols should be of length 4.")
        for side in Sides:
            if not self.sides[side].is_match(matching_symbols[side]):
                return False
        return True
