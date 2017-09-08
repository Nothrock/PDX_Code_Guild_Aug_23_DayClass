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

    def draw(self):
        print(self.suit + self.rank)


# class Deck:
#     def __init__(self):


# class Hand:
#     def __init__(self, card):

card = Card('Spades', '2')
print(card)