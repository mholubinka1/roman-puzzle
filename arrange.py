from typing import Dict, List

from card.card import Card, Symbol
from card.side import Sides


class MCMCArranger:
    def __init__(self, cards: List[Card], cols: int = 4, rows: int = 3):
        self.cards = cards
        self.cols = cols
        self.rows = rows
        self.arranged_cards = [([None] * rows) for row in ([None] * cols)]
        
    def solve(self) -> List[List[Symbol]]:
        possible_orientations = [0, 90, 180, 270]
        ## need to track tried states through loops
        for card in self.cards:
            ##start in position 1
            placed_cards = []
            for y in range(self.rows):
                for x in range(self.cols):
                    print("Success")
                # find required matches (express this as an array of other symbols with Nones)
                # find a possible match in non used cards
                # 
            #self.arranged_cards[0][0] = card
            #placed_cards.append(card.card_number)
        return
    
    def find_top_match(x, y) -> Symbol:

    def find_required(x: int, y: int, i_arrangement) -> Dict:
        top = find_top_match(x, y)
        right = None
        bottom = None
        left = None        
        return {
            Sides.TOP : top,
            Sides.RIGHT : right,
            Sides.BOTTOM : bottom,
            Sides.LEFT : left
        }