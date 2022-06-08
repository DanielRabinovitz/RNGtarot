import random
import pandas

class Tarot:
    def __init__(self):
        #list of all words
        self.words = pandas.read_table('wordlist.txt', delimiter=' ')
        #dict of cards
        self.cards = {}

    #makes new dict of cards, overwrites the old one
    def new_cards(self):
        for i in ['Past', 'Present', 'Future']:
            number = random.randint(1, 10)
            number = str(number)
            word = self.words.iloc[random.randint(0, self.words.shape[0]-1)]
            card = f'{number}\nof\n{word[0]}'
            self.cards[i] = card
    
