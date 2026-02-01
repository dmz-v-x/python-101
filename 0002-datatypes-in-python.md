## Python Data Types

### Overview
In Python, **data types** define the kind of value a variable holds and what operations can be performed on it.  
Python is a **dynamically typed language**, which means you don’t need to explicitly declare variable types — they are determined automatically at runtime.

---

### Basic Built-in Data Types

| Data Type | Example Values | Description |
|------------|----------------|-------------|
| **`int`** | `6`, `9`, `-9`, `0` | Represents whole (integer) numbers, positive or negative, without decimals. |
| **`float`** | `2.3`, `4.5`, `0.5`, `-9.8` | Represents real numbers (decimal values). |
| **`str`** | `"hello world"`, `"23r08sdh9d"` | Represents a sequence of characters (text). Strings are enclosed in quotes. |
| **`bool`** | `True`, `False` | Represents Boolean values — either `True` or `False`. |
| **`NoneType`** | `None` | Represents the absence of a value or a null object. |

---

### Example: Basic Data Types

```python
# Integer
a = 6
b = -9

# Float
pi = 3.14
temperature = 36.6

# String
message = "Hello World"
code = "23r08sdh9d"

# Boolean
is_active = True
is_logged_in = False

# NoneType
result = None
```

---

### Printing in Python

To display output in Python, we use the **`print()`** function.

```python
print("Hello World!")
```

**Output:**
```text
Hello World!
```

You can print multiple values as well:

```python
x = 10
y = 5
print("Sum:", x + y)
```

**Output:**
```text
Sum: 15
```

---

### The `type()` Function

The **`type()`** function in Python returns the **data type** of a given object.

### Syntax
```python
type(object)
```

### Example
```python
print(type("True"))      # String
print(type("Hello"))     # String
print(type(2))           # Integer
print(type(2.3))         # Float
print(type(None))        # NoneType
print(type(True))        # Boolean
```

### Output
```text
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'NoneType'>
<class 'bool'>
```

> **Note:** The output format `<class 'typename'>` shows that in Python, everything is an **object** of a specific **class**.

---

### Type Conversion

Python allows you to **convert** between data types using built-in functions such as `int()`, `float()`, and `str()`.

```python
num = "10"

print(int(num))      # Converts string to integer → 10
print(float(num))    # Converts string to float → 10.0
print(str(20))       # Converts integer to string → "20"
```

**Output:**
```text
10
10.0
20
```

---

### Key Takeaways
- Python automatically infers the type of a variable at runtime.  
- Use `type()` to check what data type a value or variable has.  
- Convert between data types using casting functions like `int()`, `float()`, and `str()`.  
- `None` represents the absence of a value — it’s not the same as `0` or `False`.

---

### Practice Exercises
1. Create variables of each type (`int`, `float`, `str`, `bool`, `None`) and print their types.  
2. Convert a string `"100"` into both an integer and a float.  
3. Create a Boolean variable and print its type using the `type()` function.  
4. Experiment with `None` — assign it to a variable and print its type.
