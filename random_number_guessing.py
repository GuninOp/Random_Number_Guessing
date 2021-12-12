import random

welcome_text = print("Welcome to Random Number Guessing.")
game_over = False
rand_num = str(random.randrange(1, 11))
guess = input("Guess and Write a Random Number from 1 to 10 or Write q to quit application.\n")

while not game_over:
    if guess == "q":
        break;()
    if guess == rand_num:
        print("You got it correctly.")
        rand_num = str(random.randrange(1, 11))
        guess = input("Guess and Write a Random Number from 1 to 10 or Write q to quit application.\n")
    if guess != rand_num:
        if guess == "q":
            break;()
        print("Try again.")
        guess = input("Guess and Write a Random Number from 1 to 10 or Write q to quit application.\n")
