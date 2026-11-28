# Python file handling

Python can read and write files with the built-in `open()` function. Prefer the `with` statement because it closes the file automatically.

## Write to a file

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python is fun!\n")
```

## Read a file

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

## Add more text

Use append mode (`"a"`) to add content without replacing what is already there.

## Common modes

- `"r"`: read an existing file
- `"w"`: write, replacing existing content
- `"a"`: append to the end
- `"x"`: create a new file and fail if it already exists

Use `encoding="utf-8"` for predictable text handling.
