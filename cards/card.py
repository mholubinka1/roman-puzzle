
class Side:
    def __init__(self, symbol):
        self.symbol = symbol


class Card:
    def __init__(self, symbols):
        self.sides = (Side(symbol) for symbol in symbols)
        self.orientation = 1
