############## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ########################################################
##### Player-logic

import DeckOfCards

class Player():
    def __init__(self, bankRoll, playerName):
        self.bankRoll = bankRoll
        self.playerName = playerName
        self.score = 0

    ### Placing a valid bet
    def placeBet(self):
        placingBet = True
        while placingBet:
            try:
                betAmount = int(input("Please enter the amount to bet: "))
                waitingValidBet = True

                while waitingValidBet:
                    if betAmount <= self.bankRoll:
                        print("A bet has been placed by " + str(self.playerName) + " -- Amount in $: " + str(betAmount))
                        waitingValidBet = False
                        return betAmount
                    else:
                        print("Your bankRoll is insufficient! Please place a valid bet. " + "Your bankroll: "
                              + str(self.bankRoll))
                        betAmount = int(input("Please enter the amount to bet: "))
            except ValueError:
                print("That is an invalid bet! Please input an amount in $!")

    ###Displays the player info
    def displayPlayerInfo(self):
        print("PLAYER INFO: ")
        print("|-"*15 + "|")
        print("Player Name: " + self.playerName)
        print("Available Bank Roll: " + str(self.bankRoll))
        print("|-"*15 + "|" + "\n")

    ### Computing player score
    ### Computing score of initial hand
    def initialDealingScore(self, cards):
        deckDic = DeckOfCards.Deck.deckDic
        for card in cards:
             if card[1] != 'ACE':
                self.score = self.score + deckDic[card[1]]
        return self.score

    ###Computes score when player hits
    def hit(self, card):
        deckDic = DeckOfCards.Deck.deckDic
        if card[0][1] == 'ACE':
            return self.score
        else:
            cardValue = deckDic[card[0][1]]
            self.score = self.score + cardValue
            return self.score

    ### Decision function for ACE value while having a soft hand(Asks for user input)
    ### Hard hands make the ACE value automatically a 1.
    def choose_ace_value(self):
        choosingValue = True
        while choosingValue:
            try:
                print("You have been dealt an ACE! ")
                decision = int(input("Please input the desired value (1 or 11): "))
                if decision not in (1,11):
                    print("That is not a valid decision, please try again! ")
                else:
                    if decision == 1:
                        print("You have chosen to make your ACE a 1")
                        return 1
                    print("You have chosen to make your ACE an 11")
                    return 11
            except ValueError:
                print("Invalid option! Please try again!")

    def printInitialDeal(self, player_deal):
        print("Dealing cards!")
        print("Player goes first...  ")
        print("Player Cards: ")
        print(player_deal)
        print("Score: " + str(self.score) + "\n")

    def printPlayerHand(self, hand):
        print(hand)
        print("Score: " + str(self.score) + "\n")

    def hitOrStay(self):
        deciding = True
        hitOrStay = ('hit', 'stay')

        decision = ''
        while deciding:
            decision = input("Hit or Stay ? ")
            decision = decision.lower()
            if decision not in hitOrStay:
                print("I didn't get that... Speak more clearly !")
                continue
            deciding = False

        if decision == 'hit':
            return True

        return False

# player = Player(100,"Vick")
# deck = DeckOfCards.Deck()
# deck.shuffleDeck()
# someCards = deck.dealCards(initial_deal=True)
# print(someCards)
# anotherCard = deck.dealCards(hit = True)
# print(anotherCard)
#
# print(player.initialDealingScore(someCards))
# print(player.hit(anotherCard))
# print(len(deck.deck))
#
# print(someCards in deck.deck)
# print(anotherCard in deck.deck)
