"""A small number guessing game with input validation."""
import random


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        raw = input("Your guess (or q to quit): ").strip()
        if raw.lower() == "q":
            print(f"The number was {secret}. Better luck next time!")
            return

        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number from 1 to 100.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return


if __name__ == "__main__":
    play()
