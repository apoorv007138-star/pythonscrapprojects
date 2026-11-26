"""Convert temperatures between Celsius, Fahrenheit, and Kelvin."""

def convert(value, source, target):
    source, target = source.upper(), target.upper()
    to_celsius = {
        "C": lambda x: x,
        "F": lambda x: (x - 32) * 5 / 9,
        "K": lambda x: x - 273.15,
    }
    from_celsius = {
        "C": lambda x: x,
        "F": lambda x: x * 9 / 5 + 32,
        "K": lambda x: x + 273.15,
    }
    if source not in to_celsius or target not in from_celsius:
        raise ValueError("Units must be C, F, or K.")
    return from_celsius[target](to_celsius[source](value))


def main():
    try:
        value = float(input("Temperature value: "))
        source = input("Convert from (C/F/K): ")
        target = input("Convert to (C/F/K): ")
        print(f"Result: {convert(value, source, target):.2f} {target.upper()}")
    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
