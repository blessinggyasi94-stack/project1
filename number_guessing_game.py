"""
Number Guessing Game
An interactive console-based game where players guess a randomly generated number.
Features difficulty levels, attempt limits, and user-friendly feedback.
"""

import random


def get_difficulty_settings():
    """
    Returns difficulty settings based on user choice.
    Returns: tuple (max_number, max_attempts, difficulty_name)
    """
    print("\n" + "="*50)
    print("Select Difficulty Level:")
    print("="*50)
    print("1. Easy   - Numbers 1-50,  10 attempts")
    print("2. Medium - Numbers 1-100, 7 attempts")
    print("3. Hard   - Numbers 1-200, 5 attempts")
    print("4. Expert - Numbers 1-500, 3 attempts")
    print("="*50)
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            return (50, 10, "Easy")
        elif choice == "2":
            return (100, 7, "Medium")
        elif choice == "3":
            return (200, 5, "Hard")
        elif choice == "4":
            return (500, 3, "Expert")
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


def get_user_guess(max_number):
    """
    Gets and validates user's guess.
    Args:
        max_number: Maximum valid number for the guess
    Returns:
        int: Valid user guess
    """
    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_number}): "))
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_number}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def play_game():
    """Main game loop."""
    print("\n" + "="*50)
    print("Welcome to the Number Guessing Game!")
    print("="*50)
    
    # Get difficulty settings
    max_number, max_attempts, difficulty = get_difficulty_settings()
    
    # Generate random number
    secret_number = random.randint(1, max_number)
    
    print(f"\n{'='*50}")
    print(f"Difficulty: {difficulty}")
    print(f"Range: 1 to {max_number}")
    print(f"Maximum Attempts: {max_attempts}")
    print(f"{'='*50}\n")
    
    attempts = 0
    guessed = False
    
    # Main guessing loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts
        
        print(f"\nAttempt {attempts} of {max_attempts}")
        if remaining > 0:
            print(f"Remaining attempts: {remaining}")
        
        guess = get_user_guess(max_number)
        
        # Check guess
        if guess == secret_number:
            print(f"\n{'='*50}")
            print(f"🎉 Congratulations! You guessed it!")
            print(f"The number was {secret_number}.")
            print(f"You found it in {attempts} attempt(s).")
            print(f"{'='*50}")
            guessed = True
            break
        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")
        else:
            print("📉 Too high! Try a lower number.")
        
        # Provide hint based on remaining attempts
        if remaining > 0:
            difference = abs(guess - secret_number)
            if difference <= 5:
                print("💡 You're very close!")
            elif difference <= 15:
                print("💡 You're getting warmer!")
    
    # Game over message if not guessed
    if not guessed:
        print(f"\n{'='*50}")
        print(f"Game Over! You've run out of attempts.")
        print(f"The secret number was {secret_number}.")
        print(f"{'='*50}")


def main():
    """Main function to run the game."""
    while True:
        play_game()
        
        # Ask if user wants to play again
        print("\n" + "="*50)
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    main()

