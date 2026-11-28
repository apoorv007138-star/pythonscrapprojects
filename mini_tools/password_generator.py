"""Generate random passwords using Python's secrets module."""
import secrets
import string

def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))

def main():
    try:
        length = int(input("Password length (minimum 4): "))
        print("Generated password:", generate_password(length))
    except ValueError as error:
        print("Invalid input:", error)

if __name__ == "__main__":
    main()
