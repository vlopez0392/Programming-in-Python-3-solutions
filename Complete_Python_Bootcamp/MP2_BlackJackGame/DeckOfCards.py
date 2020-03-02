########################## SECTION 12  MILESTONE PROJECT 2 - BLACKJACK GAME ############################################
###### Model of a Standard Deck of Cards
import random

class Deck:
    suits = ('HEARTS', 'CLUBS', 'DIAMONDS', 'SPADES')
    deckDic = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9,
               "JACK": 10, "QUEEN": 10, "KING": 10, "ACE": (1, 11)}

    def __init__(self):
        self.deck = []
        for suit in Deck.suits:
            for key in Deck.deckDic.keys():
                self.deck.append((suit, key))
        assert (len(self.deck) == 52)

    def shuffleDeck(self):
        self.deck = random.sample(self.deck, len(self.deck))

    def dealCards(self, initial_deal=False, hit=False):  # Deals cards as required by player and computer dealer at the
        if initial_deal:  # beginning of the game
            cards = random.choices(self.deck, k=2)
        elif hit:
            cards = [random.choice(self.deck)]

        Deck.discardCards(self, cards)
        return cards

    def discardCards(self, cards):  ### Discards the card (or cards) whenever an initial dealing or a hit occur.
        if len(cards) >= 2:
            for card in cards:
                self.deck.remove(card)
        else:
            self.deck.remove(cards[0])
