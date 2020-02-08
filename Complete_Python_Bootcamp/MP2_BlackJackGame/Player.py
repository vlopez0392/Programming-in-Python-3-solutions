############## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ########################################################
##### Player-logic

class Player():
    def __init__(self, bankRoll, playerName):
        self.bankRoll = bankRoll
        self.playerName = playerName

    ### Placing a valid bet
    def placeBet(self):
        betAmount = int(input("Please enter the amount to bet: "))
        waitingValidBet = True

        while waitingValidBet:
            if betAmount <= self.bankRoll:
                print("A bet has been placed by " + str(self.playerName) + " -- Amount in $: " + str(betAmount))
                waitingValidBet = False
                return betAmount
            else:
                print("Your bankRoll is insufficient! Please place a valid bet.")
                betAmount = int(input("Please enter the amount to bet: "))

    ###Displays the player info
    def displayPlayerInfo(self):
        print("PLAYER INFO: ")
        print("|-"*15 + "|")
        print("Player Name: " + self.playerName)
        print("Available Bank Roll: " + str(self.bankRoll))
        print("|-"*15 + "|" + "\n")

