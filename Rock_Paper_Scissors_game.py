import random
import os
import re

def prompt_replay():
    """
    Lets the user decide whether to play again.
    Returns True if the user wants to continue, otherwise False.
    """
    while True:
        answer = input("Play again? (Yes/No): ").strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        print("Please answer 'Yes' or 'No'.")

def clear_console():
    """
    Clears the terminal screen based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def determine_winner(player, opponent):
    """
    Determines the winner between the player's choice and the opponent's choice.
    Returns 1 if the player wins, -1 if the opponent wins, and 0 for a tie.
    """
    outcomes = {
        ('R', 'S'): 1,
        ('S', 'P'): 1,
        ('P', 'R'): 1,
        ('S', 'R'): -1,
        ('P', 'S'): -1,
        ('R', 'P'): -1
    }
    return outcomes.get((player, opponent), 0)

def display_result(result, player_score, computer_score):
    """
    Displays the result of the current round and the updated scores.
    """
    if result == 1:
        print("You won this round!")
    elif result == -1:
        print("I won this round!")
    else:
        print("It's a tie!")

    print(f"Current Score - You: {player_score}, Computer: {computer_score}")

def play_game():
    """
    Main function to play Rock, Paper, Scissors.
    Manages the game loop, handles player input, and tracks scores.
    """
    player_score = 0
    computer_score = 0

    while True:
        clear_console()
        print("Welcome to Rock, Paper, Scissors!")

        # User selects their move
        player_move = input("Choose [R]ock, [P]aper, or [S]cissors: ").strip().upper()

        # Validate user input
        if player_move not in ['R', 'P', 'S']:
            print("Invalid choice! Please choose [R], [P], or [S].")
            continue

        # Computer randomly selects its move
        computer_move = random.choice(['R', 'P', 'S'])
        print(f"I chose: {computer_move}")

        # Determine the round winner
        result = determine_winner(player_move, computer_move)
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

        # Display the round result and updated scores
        display_result(result, player_score, computer_score)

        # Ask the player if they want to play another round
        if not prompt_replay():
            break

    # Final score display
    clear_console()
    print("Game over!")
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
