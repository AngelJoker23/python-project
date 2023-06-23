import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (Rock/Paper/Scissors) or 'I quit' to exit: ").lower()
        if choice in ["rock", "paper", "scissors", "i quit"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Game Tied"
    elif (player_choice == "rock" and computer_choice == "paper") or \
         (player_choice == "scissors" and computer_choice == "rock") or \
         (player_choice == "paper" and computer_choice == "scissors"):
        return "You Lose"
    else:
        return "You Win"

# Main game loop
while True:
    player_choice = get_player_choice()

    if player_choice == "i quit":
        print("Thank you for playing.")
        break

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    print(f"Player: {player_choice.capitalize()}")
    print(f"Computer: {computer_choice.capitalize()}")
    print(result)
    print()
