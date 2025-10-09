"""
Number Guessing Game
A simple game where the player tries to guess a secret number.
"""

import random


def display_welcome_message():
    """Display the welcome message to the player."""
    print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")


def get_valid_input(prompt):
    """
    Get valid integer input from the user.
    
    Args:
        prompt (str): The prompt message to display
        
    Returns:
        int: Valid integer input from user
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def play_game(secret_number=None, min_range=1, max_range=1000):
    """
    Main game loop.
    
    Args:
        secret_number (int, optional): The secret number to guess. 
                                       If None, generates random number.
        min_range (int): Minimum value for random number generation
        max_range (int): Maximum value for random number generation
    """
    if secret_number is None:
        secret_number = random.randint(min_range, max_range)
    
    attempts = 0
    display_welcome_message()
    
    guess = get_valid_input("Enter a number: ")
    attempts += 1
    
    while guess != secret_number:
        attempts += 1
        
        # Provide helpful hints
        if guess < secret_number:
            print("Ha ha! You're stuck in my loop! Too low!")
        else:
            print("Ha ha! You're stuck in my loop! Too high!")
        
        guess = get_valid_input("Try again: ")
    
    print(f"\nWell done, muggle! You are free now.")
    print(f"You guessed the number in {attempts} attempts!")
    
    return attempts


def main():
    """Main entry point for the game."""
    # You can change these settings
    SECRET_NUMBER = 777  # Set to None for random number
    MIN_RANGE = 1
    MAX_RANGE = 1000
    
    play_game(secret_number=SECRET_NUMBER, min_range=MIN_RANGE, max_range=MAX_RANGE)
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            play_game(secret_number=SECRET_NUMBER, min_range=MIN_RANGE, max_range=MAX_RANGE)
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please answer 'yes' or 'no'.")


if __name__ == "__main__":
    main()