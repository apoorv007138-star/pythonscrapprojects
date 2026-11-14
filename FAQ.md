# Python FAQs (Frequently Asked Questions)

A beginner-friendly collection of common Python questions, with simple explanations and examples.

## 1. What is Python?

Python is a high-level, general-purpose programming language. It is popular because its syntax is readable and it is used in web development, automation, data science, artificial intelligence, and scripting.

## 2. Is Python free to use?

Yes. Python is open-source and free to download, use, and distribute.

## 3. How do I install Python?

1. Visit [python.org/downloads](https://www.python.org/downloads/).
2. Download the version for your operating system.
3. Run the installer.
4. On Windows, select **Add Python to PATH** before installing.
5. Open a terminal and check the installation:

```bash
python --version
```

On some systems, use `python3 --version`.

## 4. How do I run a Python file?

Save your code in a file ending in `.py`, such as `hello.py`, then run:

```bash
python hello.py
```

On some systems, use `python3 hello.py`.

## 5. Do I need a semicolon at the end of every Python statement?

No. Python normally uses a new line to separate statements. Semicolons are optional and rarely needed.

## 6. What is indentation in Python?

Indentation means the spaces at the beginning of a line. Python uses indentation to define blocks of code, such as the body of an `if` statement or a loop.

```python
if age >= 18:
    print("You are an adult")
```

The indented line belongs to the `if` block.

## 7. What are variables?

Variables are names used to store values.

```python
name = "Apoorv"
age = 18
marks = 92.5
```

Python determines the type of a variable from the value assigned to it.

## 8. What are the basic data types in Python?

Common built-in types include:

- `int`: whole numbers, such as `10`
- `float`: decimal numbers, such as `3.14`
- `str`: text, such as `"Hello"`
- `bool`: `True` or `False`
- `list`: ordered, changeable collection
- `tuple`: ordered, unchangeable collection
- `set`: collection of unique values
- `dict`: key-value pairs

## 9. What is the difference between a list and a tuple?

A list can be changed after it is created. A tuple cannot be changed after creation.

```python
my_list = [1, 2, 3]
my_list.append(4)

my_tuple = (1, 2, 3)
```

## 10. What is the difference between = and ==?

- `=` assigns a value to a variable.
- `==` checks whether two values are equal.

```python
score = 10       # assignment
print(score == 10)  # comparison: True
```

## 11. What are conditional statements?

Conditional statements let a program make decisions. Python uses `if`, `elif`, and `else`.

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Keep practising")
```

## 12. What is a loop?

A loop repeats a block of code.

A `for` loop is commonly used to iterate over a sequence or range:

```python
for number in range(1, 4):
    print(number)
```

A `while` loop repeats while its condition is true:

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

## 13. What does range() do?

`range()` generates a sequence of integers, commonly used with `for` loops. The stop value is not included.

```python
for number in range(1, 5):
    print(number)  # 1, 2, 3, 4
```

## 14. What is a function?

A function is a reusable block of code. Define one with `def` and call it by using its name.

```python
def greet(name):
    print("Hello", name)

greet("Apoorv")
```

## 15. What does return do?

`return` sends a result back from a function. It is different from `print()`, which displays something on the screen.

```python
def add(a, b):
    return a + b

result = add(4, 5)
print(result)  # 9
```

## 16. What is the difference between break and continue?

- `break` immediately exits the nearest loop.
- `continue` skips the rest of the current iteration and moves to the next one.

## 17. What is a comment in Python?

A comment is text in the code that Python ignores when running the program. A single-line comment starts with `#`.

```python
# This is a comment
print("Hello, Python!")
```

## 18. What is a module?

A module is a Python file containing code—such as functions and variables—that can be reused in another file. You can load a module with `import`.

```python
import math

print(math.sqrt(25))
```

## 19. What is pip?

`pip` is Python's package installer. It can install third-party libraries.

```bash
python -m pip install requests
```

## 20. What is a virtual environment?

A virtual environment keeps the packages for one project separate from other Python projects.

Create one:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\\Scripts\\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

## 21. What is an exception?

An exception is an error that occurs while a program is running. Use `try` and `except` to handle expected errors.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

## 22. What is a dictionary?

A dictionary stores information as key-value pairs.

```python
student = {
    "name": "Apoorv",
    "marks": 92
}

print(student["name"])
```

## 23. How do I take input from a user?

Use `input()`. It returns text, so convert it when you need a number.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old.")
```

## 24. What is a string?

A string is a sequence of characters used to represent text. Strings can be written using single or double quotes.

```python
message = "Learning Python is fun!"
print(message.upper())
```

## 25. How do I read or write a file?

Use `open()`. The `with` statement closes the file automatically when the block ends.

```python
# Write to a file
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")

# Read from a file
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

## 26. What are common Python errors?

- `SyntaxError`: code does not follow Python's syntax rules.
- `NameError`: a name has not been defined.
- `TypeError`: an operation is used with an inappropriate type.
- `ValueError`: a value has the right general type but is not acceptable.
- `IndexError`: a sequence index is out of range.
- `KeyError`: a dictionary key does not exist.

Read the final line of the traceback first to identify the error type, then check the line number shown.

## 27. Is Python case-sensitive?

Yes. `name`, `Name`, and `NAME` are treated as different names.

## 28. What is None in Python?

`None` represents the absence of a value. It is not the same as `0`, `False`, or an empty string.

## 29. What is object-oriented programming (OOP)?

OOP is a programming approach based on classes and objects. A class defines a structure and behaviour; an object is an instance of that class.

```python
class Student:
    def __init__(self, name):
        self.name = name

student = Student("Apoorv")
print(student.name)
```

## 30. Where can I practise Python?

Try writing small programs such as:
- A calculator
- A number guessing game
- A to-do list
- An expense tracker
- A quiz application

Practise one concept at a time, run your code, and experiment with changing it.

---

## Quick learning tip

If you are new to Python, learn in this order: variables and data types → input/output → conditions → loops → functions → collections → files and exceptions → modules and OOP.

*Examples are written for Python 3.*
