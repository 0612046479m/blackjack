from PIL import Image
import random, os

fp = os.path.dirname(os.path.realpath(__file__))


# ACE is equal to 11 or 1 depending on 

class Card():
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        self.suits = ['spades','hearts','clubs' ,'diamonds']
        #card Names
        self.cNs = {
            "1": "Ace",
            "11": "Jack",
            "12": "Queen",
            "13": "King"
        }
        for i in range(2,11):
            self[str(i)] = str(i)
        self.name = self.cNs[str(self.value)]

    def __str__(self):
        return f"{self.cNs[str(self.value)]} of {self.suits[self.suit]}"
    
    def getAsset(self):
        #ex 3 of hearts, aessets/cards/hearts-3.png
        return Image.open(f"{fp}/assets/cards/{self.suits[self.suit]}-{self.value}.png")
    
    def getVal(self):
        pass

class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(1,14))
        [[self.append(Card(v,s)) for s in suits]for v in values]     
    
    def shuffle(self):
        random.shuffle(deck)
        # print('Shuffled The Deck')
    
    def deal(self):
        top = self[0]
        self.remove(top)
        return top


if __name__ == "__main__":
    deck = StandardDeck()
    deck.shuffle()

    for card in deck:
        print(card)


    print(len(deck))   
    print(deck.deal())
    print(len(deck))













