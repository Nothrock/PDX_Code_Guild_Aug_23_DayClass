# I think the main issue is having logic in odd places. I would suggest a structure like the following:
#
# Card - holds the value and suit of an individual card;
# Deck - holds the cards and the logic for shuffling and dealing;
# Hand - another collection of cards, with the logic for adding up scores. The hand doesn't need to know its owner, the logic for which Cards in the Hand to show should be in the Player. It shouldn't access a global deck - implement e.g. def draw_from(self, deck):;
# Player - a player has a Hand of Cards, the input logic (hit_or_stand, which should incorporate validation), the rules for showing the cards, their credit and stats, etc.;
# Dealer - a subclass of Player holding the dealer's playing logic and the different rules for showing its hand;
# Game - holds the deck and the players and the logic for progressing through the game, including e.g. history, which should be Game instance attributes rather than global variables.


import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return str(self.rank) + ' of ' + str(self.suit)

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Deck:
    def __init__(self):
        self.suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.ranks = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10),
                 ('Q', 10), ('K', 10), ('A', 11)]
        self.cards = []
        for r in self.ranks:
            for s in self.suits:
                c = Card(suit = s, rank = r[0], value = r[1])
                # c.rank = r[0]
                # c.value = r[1]
                # c.suit = s
                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def cut_deck(self):
        self.cut_1 = []
        self.cut_2 = []
        self.cut_1 = self.cards[0:len(self.cards)//2]
        self.cut_2  = self.cards[len(self.cards)//2:]
        # self.cut_2.append(self.cut_1)
        self.cards = self.cut_2 + self.cut_1
        # testing the cut_deck
        print('Length:', len(self.cards), len(self.cut_1), len(self.cut_2))

    def show(self):
        for i in self.cards:
            print(i)



class Hand:
    def __init__(self):
        pass





deck = Deck()
for i in deck.cards:
    print(i)
# deck.shuffle()
# for i in deck.cards:
#     print(i)
deck.show()
print('cutting the deck')
deck.cut_deck()
print("Length: ", len(deck.cards))
deck.show()