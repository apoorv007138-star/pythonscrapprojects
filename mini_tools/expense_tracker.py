"""Track expenses during one run of the program."""
def main():
    expenses = []
    print("Expense Tracker — enter 'done' when finished.")
    while True:
        name = input("Expense name: ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Please enter a name.")
            continue
        try:
            amount = float(input("Amount: ₹"))
            if amount < 0:
                raise ValueError
        except ValueError:
            print("Enter a valid non-negative amount.")
            continue
        expenses.append((name, amount))

    print("\nYour expenses:")
    for name, amount in expenses:
        print(f"- {name}: ₹{amount:.2f}")
    print(f"Total: ₹{sum(amount for _, amount in expenses):.2f}")

if __name__ == "__main__":
    main()
