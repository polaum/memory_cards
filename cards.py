from pymongo import MongoClient
client = MongoClient()

cards_db = client['cards_db']
cards = cards_db['cards']

class Card:
    def __init__(self, question, answer):
        self.this_card = cards.find_one({'card_index' : self.index})
        if not self.this_card:
            #new card

