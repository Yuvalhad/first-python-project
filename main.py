import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game! 🎮")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! 👆")
            elif guess > secret_number:
                print("Too high! 👇")
            else:
                print(f"\n🎉 Congratulations! You found the number {secret_number} in {attempts} attempts!")
                return

            # Show remaining attempts
            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number!")

    print(f"\nGame Over! 😢 The number was {secret_number}")

# This block only runs if you execute main.py directly
if __name__ == "__main__":
    number_guessing_game()