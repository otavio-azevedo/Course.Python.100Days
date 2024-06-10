from art import logo
import os

print(logo)

print("Lets start the auction! 🧑‍⚖️\n")

auction_open = True
auction_dict = {}

while auction_open:
    name = input("What's your name? \n")
    bid = float(input("What's your bid? \n"))
    auction_dict[name] = bid
    os.system('cls')
    more_bidders = input("Are there more bidders? (Y/N)\n")

    if more_bidders == "N":
        auction_open = False

# Finding the key-value pair with the maximum value
max_key, max_value = max(auction_dict.items(), key=lambda item: item[1])

print(f"The winner is {max_key} with the bid of ${max_value}!")
