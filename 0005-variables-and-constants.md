## Variables and Constants in Python

## Overview
In Python, **variables** and **constants** are used to store data values that can be used and manipulated throughout your program.  
Python is a **dynamically typed language**, meaning you don’t need to declare variable types explicitly — they are inferred automatically at runtime.

---

### 1. What is a Variable?

A **variable** is a name that refers to a memory location where a value is stored.  
In simple terms, it’s a **container** for storing data.

### Example:
```python
name = "Himanshu"
age = 26
language = "Python"

print(name)
print(age)
print(language)
```

**Output:**
```text
Himanshu
26
Python
```

---

### Rules for Naming Variables

When creating variable names, follow these rules:

✅ Must begin with a **letter** or an **underscore** (`_`)  
✅ Can contain **letters**, **numbers**, and **underscores**  
❌ Cannot start with a **number**  
❌ Cannot use **Python keywords** (`for`, `if`, `class`, etc.)  
✅ Are **case-sensitive** — `Name` and `name` are different  

### Examples:
```python
my_name = "Himanshu"   # ✅ Valid
_age = 25              # ✅ Valid
Name1 = "Python"       # ✅ Valid
1name = "Error"        # ❌ Invalid (starts with number)
for = "loop"           # ❌ Invalid (reserved keyword)
```

---

### 2. Variable Assignment

Variables can hold different data types (int, float, str, etc.), and Python automatically assigns the type based on the value.

```python
x = 10          # Integer
y = 3.14        # Float
name = "John"   # String
is_active = True  # Boolean
```

You can check the type of a variable using the **`type()`** function:

```python
print(type(x))
print(type(y))
print(type(name))
print(type(is_active))
```

**Output:**
```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

### 3. Multiple Assignments

Python allows assigning values to multiple variables in one line.

```python
a, b, c = 5, 10, 15
print(a, b, c)
```

**Output:**
```text
5 10 15
```

You can also assign the **same value** to multiple variables at once:

```python
x = y = z = 100
print(x, y, z)
```

**Output:**
```text
100 100 100
```

---

### 4. Constants in Python

Python doesn’t have a built-in constant type like some other languages (e.g., `const` in C++ or Java).  
However, **by convention**, constants are written in **uppercase letters** to indicate that their value **should not be changed**.

### Example:
```python
PI = 3.14159
MAX_USERS = 100
APP_NAME = "MyApp"

print(PI)
print(MAX_USERS)
print(APP_NAME)
```

Although you *can* technically reassign these values, it is **not recommended**.

```python
PI = 3.14  # ⚠️ Not good practice — constants should not change
```

---

### 5. Dynamic Typing

Python allows you to change the data type of a variable during execution.

```python
x = 10
print(type(x))  # int

x = "Hello"
print(type(x))  # str
```

**Output:**
```text
<class 'int'>
<class 'str'>
```

**Explanation:**  
Python variables are **dynamically typed**, meaning their type can change when you assign a new value.

---

### 6. Deleting Variables

You can delete a variable using the **`del`** keyword.

```python
x = 10
print(x)
del x
# print(x)  # ❌ This will cause an error: NameError: name 'x' is not defined
```

---

### Summary

| Concept | Description | Example |
|----------|--------------|----------|
| Variable | A container to store data | `x = 10` |
| Constant | A value that should not change (by convention) | `PI = 3.14` |
| Multiple Assignment | Assign multiple values in one line | `a, b = 5, 10` |
| Same Value Assignment | Assign same value to many variables | `x = y = 100` |
| Dynamic Typing | Variable type can change at runtime | `x = 10; x = "Hello"` |

---

### Complete Example

```python
# Variables
name = "Himanshu"
age = 26
language = "Python"

# Constants (by convention)
PI = 3.14159
MAX_USERS = 100

# Multiple assignment
x, y, z = 10, 20, 30

# Printing values
print(f"Name: {name}, Age: {age}, Language: {language}")
print("PI:", PI)
print("Max Users:", MAX_USERS)
print("Values:", x, y, z)
```

**Output:**
```text
Name: Himanshu, Age: 26, Language: Python
PI: 3.14159
Max Users: 100
Values: 10 20 30
```

---

### Practice Exercises

1. Create variables `name`, `age`, and `city` and print them using an f-string.  
2. Define constants `PI` and `GRAVITY`, print them, and try changing their values.  
3. Assign values to multiple variables in one line and print them.  
4. Check the data type of each variable using `type()`.  
5. Try deleting a variable using `del` and observe the error message when you print it again.

---

**Key Takeaway:**  
Variables store data that can change, while constants hold data that *should not* change.  
Python is dynamically typed — flexible and simple to use for all kinds of programming tasks.
