"""Calculate a restaurant bill with an optional tip split."""

def calculate_total(bill, tip_percent, people=1):
    if bill < 0 or tip_percent < 0 or people < 1:
        raise ValueError("Bill and tip must be non-negative; people must be at least 1.")
    total = bill * (1 + tip_percent / 100)
    return total, total / people


def main():
    try:
        bill = float(input("Bill amount: ₹"))
        tip = float(input("Tip percentage: "))
        people = int(input("Split between how many people? "))
        total, share = calculate_total(bill, tip, people)
        print(f"Total including tip: ₹{total:.2f}")
        print(f"Each person pays: ₹{share:.2f}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
