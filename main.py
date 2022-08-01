from BlackJack import BlackJack

money = 100

while money > 0:
    print("You have £" + str(money) + " left.")

    bet = money+1

    while not (bet <= money):
        while not (bet := input("How much would you like to bet?\n\t")).isnumeric():
            pass
        bet = int(bet)

    game = BlackJack()
    game.deal()
    while not game.is_game_over():
        print("Current score:", game.get_score())
        game.user_input(input("What do you want to do?\n\t").lower())

    print(game.get_result()[0])
    if game.get_result()[1]:
        money += bet
    else:
        money -= bet

    if money > 0:
        input("Please press enter to continue playing.")
    else:
        print("You have no money left.")
