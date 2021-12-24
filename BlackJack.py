from deckOfCards import Deck


class BlackJack:
    def __init__(self):
        self.game_over = False
        self.result = ""
        self.cards = []
        self.deck = Deck()
        self.deck.shuffle()
        self.score = 0
        self.dealer_score = 0

    def deal(self):
        self.hit()
        self.hit()

        if self.score == 21:
            self.game_over = True
            self.result = ["Black Jack!", True]

    def hit(self):
        card = self.deck.get_card()
        print("You drew a\n\t", card.get_card())
        self.cards.append(card)
        self.score += card.get_value()
        if self.score > 21:
            self.game_over = True
            self.result = ["Bust!", False]

    def dealer_play(self):
        self.dealer_score += self.deck.get_card().get_value(d=True)
        self.dealer_score += self.deck.get_card().get_value(d=True)

        while self.dealer_score <= 17:
            self.dealer_score += self.deck.get_card().get_value(d=True)

    def fold(self):
        self.game_over = True
        self.result = ["You folded!", False]

    def stand(self):
        self.dealer_play()
        if 21 >= self.dealer_score > self.score:
            self.result = ["You lose!", False]
        else:
            self.result = ["You win!", True]
        print("You:", self.score, "\nDealer:", self.dealer_score)

        self.game_over = True

    def is_game_over(self):
        return self.game_over

    def get_score(self):
        return self.score

    def get_result(self):
        return self.result

    def user_input(self, option):
        if option == "hit":
            self.hit()
        elif option == "stand":
            self.stand()
        elif option == "fold":
            self.fold()
