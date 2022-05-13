import random
from ssl import Options

user_wins = 0

comp_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit.").lower()
    if user_input == "q":
        break
    if user_input not in["rock", "paper", "scissors"]:
        continue
    random_number = random.randint(0, 2) #rock: 0, paper:1, scissors:2

    comp_pick = options[random_number]
    print ("Computer Picked", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and comp_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        comp_wins += 1

print("You won", user_wins, "times.")
print("Computer won", comp_wins, "times.")

print("GoodBye!")


