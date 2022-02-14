from typing import List
from card.card import Card, Symbol

class MCMCArranger:
    def __init__(self, cards: List[Card], cols: int = 4, rows: int = 3):
        self.cards = cards
        self.cols = cols
        self.rows = rows
        self.arranged_cards = [([None] * rows) for row in ([None] * cols)]
        
    def solve(self) -> List[List[Symbol]]:
        placed_cards = []
        for card in self.cards:
            for y in range(self.rows):
                for x in range(self.cols):
                    print("Success")
                # find required matches (express this as an array of other symbols with Nones)
                # find a possible match in non used cards
                # 
            #self.arranged_cards[0][0] = card
            #placed_cards.append(card.card_number)
        return

    def find_required(x, y) -> List[Symbol]:
        ## do each direction in turn up, right, down, left
        return