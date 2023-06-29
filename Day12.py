# Guessing game to understand scope

import random

GUESSING_WORD = random.randint(1, 100)
EASY_LEVEl_ATTEMPTS = 10
HARD_LEVEl_ATTEMPTS = 5

def mode():
    print("Welcome to digit Guessing Game!! ")
    print("Guess a number between 1 and 100")
    easy_or_hard = input("Choose a difficulty level- easy_level or hard_level:").lower()
    if easy_or_hard == "easy":
        print("You have 10 attempts.")
        return EASY_LEVEl_ATTEMPTS
    else:
        print("You have 5 attempts.")
        return HARD_LEVEl_ATTEMPTS


def guessing_game(mode, random_digit):
    while mode:
        guessed_word = int(input("Guess a number:"))
        if guessed_word > random_digit:
            print("Guess is too high")
            mode -= 1
            if mode == 0:
                print("Your all attempts are over!!")
                print(f"It was {random_digit}")
            else:
                print(f"You have only {mode} attempt(s)")
        elif guessed_word < random_digit:
            print("Guess is too low")
            mode -= 1
            if mode == 0:
                print("Your all attempts are over!!")
                print(f"It was {random_digit}")
            else:
                print(f"You have only {mode} attempt(s)")
        else:
            print(f"You guessed it right, its {random_digit}")
            break


guessing_game(mode=mode(), random_digit=GUESSING_WORD)
