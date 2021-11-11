import random

suits = ["hearts", "clubs", "diamonds", "spades"]
values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self, d=False):
        if self.value == "ace":
            if d:
                return [1, 11][random.randint(0, 1)]

            if input("High or low ace? ").lower() == "h":
                return 11
            else:
                return 1
        elif self.value in ["king", "queen", "jack"]:
            return 10
        else:
            return self.value

    def get_card(self):
        return str(self.value) + " of " + self.suit


class Deck:
    def __init__(self, no_of_decks=1):
        self.deck = []
        for i in range(no_of_decks):
            for suit in suits:
                for value in values:
                    self.deck.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.deck)

    def show_cards(self):
        for card in self.deck:
            print(card.get_card(), end=", ")
        print()

    def get_card(self, number=1):
        if number == 1:
            return self.deck.pop(0)
        else:
            return [self.deck.pop(0) for i in range(number)]

    def get_length(self):
        return len(self.deck)
