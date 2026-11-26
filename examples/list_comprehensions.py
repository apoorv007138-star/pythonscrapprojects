"""Small, runnable examples of Python list comprehensions."""

numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]
evens = [number for number in numbers if number % 2 == 0]
labels = ["even" if number % 2 == 0 else "odd" for number in numbers]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", evens)
print("Labels:", labels)
