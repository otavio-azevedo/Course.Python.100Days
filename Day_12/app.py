import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficult = input("Choose a difficulty. Type 'easy' or 'hard':")


def set_difficulty(difficult):
    attempts = EASY_LEVEL if difficult == 'easy' else HARD_LEVEL
    print(f"Ok... you have {attempts} attempts, good luck.")
    return attempts


def start_game():
    random_number = random.randint(1, 100)
    attempts = set_difficulty(difficult)

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == random_number:
            attempts = 0
            print("YOU WIN!🏆")
            break
        else:
            if guess > random_number:
                print("Too high...")
            else:
                print("Too low...")
        attempts -= 1

        if attempts == 0:
            print("YOU LOSE!❌")

        print(f"Attempts left: {attempts}")


start_game()
