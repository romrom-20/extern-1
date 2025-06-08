# Number Guessing Game
# Author: saman

import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game! Try to guess the number between 1 and 100.")

    while attempts < max_attempts:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempt{'s' if attempts > 1 else ''}!")
            break
    else:
        print("Game over! Better luck next time! The number was", number_to_guess)

if __name__ == "__main__":
    guessing_game()
