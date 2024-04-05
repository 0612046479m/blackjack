from cards import * 

class Player():
    def __init__(self,name:str='Bill'):
        self.name = name
        self.cards = []
        self.current_card_score = 0
        self.win = False
        self.gameHistory = []
        # self.Ace_chosen_value= #can be 11 or 1