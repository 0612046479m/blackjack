from PIL import Image
import random, os
# from player import Player

fp = os.path.dirname(os.path.realpath(__file__))
# ACE is equal to 11 or 1 depending on 

class Card():
    #card Names
    cNs = {
        "1": "Ace",
        "11": "Jack",
        "12": "Queen",
        "13": "King"
    }
    for i in range(2,11):
        cNs[str(i)] = str(i)
            
    def __init__(self,value:int,suit:int):
        self.value = value
        self.suit = suit
        self.suits = ['spades','hearts','clubs' ,'diamonds']      
        self.name = Card.cNs[str(self.value)]

    def __str__(self):
        return f"{Card.cNs[str(self.value)]} of {self.suits[self.suit]}"
    
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
        random.shuffle(self)
        # print('Shuffled The Deck')
    
    def deal(self) -> Card:
        top = self[0]
        self.remove(top)
        return top
    


if __name__ == "__main__":
    deck = StandardDeck()
    deck.shuffle()

    # for card in deck:
    #     print(card)

    # player = Player()
    # print(deck[0])  
    # player.cards.append(deck.deal())
    # print(player.cards[0])
    # print(deck[0])
    # print(len(deck))













