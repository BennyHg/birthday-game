from calendar import month
from random import randint

name = input("Hi! What is your name?")


for num_guesses in range(5):
    guess_number = 1
    month_number = randint(1, 12)
    year_number = randint(1924, 2004)

    print("Guess: ", name, "were you born", 
        month_number, "/", year_number, "?")

    response = input("yes or no?")

    if response == "yes":
        print("I knew it!")
        exit()
    elif num_guesses == 4:
        print("I have other things to do. Good bye.")
    else:
        print("Drat! Lemme try again!")