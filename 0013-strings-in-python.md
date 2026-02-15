## Strings in Python

A **string** in Python is a sequence of characters.  
Strings are **immutable**, meaning once created, their content cannot be changed.  
They can be created using **single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`)**.

---

## 1. Creating Strings

```python
string1 = 'Hello, Python!'
string2 = "Hello, World!"
string3 = '''This is a
multi-line string'''
```

---

## 2. Strings are Immutable

```python
s = "Hello"
s[0] = 'h'  # ❌ Error: strings cannot be modified
```

---

## 3. Ordered (Indexable)

```python
s = "Python"
print(s[0])   # Output: 'P'
print(s[-1])  # Output: 'n'
```

---

## 4. Heterogeneous Collection

```python
s = "Hello123!@#"
```

A string can contain **letters, digits, and special characters**.

---

## 5. Iterable

```python
s = "Python"
for char in s:
    print(char)
# Output: P y t h o n (each on a new line)
```

---

## 6. Common String Methods

### `len()`
Returns the length of the string.

```python
s = "Python"
print(len(s))  # Output: 6
```

---

### `upper()` / `lower()`
Converts the string to uppercase or lowercase.

```python
s = "python"
print(s.upper())  # 'PYTHON'
print(s.lower())  # 'python'
```

---

### `capitalize()` / `title()`
Capitalizes the first letter or every word.

```python
s = "hello python world"
print(s.capitalize())  # 'Hello python world'
print(s.title())       # 'Hello Python World'
```

---

### `strip()`, `lstrip()`, `rstrip()`
Removes whitespace from both sides or one side.

```python
s = " Hello, World! "
print(s.strip())   # 'Hello, World!'
print(s.lstrip())  # 'Hello, World! '
print(s.rstrip())  # ' Hello, World!'
```

---

### `replace(old, new)`
Replaces part of a string with another.

```python
s = "Hello, World!"
print(s.replace("World", "Python"))  # 'Hello, Python!'
```

---

### `split(delimiter)`
Splits a string into a list based on a delimiter.

```python
s = "apple,orange,banana"
print(s.split(","))  # ['apple', 'orange', 'banana']
```

---

### `join(iterable)`
Joins list elements into a single string.

```python
fruits = ['apple', 'orange', 'banana']
print(", ".join(fruits))  # 'apple, orange, banana'
```

---

### `find(substring)`
Finds the index of a substring. Returns `-1` if not found.

```python
s = "Hello, Python!"
print(s.find("Python"))  # 7
print(s.find("Java"))    # -1
```

---

### `count(substring)`
Counts occurrences of a substring.

```python
s = "banana"
print(s.count("a"))  # 3
```

---

### `startswith()` / `endswith()`
Checks if a string starts or ends with a given substring.

```python
s = "Hello, World!"
print(s.startswith("Hello"))  # True
print(s.endswith("World!"))   # True
```

---

### `isalpha()`, `isdigit()`, `isnumeric()`
Checks the type of characters in the string.

```python
s = "Python"
print(s.isalpha())  # True

s = "12345"
print(s.isdigit())  # True

s = "123456"
print(s.isnumeric())  # True
```

---

### `islower()` / `isupper()`
Checks if all characters are lowercase or uppercase.

```python
s = "hello"
print(s.islower())  # True

s = "HELLO"
print(s.isupper())  # True
```

---

### `format()`
Used to format strings with placeholders.

```python
name = "John"
age = 25
greeting = "My name is {} and I am {} years old.".format(name, age)
print(greeting)  # My name is John and I am 25 years old.

# Using named placeholders
greeting = "My name is {name} and I am {age} years old.".format(name="Alice", age=30)
print(greeting)  # My name is Alice and I am 30 years old.
```

---

### `swapcase()`
Swaps case of each character.

```python
s = "Hello World"
print(s.swapcase())  # 'hELLO wORLD'
```

---

## 7. String Slicing

You can extract parts (substrings) using slicing.

```python
s = "Hello, Python!"
print(s[0:5])   # 'Hello'
print(s[7:])    # 'Python!'
print(s[::-1])  # '!nohtyP ,olleH'
```

---

## 8. Escape Sequences

| Escape | Description |
|:-------|:-------------|
| `\n`   | Newline |
| `\t`   | Tab |
| `\\`   | Backslash |
| `\'`   | Single quote |
| `\"`   | Double quote |

Example:

```python
print("Hello\nPython")  # New line
print("Hello\tPython")  # Tab space
print("He said, \"Python is fun!\"")
```

---

**Summary**
- Strings are **immutable** and **ordered**.
- You can perform many operations like slicing, joining, formatting, and case conversions.
- They are **one of the most powerful data types** in Python used everywhere in text processing.
