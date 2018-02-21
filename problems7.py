import random

#Problem 7.1.
#Design the data structures for a generic deck of cards. Explain how you
#would subclass the data structures to implement blackjack.
class Card:
    def __init__(self, suit, rank, aces_high=True):
        self.ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'Jack', 'Queen', 'King']
        if aces_high:
            self.ranks[1] = None
            self.ranks.append('Ace')
        
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.suit = suit
        self.rank = rank

    def __str__(self):
        if aces_high:
            self.ranks
        return "%s of %s" % (self.rank, rank_names[self.suit])

    def __lt__(self, other):
        if self.rank != other.rank:
            return self.rank < other.rank
        else:
            return self.suits.index(self.suit) < self.suits.index(self.rank)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    def __init__(self):
        self.suits =  set(['Clubs', 'Diamonds', 'Hearts', 'Spades'])
        self.ranks = list(range(1, 14))
        self.deck = [Card(rank, suit) for rank in self.ranks
                                      for suit in self.suits]


