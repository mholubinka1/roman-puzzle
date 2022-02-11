from arrange import MCMCArranger
from setup import *

card_config_file = 'card_config.json'
cards = load_cards(card_config_file)
arranger = MCMCArranger(cards)
