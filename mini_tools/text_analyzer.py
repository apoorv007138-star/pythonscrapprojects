"""Print basic statistics about text entered by the user."""

def analyze(text):
    words = text.split()
    return {
        "characters": len(text),
        "characters_without_spaces": len("".join(text.split())),
        "words": len(words),
        "sentences": sum(text.count(mark) for mark in ".!?"),
    }


def main():
    text = input("Enter a sentence or paragraph: ")
    for label, value in analyze(text).items():
        print(f"{label.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()
