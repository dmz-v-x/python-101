## Different Ways of Printing in Python

### Overview
The **`print()`** function in Python is one of the most commonly used functions.  
It allows you to **display output** on the console.  
Python offers multiple ways to print text, variables, and formatted data.

---

### 1. Basic Print Statement

The simplest way to print something is to use `print()` with a string.

```python
print("Hello World")
```

**Output:**
```text
Hello World
```

---

### 2. Printing Multiple Values

You can print multiple values separated by commas inside the `print()` function.

```python
name = "Himanshu"
age = 26
print("Name:", name, "Age:", age)
```

**Output:**
```text
Name: Himanshu Age: 26
```

💡 **Tip:**  
Python automatically inserts a space between multiple arguments separated by commas.

---

### 3. Using the `sep` (Separator) Parameter

The `sep` parameter in `print()` defines how multiple values are separated.

### Example:
```python
print("python", "is", "easy", sep="-")
print("python", "is", "easy", sep="_")
```

**Output:**
```text
python-is-easy
python_is_easy
```

**Explanation:**
- By default, `print()` separates values using a space.
- Using `sep` allows you to customize the separator character.

---

### 4. Using the `end` Parameter

The `end` parameter specifies what to print **at the end** of a statement.  
By default, `print()` adds a **newline (`\n`)** at the end, moving to the next line.  
You can change it using the `end` parameter.

### Example:
```python
print("Hello", end=" ")
print("World")
```

**Output:**
```text
Hello World
```

**Explanation:**  
Instead of moving to the next line after printing “Hello”, the `end=" "` parameter adds a space — so “World” prints on the same line.

---

### 5. Using Formatted Strings (f-Strings)

**f-Strings** (introduced in Python 3.6) provide an elegant way to insert variables directly inside strings.

### Example:
```python
name = "Himanshu"
age = 26
print(f"Name: {name}, Age: {age}")
```

**Output:**
```text
Name: Himanshu, Age: 26
```

**Explanation:**
- Prefix the string with **`f`**.
- Variables inside `{}` are replaced by their actual values.

---

### 6. Using the `str.format()` Method

Before f-Strings, the `.format()` method was used for formatted printing.

### Example:
```python
name = "Himanshu"
age = 26
print("Name: {0}, Age: {1}".format(name, age))
```

**Output:**
```text
Name: Himanshu, Age: 26
```

**Explanation:**
- `{0}` and `{1}` are placeholders replaced by the corresponding arguments passed to `.format()`.

---

### Summary

| Method | Example | Description |
|---------|----------|-------------|
| Basic print | `print("Hello World")` | Prints a simple message |
| Multiple values | `print("Name:", name, "Age:", age)` | Prints multiple values separated by spaces |
| `sep` parameter | `print("A", "B", sep="-")` | Custom separator between printed values |
| `end` parameter | `print("Hello", end=" ")` | Custom string appended at the end |
| f-String | `print(f"Name: {name}")` | Easiest and most modern way to format strings |
| `.format()` | `print("Name: {0}".format(name))` | Older string formatting method |

---

### Complete Example

```python
print("Hello World")

# Printing multiple values
name = "Himanshu"
age = 26
print("Name:", name, "Age:", age)

# Using separator
print("python", "is", "easy", sep="-")
print("python", "is", "easy", sep="_")

# Using end parameter
print("Hello", end=" ")
print("World")

# Formatted strings
print(f"Name: {name}, Age: {age}")
print("Name: {0}, Age: {1}".format(name, age))
```

**Output:**
```text
Hello World
Name: Himanshu Age: 26
python-is-easy
python_is_easy
Hello World
Name: Himanshu, Age: 26
Name: Himanshu, Age: 26
```

---

### Practice Exercises

1. Print your name and hobby in one line using the `sep` parameter.  
2. Use the `end` parameter to print two sentences on the same line.  
3. Print your name, age, and city using an f-string.  
4. Try the same using `.format()` method and compare both outputs.

---

**Key Takeaway:**  
The `print()` function is versatile — from basic output to advanced formatted strings, it’s a powerful tool for displaying information in Python.
