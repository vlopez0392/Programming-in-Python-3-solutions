############## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ########################################################
###### Model of the computer dealer and main game logic

####Imports
import DeckOfCards
import Player
import ComputerDealer

##############################################   Main Game   ###########################################################
game_on = True
twenty_one = 21
print("Welcome to a text-based simplified BlackJack Game! ")
print("Coded by Vick @2020" + "\n")
print("GAME ON!!!")

while game_on:
    ###Start game
    computer_dealer = ComputerDealer.ComputerDealer()
    player = Player.Player(1000, "Vick")
    player.displayPlayerInfo()
    player.placeBet()

    print("Shuffling the deck ...")
    deck = DeckOfCards.Deck()
    deck.shuffleDeck()
    print("Deck shuffled !")

    ###Initial deal# player = Player(100,"Vick")
    player_initial_deal = deck.dealCards(initial_deal= True)
    computer_initial_deal = deck.dealCards(initial_deal=True)

    #Compute initial player and computer score
    player.initialDealingScore(player_initial_deal)
    computer_dealer.computeScore(computer_initial_deal, initial_deal=True)

    #Print to the console
    player.printInitialDeal(player_initial_deal)
    computer_dealer.printComputerDeal(computer_initial_deal, initial_deal=True)

    ########################################## Players turn#############################################################
    print("Player's turn! ")
    player_turn = True
    current_player_hand = player_initial_deal

    while player_turn:
        hit = player.hitOrStay()

        if hit:
            print("Hit! Card received...")
            card = deck.dealCards(hit=hit)
            current_player_hand.append(card)
            player.hit(card)
            player.printPlayerHand(current_player_hand)

            if player.score > twenty_one:
                print("Player bust! The house wins!")
                computer_dealer.printComputerDeal(computer_initial_deal, initial_deal=False)
                player_turn = False

        else:
            print("You have decided to stay! It's now the house's turn! ")
            player.printPlayerHand(current_player_hand)
            player_turn = False

    ###Dealer's Turn
    computer_turn = True
    while computer_turn:

        computer_turn = False

    game_on = False
