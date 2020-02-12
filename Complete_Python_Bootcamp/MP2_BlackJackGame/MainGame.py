############## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ########################################################
####Imports
import random
import DeckOfCards
import Player

##Dealing with the computer dealer
########################################################################################################################
def printComputerDeal(computer_deal):
    print("Dealing House cards... ")
    print("Dealer Up Card: ")
    randCard = random.randint(0,1)
    show_card = computer_deal[randCard]

    if randCard == 0:
        print(str([show_card,"*****"]) +  "\n")
    else:
        print(str(["*****", show_card]) + "\n")

##Main Game
########################################################################################################################
game_on = True
print("Welcome to a text-based simplified BlackJack Game! ")
print("Coded by Vick @2020" + "\n")
print("GAME ON!!!")

while game_on:
    ###Start game
    player = Player.Player(1000, "Vick")
    player.displayPlayerInfo()
    player.placeBet()

    print("Shuffling the deck ...")
    deck = DeckOfCards.Deck()
    deck.shuffleDeck()
    print("Deck shuffled !" + "\n")

    ###Initial deal
    player_initial_deal   = deck.dealCards(initial_deal= True)
    computer_initial_deal = deck.dealCards(initial_deal=True)
    player.printPlayerDeal(player_initial_deal)
    printComputerDeal(computer_initial_deal)

    ###Players turn
    print("Player's turn! ")
    player_turn = True
    current_player_hand = player_initial_deal

    while player_turn:
        hit = player.hitOrStay()
        if hit:
            card = deck.dealCards(hit = hit)
            current_player_hand.append(card)

        player_turn = False

    ###Dealer's Turn
    computer_turn = True
    while computer_turn:
        computer_turn = False

    game_on = False
