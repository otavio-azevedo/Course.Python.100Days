import os
import random
from time import sleep
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_initial_cards():
    return [hit(), hit()]


def hit():
    return random.choice(cards)


end_game = False
player_cards = []
computer_cards = []


def check_result(player_cards, computer_cards, player_score, computer_score):
    print(
        f"Player cards: {player_cards}, current score: {player_score}")
    print(
        f"Computer's cards: {computer_cards}, current score: {computer_score}")
    if player_score > 21 and computer_score < 21:
        print("YOU LOSE! ❌")
    elif player_score == computer_score:
        print("DRAW! ➖")
    elif abs((player_score - 21)) > abs((computer_score-21)):
        print("YOU LOSE! ❌")
    elif abs((player_score - 21)) < abs((computer_score-21)):
        print("YOU WIN! 🏆")

    sleep(2)
    os.system("cls")


def show_players_info(player_cards, computer_cards, player_score):
    print(f"🥸  Player cards: {player_cards}, current score: {player_score}")
    print(f"💻 Computer's first card: {computer_cards[0]}")


while end_game == False:
    want_to_play = input("🎮🎲 Do you want to play a game of Blackjack?(y/n) :")
    end_game = True if want_to_play == "n" else False
    if end_game == True:
        break

    player_cards = get_initial_cards()
    computer_cards = get_initial_cards()
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    show_players_info(player_cards, computer_cards, player_score)

    new_card = True
    while new_card:
        want_to_hit = input("Type 'y' to get another card, type 'n' to pass: ")
        new_card = True if want_to_hit == "y" else False

        if new_card == False or player_score > 21:
            break

        new_card = hit()
        player_cards.append(new_card)
        player_score = sum(player_cards)
        show_players_info(player_cards, computer_cards, player_score)

        if player_score > 21:
            new_card = False

    check_result(player_cards, computer_cards,
                 player_score, computer_score)
