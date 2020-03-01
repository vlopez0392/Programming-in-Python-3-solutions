########################## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ############################################
###### Model of a computer dealer and it's logic
import random
import DeckOfCards

class ComputerDealer:
    def __init__(self, computer_score = 0):
        self.computer_score = computer_score
        self.deckDic = DeckOfCards.Deck.deckDic

    def printComputerDeal(self,computer_deal, initial_deal = False):
        if initial_deal:
            print("Dealing House cards... ")
            print("Dealer Up Card: ")
            randCard = random.randint(0,1)
            show_card = computer_deal[randCard]

            if randCard == 0:
                print(str([show_card,"*****"]))
            else:
                print(str(["*****", show_card]))

            show_score = self.computer_score - self.deckDic[computer_deal[abs(randCard-1)][1]]
            print("House up-card score: " + str(show_score) + "\n")

        else:
            print("House Cards: ")
            print(computer_deal)
            print("House Score: " + str(self.computer_score) + "\n")

    def reset_computer_score(self):
        self.computer_score = 0

    def computeScore(self,cards, initial_deal = False):
        if initial_deal == True:
            for card in cards:
                if card[1] != 'ACE':
                    self.computer_score = self.computer_score + self.deckDic[card[1]]

        else: ##Computer dealer "hits"
            self.computer_score = self.computer_score + self.deckDic[cards[0][1]]

