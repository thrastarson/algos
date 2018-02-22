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
        
        if rank == 1 and aces_high:
            self.rank = 14
        else:
            self.rank = rank
    
    def is_face_card(self):
        return self.ranks[self.rank] in ('Jack', 'Queen', 'King')

    def is_ace(self):
        return self.rank == 1 or self.rank == 14

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

    def shuffle(self):
        random.shuffle(self.deck)

    def add_card(self, card):
        self.deck.append(card)

    def remove_card(self):
        return self.deck.remove(card)

    def pop_card(self, index=-1)
        return self.cards.pop(index)

    def sort(self):
        self.deck.sort()

    def size(self):
        return len(self.deck)

    def is_empty(self):
        return len(self.deck) == 0

class Hand:
    def __init__(self, hand=None):
        if hand is None:
            self.hand = []
        else:
            self.hand = hand

    def score(self):
        return sum(card.rank for card in self.hand)

    def add_card(self, card)
        self.hand.append(card)

class BlackJackHand(Hand):
    def __init__(self, hand=None):
        super().__init__(hand=hand)

    def score(self):
        high_score = 0
        low_score = 0
        for card in self.hand:
            if card.is_face_card():
                low_score += 10
                high_score += 10
            elif card.is_ace():
                low_score += 1
                high_score += 11
            else:
                low_score += card.rank
                high_score += card.rank
        
        if scores[0] == scores[1]:
            return scores[0]
        else:
            if high_score <= 21 or low_score <= 21:
                return max(high_score, low_score)
            else:
                return min(high_score, low_score)
    
    def busted(self):
        return self.score() > 21

    def is_21(self):
        return self.score() == 21

    def is_black_jack(self):
        return len(self.hand) == 2 and self.is_21()

    def is_push(self, other):
        if self.score() == other.score()

#Problem 7.2
#Imagine you have a call center with three levels of employees: respondents,
#manager, and director. An incoming telephone call must be first allocated
#to a respondent who is free. If the respondent can't handle the call, he
#or she must escalate the call to a manager. If the manager is not free or not
#able to handle it, then the call should be escalated to a director. Design
#the classes and data structures for this problem. Implement a method dispatchCall()
#which assigns a call to the first available employee.
class CallCenter:
    def __init__(self, director, manager, respondents):
        if respondents is None:
            self.respondents = []
        else:
            self.respondents = respondents

        self.director = director
        self.manager = manager

    def dispatch_call(self, call):
        for respondent in self.respondents:
            if respondent.is_free():
                respondent.assign_call(call)
                return

        if manager.is_free():
            manager.assign_call(call)
        elif director.is_free():
            director.assign_call(call)
        else:
            raise ValueError('Nobody is available.')

class Employee:
    def __init__(self, name):
        self.name = name
        self.is_free = True

    def is_free(self):
        return self.is_free

    def assign_call(self, call):
        self.is_free = False
        self.process_call(call)

    def process_call(self, call):
        #something

class Respondent(Employee):
    def __init__(self, name):
        super().__init__(name)

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

class Director(Employee):
    def __init__(self, name):
        super().__init__(name)
    



















