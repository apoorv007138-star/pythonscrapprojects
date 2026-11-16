"""Generate a random password using Python's secrets module."""
import secrets
import string


def generate_password(length=16, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+?"

    # Ensure the password includes a mix of character categories.
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if use_symbols:
        required.append(secrets.choice("!@#$%^&*()-_=+?"))

    remaining = [secrets.choice(characters) for _ in range(length - len(required))]
    password = required + remaining
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    try:
        size = int(input("Password length (minimum 4): "))
        symbols = input("Include symbols? (Y/n): ").strip().lower() != "n"
        print("Generated password:", generate_password(size, symbols))
    except ValueError as error:
        print("Error:", error)
