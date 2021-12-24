from BlackJack import BlackJack

money = 100

while money > 0:
    bet = int(input("How much would you like to bet?\n\t"))
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
    print("You have £" + str(money) + " left.")

    input("Please press enter to continue playing.")



print("You're out of money!")
