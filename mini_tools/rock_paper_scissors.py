"""Play Rock, Paper, Scissors against the computer."""
import random

CHOICES = ("rock", "paper", "scissors")

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    if (player, computer) in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")):
        return "player"
    return "computer"

def main():
    print("Rock, Paper, Scissors — type quit to stop.")
    while True:
        player = input("Your choice: ").strip().lower()
        if player == "quit":
            break
        if player not in CHOICES:
            print("Choose rock, paper, or scissors.")
            continue
        computer = random.choice(CHOICES)
        result = decide_winner(player, computer)
        print(f"Computer chose {computer}. Result: {result}!")

if __name__ == "__main__":
    main()
