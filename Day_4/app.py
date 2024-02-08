import random
import rockpaperscissors

print("Welcome to the famous RPS Game - Rocke, Paper or Scissors? 🪨 📄 ✂️\n")

user_choice = int(input("What do you choose? (0 = Rock, 1 = Paper or 2 = Scissors)\n"))

if 0 > user_choice or user_choice > 2:
    raise Exception("Invalid choice.")

print(f"Your choice:\n {rockpaperscissors.options[user_choice]}")

computer_choice = random.randint(0,2)
print(f"Computer choice:\n {rockpaperscissors.options[computer_choice]}")

if user_choice == computer_choice:
    print("DRAW! 🫠")
elif user_choice == 0 and computer_choice == 1:
    print("YOU LOOSE! 🥲")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN! 🎉")
elif user_choice == 1 and computer_choice == 0:
    print("YOU WIN! 🎉")
elif user_choice == 1 and computer_choice == 2:
    print("YOU LOOSE! 🥲")
elif user_choice == 2 and computer_choice == 0:
    print("YOU LOOSE! 🥲")
elif user_choice == 2 and computer_choice == 1:
    print("YOU WIN! 🎉")