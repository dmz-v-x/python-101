## Comments in Python

### Overview
**Comments** in Python are lines in the code that the **interpreter ignores** while executing a program.  
They are used to:
- Explain what the code does  
- Improve readability 
- Help other developers (and your future self) understand the logic  

Comments are an essential part of **writing clean and maintainable code**.

---

### Types of Comments in Python

### 1. Single-line Comments

A **single-line comment** starts with a hash symbol (`#`).  
Everything after the `#` on that line is ignored by Python.

```python
# This is a single-line comment
print("Hello, World!")  # This is an inline comment
```

**Explanation:**
- `# This is a single-line comment` → Comment before code  
- `print("Hello, World!")  # This is an inline comment` → Comment after code on the same line  

---

### 2. Multi-line Comments (Using #)

Python doesn’t have a dedicated multi-line comment syntax (like `/* ... */` in other languages).  
Instead, you can use **multiple single-line comments** one after another.

```python
# This is a multi-line comment
# explaining what the following
# block of code does.

print("Learning Python Comments")
```

**Explanation:**  
Each line starts with a `#`, but together they form a readable paragraph-style comment.

---

### 3. Multi-line Comments (Using Triple Quotes)

You can also use **triple quotes (`'''` or `"""`)** for multi-line comments.  
These are technically **multi-line strings**, but if they are **not assigned to a variable or used as a docstring**, Python ignores them — effectively treating them as comments.

```python
'''
This is a multi-line comment
using triple single quotes.
It is not assigned to a variable,
so Python will ignore it.
'''

"""
This is another multi-line comment
using triple double quotes.
"""
```

**Note:**  
While this works, it’s generally **recommended** to use `#` for comments, and reserve triple quotes for **docstrings**.

---

### 4. Inline Comments

An **inline comment** appears **on the same line as code**, usually explaining that specific line.

```python
x = 10  # Assigning 10 to variable x
y = 20  # Assigning 20 to variable y
sum = x + y  # Adding x and y
print(sum)  # Output will be 30
```

**Best Practice:**  
Leave at least **two spaces** between code and the start of the inline comment.

---

### 5. Docstrings (Documentation Strings)

**Docstrings** are **special multi-line strings** used to document modules, classes, functions, or methods.  
They describe what the function/class/module does.

They are defined using **triple quotes** (`'''` or `"""`) immediately **below a function, class, or module definition**.

```python
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

class Calculator:
    """A simple calculator class."""
    pass
```

You can access a function or class docstring using the `__doc__` attribute:

```python
print(add.__doc__)
```

**Output:**
```text
This function returns the sum of two numbers.
```

---

### Summary

| Type | Symbol / Syntax | Description |
|------|------------------|--------------|
| Single-line | `#` | For short explanations or quick notes |
| Multi-line (#) | Multiple `#` lines | For block-style explanations |
| Multi-line (quotes) | `'''...'''` or `"""..."""` | For ignored multi-line strings |
| Inline | `code  # comment` | Comments on the same line as code |
| Docstring | `"""..."""` below a def/class | For documentation, accessible via `__doc__` |

---

### Example: All Comment Types Together

```python
# This program demonstrates different types of comments

'''
This is a multi-line comment using triple quotes.
It explains the following block of code.
'''

def greet(name):
    """Function to greet a person by name."""
    print("Hello,", name)  # Inline comment

# Calling the function
greet("Python Learner")
```

**Output:**
```text
Hello, Python Learner
```

---

### Best Practices

✅ Use comments to **explain why** code exists — not just what it does.  
✅ Keep comments **short, clear, and meaningful**.  
✅ Update comments if you change the code.  
✅ Use **docstrings** for documenting modules, classes, and functions.  
✅ Avoid over-commenting — clean, self-explanatory code needs fewer comments.

---

### Practice Exercises

1. Write a function that multiplies two numbers and use a **docstring** to describe it.  
2. Add **inline comments** explaining each step in your function.  
3. Create a **multi-line comment** that explains the purpose of your script at the top of the file.

---

**Key Takeaway:**  
Comments are ignored by Python but **valued by developers**.  
Good comments make your code **easier to understand, maintain, and debug**.
