import random

suits = ["hearts", "clubs", "diamonds", "spades"]
values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]


class Card:
    def __init__(self, suit, value, turned_over=True):
        self.suit = suit
        self.value = value
        self.turned_over = turned_over

    def get_value(self, d=False):
        if self.turned_over:
            if self.value == "ace":
                if d:
                    return [1, 11][random.randint(0, 1)]

                if input("High or low ace? ").lower() == "high":
                    return 11
                else:
                    return 1
            elif self.value in ["king", "queen", "jack"]:
                return 10
            else:
                return self.value
        else:
            raise Exception('Can\'t get value of turned over card')

    def get_card(self):
        if self.turned_over:
            return str(self.value) + " of " + self.suit
        else:
            return "card"

    def get_suit(self):
        return self.suit

    def turn_over(self):
        self.turned_over = not self.turned_over

    def is_turned_over(self):
        return self.turned_over


class Deck:
    def __init__(self, no_of_decks=1, turned_over=True):
        self.deck = []
        for i in range(no_of_decks):
            for suit in suits:
                for value in values:
                    self.deck.append(Card(suit, value, turned_over))

    def shuffle(self):
        random.shuffle(self.deck)

    def show_cards(self):
        for card in self.deck:
            print(card.get_card(), end=", ")
        print()

    def get_card(self, number=1, turned_over=True):
        if number == 1:
            return self.deck.pop(0)
        else:
            return [self.deck.pop(0) for i in range(number)]

    def get_length(self):
        return len(self.deck)
