import random
from cards import StandardDeck as Deck
# run twice and add the values
# print(random.choice(deck))



class Jackle():
    def __init__(self) -> None:
        self.name = 'Jackle the Dealer'
        self.deck = Deck()
        self.deck.shuffle()
        self.cards = []
        self.current_card_score = 0
        self.win = False
        self.gameHistory = []
        self.deal()
    
    def deal(self):
        for i in range(5):
            self.cards.append(self.deck.deal())

    def printCards(self):
        for card in self.cards:
            print(card)
    
    def play(self):