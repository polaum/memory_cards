import random

from pymongo import MongoClient

client = MongoClient()

cards_db = client['cards_db']
cards = cards_db['default_cards_collection']


class CreationException(Exception):
    pass


class Card:

    def __init__(self, question, answer):
        self.this_card = cards.find_one({'question': question})
        if not self.this_card:
            # new card
            i = cards.count()
            cards.insert_one({'card_index': i, 'question': question, 'answer': answer})

    @property
    def question(self):
        return self.this_card['question']

    @property
    def answer(self):
        return self.this_card['answer']

    @property
    def card_index(self):
        return self.this_card['card_index']

    @question.setter
    def question(self, value):
        self.this_card['question'] = value
        cards.save(self.this_card)

    @answer.setter
    def answer(self, value):
        self.this_card['answer'] = value
        cards.save(self.this_card)

    def next(self):
        card = cards.find_one({'card_index': (self.card_index + 1)})
        if card:
            return Card(card['question'], card['answer'])

    @staticmethod
    def shuffle():
        card = cards.find_one({'card_index': random.randint(0, cards.count() - 1)})
        return Card(card['question'], card['answer'])


