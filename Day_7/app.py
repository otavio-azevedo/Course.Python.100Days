
import random
from hangman_art import stages, logo
from hangman_word_list import word_list
import os

print(logo)

chosen_word = random.choice(word_list)

print(chosen_word)

chosen_word_len = len(chosen_word)
blanks_list = list("_" * chosen_word_len)

lives = len(stages)-1
guesses = []


while "_" in blanks_list and lives > 0:
    user_guess = input("Guess a letter: ")
    user_guess = user_guess.lower()

    if user_guess in guesses:
        print("You already tried this letter, please give a different guess... 😑")
        continue

    guesses.append(user_guess)

    os.system("cls")
    if(user_guess not in chosen_word):
        lives -= 1
        print(
            f"The word doesn't contains your guess 🥲. \nYou lose a life and now you have {lives} lives ❤️")

    for index, letter in enumerate(chosen_word):
        if user_guess == letter:
            blanks_list[index] = letter

    print(blanks_list)
    print(stages[lives])

result = "WIN 🎉" if lives > 0 else "LOOSE 💀"
print(f"YOU {result} !")
