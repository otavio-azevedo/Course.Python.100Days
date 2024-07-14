import random
from art import logo, vs
from data import data


def select_one_from_data():
    return random.choice(data)


def check_winner(option_A, option_B):
    if(option_A['follower_count'] > option_B['follower_count']):
        return 'A'
    else:
        return 'B'


def start_game():
    end_game = False
    score = 0

    while end_game is False:
        option_A = select_one_from_data()
        print(
            f"Compare A: {option_A['name']}, {option_A['description']} from {option_A['country']}")

        print(vs)

        option_B = select_one_from_data()
        print(
            f"Compare B: {option_B['name']}, {option_B['description']} from {option_B['country']}")

        guess = input("Who has more followers? Type 'A' or 'B':")
        winner = check_winner(option_A, option_B)

        if guess == winner:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            end_game = True


print(logo)
start_game()
