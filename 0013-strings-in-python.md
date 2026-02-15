# Strings in Python

A **string** in Python is a sequence of characters.  
Strings are **immutable**, meaning once created, their content cannot be changed.  
They can be created using **single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`)**.

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
s[0] = 'h'  # ❌ TypeError: 'str' object does not support item assignment
```

**Note:** To "change" a string you must create a new one:
```python
s = "Hello"
s = "h" + s[1:]  # 'hello'
```

---

## 3. Ordered (Indexable)

```python
s = "Python"
print(s[0])   # Output: 'P'
print(s[-1])  # Output: 'n'
```

Accessing an index that doesn't exist raises `IndexError`:
```python
# print(s[100])  # IndexError: string index out of range
```

---

## 4. Heterogeneous Characters

```python
s = "Hello123!@#"
```

Strings can contain letters, digits, punctuation, whitespace and special characters.

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
```python
s = "Python"
print(len(s))  # Output: 6
```

### `upper()` / `lower()`
```python
s = "python"
print(s.upper())  # 'PYTHON'
print(s.lower())  # 'python'
```

### `capitalize()` / `title()`
```python
s = "hello python world"
print(s.capitalize())  # 'Hello python world'
print(s.title())       # 'Hello Python World'
```

### `strip()`, `lstrip()`, `rstrip()`
```python
s = " Hello, World! "
print(s.strip())   # 'Hello, World!'
print(s.lstrip())  # 'Hello, World! '
print(s.rstrip())  # ' Hello, World!'
```

### `replace(old, new)`
```python
s = "Hello, World!"
print(s.replace("World", "Python"))  # 'Hello, Python!'
```

### `split(delimiter)`
```python
s = "apple,orange,banana"
print(s.split(","))  # ['apple', 'orange', 'banana']
```

### `join(iterable)`
```python
fruits = ['apple', 'orange', 'banana']
print(", ".join(fruits))  # 'apple, orange, banana'
```

### `find(substring)`
```python
s = "Hello, Python!"
print(s.find("Python"))  # 7
print(s.find("Java"))    # -1
```

### `count(substring)`
```python
s = "banana"
print(s.count("a"))  # 3
```

### `startswith()` / `endswith()`
```python
s = "Hello, World!"
print(s.startswith("Hello"))  # True
print(s.endswith("World!"))   # True
```

### `isalpha()`, `isdigit()`, `isnumeric()`
```python
print("Python".isalpha())   # True
print("12345".isdigit())    # True
print("123456".isnumeric()) # True
```

### `islower()` / `isupper()`
```python
print("hello".islower())  # True
print("HELLO".isupper())  # True
```

### `format()` and f-strings
```python
name = "John"; age = 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
```

### `swapcase()`
```python
print("Hello World".swapcase())  # 'hELLO wORLD'
```

---

## 7. String Slicing

Syntax: `string[start:stop:step]`
```python
s = "Hello, Python!"
print(s[0:5])   # 'Hello'
print(s[7:])    # 'Python!'
print(s[::-1])  # '!nohtyP ,olleH'
```

---

## 8. Escape Sequences

| Escape | Meaning |
|:------:|:--------|
| `\n`   | Newline |
| `\t`   | Tab |
| `\\`   | Backslash |
| `\'`   | Single quote |
| `\"`   | Double quote |

```python
print("Hello\nPython")
print("He said, \"Python is fun!\"")
```

---

## 9. Encoding / Decoding (brief)

Converting between `str` (text) and `bytes` requires encoding/decoding:

```python
s = "café"
b = s.encode("utf-8")    # bytes
print(b)                 # b'caf\xc3\xa9'
print(b.decode("utf-8")) # 'café'
```

Mistakes in encoding/decoding can raise `UnicodeEncodeError` or `UnicodeDecodeError`.

---

## 10. Common Errors & Why They Happen

1. **`TypeError: 'str' object does not support item assignment`**  
   - Cause: Trying to change a character via index (`s[0] = 'h'`) — strings are immutable.  
   - Fix: Build a new string (`s = 'h' + s[1:]`).

2. **`IndexError: string index out of range`**  
   - Cause: Accessing `s[i]` where `i` is outside `0 .. len(s)-1`.  
   - Fix: Check `len(s)` or use slicing which is safe (e.g., `s[0:100]`).

3. **`AttributeError: 'NoneType' object has no attribute 'upper'`**  
   - Cause: Calling a string method on a variable that is `None` (e.g., `s = None; s.upper()`).  
   - Fix: Ensure the variable is a string before calling methods (`if s is not None:`).

4. **`TypeError: can only concatenate str (not "int") to str`**  
   - Cause: Trying to `+` a `str` and a non-str (e.g., `"Age: " + 25`).  
   - Fix: Convert with `str(25)` or use f-strings: `f"Age: {25}"`.

5. **`ValueError` when converting strings to numbers**  
   - Example: `int("abc")` raises `ValueError`.  
   - Fix: Validate or handle with `try/except`.

6. **`UnicodeEncodeError` / `UnicodeDecodeError`**  
   - Cause: Wrong encoding during `.encode()` or `.decode()` or when writing/reading files.  
   - Fix: Use the correct encoding (e.g., `"utf-8"`) consistently.

7. **Unexpected results due to invisible characters**  
   - Cause: Strings may contain whitespace, non-printable characters, or different newline conventions.  
   - Fix: Use `.strip()` / `repr()` / `ord()` to inspect and clean strings.

---

## 11. Performance Note

Repeated string concatenation in large loops can be inefficient (strings are immutable). For heavy concatenation, prefer:

- Building a list and `''.join(list_of_parts)`  
- Using `io.StringIO` for very large dynamic building

Example (inefficient):
```python
s = ""
for i in range(10000):
    s += str(i)  # creates many intermediate strings
```

Efficient alternative:
```python
parts = []
for i in range(10000):
    parts.append(str(i))
s = "".join(parts)
```

---

## 12. Practice Tasks

1. **Index & slicing**
   - Given `s = "PythonRocks"`, print:
     - First character
     - Last character
     - Substring `"thonR"`
     - Reversed string

2. **Immutable update**
   - Convert `"Hello"` to `"hELLO"` using slicing and concatenation.

3. **Parsing**
   - Given `"name:age:city" = "Alice:30:Paris"`, split into variables and print an f-string: `Alice is 30 and lives in Paris`.

4. **Validation**
   - Write a function `is_valid_username(s)` that returns `True` if `s`:
     - is 3–16 characters long,
     - contains only letters and digits,
     - starts with a letter.

5. **Counting**
   - Count vowels in a string (both uppercase & lowercase) and print counts for each vowel.

6. **Safe conversion**
   - Write a function `to_int(s)` that tries to convert `s` to `int` and returns `None` if conversion fails (handle exceptions).

7. **Encoding**
   - Read a Unicode string with accents (e.g., `"café"`) and show its UTF-8 byte representation and back.

8. **Performance**
   - Create a list of 10,000 small strings and join them into one string. Measure (optionally) the difference between repeated `+=` vs list + `join`.

---

## Summary

- Strings are **immutable**, **ordered**, and **iterable**.  
- Use slicing, built-in methods (`split`, `join`, `replace`, etc.) for manipulation and parsing.  
- Watch for common errors: `TypeError` (mutation/concatenation), `IndexError`, `AttributeError`, `ValueError`, and Unicode errors.  
- For heavy concatenation, build parts and use `join()`.
