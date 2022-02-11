from symbol_type import SymbolType

class Symbol:
    def __init__(self, symbol_type: SymbolType, half: int):
        self.type = symbol_type
        self.half = half

class Card:
    def __init__(self, card_number: int, symbols, orientation = 0):
        self.card_number = card_number
        if len(symbols) != 4:
            raise
        self.sides = symbols
        self.orientation = orientation

    def rotate(self, clockwise: bool = True, rotation_angle: int = 90):
        self.orientation = (self.orientation + rotation_angle) if clockwise else (self.orientation - rotation_angle)
        self.sides = self.rotate_symbols(self.sides, clockwise, rotation_angle)
        return
    
    def rotate_symbols(sides, clockwise: bool = True, rotation_angle: int = 90):
        allowed_angles = [0, 90, 180, 270]
        if rotation_angle not in allowed_angles:
            raise
        x = rotation_angle / 90
        if clockwise:
            return sides[-x:] + sides[:-x]
        else:
            return sides[x:] + sides[:x]
        
        
        