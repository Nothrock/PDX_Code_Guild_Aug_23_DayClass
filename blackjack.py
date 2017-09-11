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
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + ' of ' + str(self.suit)

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


class Deck:
    def __init__(self):
        suits = [Spades, Hearts, Clubs, Diamonds]
        ranks = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, K, Q]


    def shuffle(self):
        random.shuffle(self.cards)


# class Hand:
#     def __init__(self, card):

card = Card('Spades', '2')
print(card)