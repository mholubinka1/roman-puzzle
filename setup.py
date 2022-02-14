import json

from card.card import *
from card.side import to_side
from card.symbol_type import to_symbol_type

def create_card(card_number: int, card: dict):
    sides = card['sides']
    symbols = [{to_side(card['id']): Symbol(to_symbol_type(side['symbol']), int(side['half']))} for side in card['sides']]
    return Card(card_number, symbols)


def load_cards(config_path: str):
    with open(config_path) as json_file:
        cards_json = json.load(json_file)
        cards = [create_card(int(id), cards_json[id]) for id in cards_json]
        return cards