from deckOfCards import Deck

deck = Deck()
deck.shuffle()


def dealer_play():
    dealer = 0
    dealer += deck.get_card().get_value(d=True)
    dealer += deck.get_card().get_value(d=True)

    while dealer <= 17:
        dealer += deck.get_card().get_value(d=True)
    return dealer


score = 0
game_ended = False

card1 = deck.get_card()
card2 = deck.get_card()
print("You have been dealt:\n\t", card1.get_card(), "\n\t", card2.get_card())
score += card1.get_value() + card2.get_value()

if score == 21:
    print("Black Jack!")
    game_ended = True

fold = False

while score <= 21 and not game_ended:
    print("Current score:", score)
    option = input("What do you want to do? ").lower()
    if option == "hit":
        card = deck.get_card()
        print("You drew a\n\t", card.get_card())
        score += card.get_value()
    elif option == "fold":
        fold = True
        break
    elif option == "stand":
        dealer_score = dealer_play()
        if 21 >= dealer_score > score:
            print("You lose!")
        else:
            print("You win!")
        print("You:", score, "\nDealer:", dealer_score)
        break

if not fold:
    if score == 21:
        print("Perfect score!")
    elif score > 21:
        print("Bust!")
else:
    print("You folded.")
