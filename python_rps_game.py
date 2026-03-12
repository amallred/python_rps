import random

# User input (r/p/s)
player_input = input("Choose your move. Type rock, paper, or scissors: ")
# Convert input to lowercase
lower_input = player_input.lower()

# Validate entry (r/p/s)
    # Compare to list of r/p/s
options = ["rock", "paper", "scissors"]

# if match, continue
if lower_input in options:
    # computer play is randomized from list
    computer_move = random.choice(options)
    print(f"Your move is: {lower_input}")
    print(f"Computer move is: {computer_move}")
    # if comp & input are same: print tie
    if computer_move == lower_input:
        print("It's a tie!")

    # if comp or input = r & comp or input = s
    elif computer_move == "rock" and lower_input == "scissors":
        print("Computer wins!")

    # if comp or input = s & comp or input = p
    elif computer_move == "scissors" and lower_input == "paper":
        print("Computer wins!")

    # if comp or input = p & comp or input = r
    elif computer_move == "paper" and lower_input == "rock":
        print("Computer wins!")
    else:
        print("You win! 🎉🎉🎉")

# if not, error message
else:
    print(f"{lower_input} is not an option")

# print both choices
# print who won / tie