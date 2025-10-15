import random

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\nWelcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess == secret_number:
            print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
        
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")

    print(f"\nGame Over! The number was {secret_number}.")
    return False

def main():
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()