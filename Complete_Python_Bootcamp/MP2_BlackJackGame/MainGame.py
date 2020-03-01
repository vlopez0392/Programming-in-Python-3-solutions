########################## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ############################################
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

def play_again():
    deciding = True
    while deciding:
        try:
            decision = input("Play again? Enter Y/N: ")
            if decision.lower() in ("y", "yes"):
                print("\n")
                return True
            elif decision.lower() in ("n", "no"):
                return False
        except ValueError:
            print("Invalid decision, try again by typing yes, no, y or n")


###Start game
computer_dealer = ComputerDealer.ComputerDealer()
player = Player.Player(1000, "Vick")
first_game = True

while game_on:
    player.displayPlayerInfo()
    this_bet = player.placeBet()

    if not first_game:
        player.reset_player_score()
        computer_dealer.reset_computer_score()

    print("Shuffling the deck ...")
    deck = DeckOfCards.Deck()
    deck.shuffleDeck()
    print("Deck shuffled !")
    print("Dealing cards !" + "\n")

    ###Initial deal# player = Player(100,"Vick")
    player_initial_deal = deck.dealCards(initial_deal= True)
    computer_initial_deal = deck.dealCards(initial_deal=True)

    #Compute initial player and computer score
    player.initialDealingScore(player_initial_deal)
    computer_dealer.computeScore(computer_initial_deal, initial_deal=True)

    #Print to the console
    player.printInitialDeal(player_initial_deal)
    computer_dealer.printComputerDeal(computer_initial_deal, initial_deal=True)

    ########################################## Player's turn############################################################
    print("Player's turn! ")
    player_turn = True
    player_bust = False
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
                player.lostBet(betAmount=this_bet)
                computer_dealer.printComputerDeal(computer_initial_deal, initial_deal=False)
                player_bust = True
                player_turn = False

        else:
            print("You have decided to stay! It's now the house's turn! ")
            print("Player's Hand: ")
            player.printPlayerHand(current_player_hand)
            player_turn = False

    if player_bust:
        if player.bankRoll <= 0:
            print("Bankroll reached 0! Get some more money please!")
            break
        else:
            keepPlaying = play_again()
            if keepPlaying:
                first_game = False
                continue
            else:
                print("GAME OVER !")
                break

    ########################################## Dealer's turn############################################################
    computer_turn = True
    while computer_turn:
        print("Revealing the house Cards... ")
        computer_dealer.printComputerDeal(computer_initial_deal, initial_deal=False)
        computer_turn = False

    game_on = False

