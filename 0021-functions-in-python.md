## Functions in Python

A **function** in Python is a **block of reusable code** designed to perform a specific task.  
Functions help make programs:

- More **organized**
- Easier to **read**
- Easier to **maintain**
- Less **repetitive**

A function can:
- Take **input** (parameters)
- **Process** that input
- Return **output**

---

## Types of Functions in Python

### 1. Built-in Functions
Python provides many built-in functions such as:
- `print()`
- `len()`
- `type()`
- `sum()`
- `range()`

```python
print(len("Python"))
```

---

### 2. User-Defined Functions
Functions that **we define ourselves** using the `def` keyword.

---

## Why Use Functions?

| Benefit | Explanation |
|------|-------------|
| Reusability | Write once, use many times |
| Modularity | Break large programs into small pieces |
| Maintainability | Easy to update or fix code |
| Readability | Code becomes self-explanatory |

---

## 1. Defining a Function

### Syntax

```python
def function_name(parameters):
    """Optional docstring"""
    # function body
    return value  # optional
```

- `def` → keyword to define a function
- `parameters` → input variables
- `return` → sends result back to caller

---

## 2. Simple Function Example

```python
def greet():
    """This function prints a greeting message"""
    print("Hello, welcome to Python functions!")

greet()
```

**Output:**
```text
Hello, welcome to Python functions!
```

---

## 3. Parameters and Arguments

- **Parameters** → variables in function definition
- **Arguments** → values passed during function call

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

**Output:**
```text
Hello, Alice!
```

---

## 4. Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

**Output:**
```text
15
```

---

## 5. `return` Statement

The `return` statement sends a value back to the caller and **ends the function execution**.

```python
def square(x):
    return x * x

print(square(4))
```

**Output:**
```text
16
```

---

## 6. Default Parameters

Default values are used when arguments are not provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Charlie")
```

**Output:**
```text
Hello, Guest!
Hello, Charlie!
```

---

## 7. Keyword Arguments

Arguments can be passed using parameter names (order doesn’t matter).

```python
def person_info(name, age):
    print(f"Name: {name}, Age: {age}")

person_info(age=25, name="Bob")
```

**Output:**
```text
Name: Bob, Age: 25
```

---

## 8. Variable-Length Arguments

### `*args` → Variable Number of Positional Arguments

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
```

**Output:**
```text
15
```

---

### `**kwargs` → Variable Number of Keyword Arguments

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

**Output:**
```text
name: Alice
age: 30
city: New York
```

---

## 9. Scope of Variables

### Local vs Global Variables

```python
x = 10  # Global

def local_scope():
    x = 5  # Local
    print(f"Inside function: {x}")

local_scope()
print(f"Outside function: {x}")
```

**Output:**
```text
Inside function: 5
Outside function: 10
```

---

### Modifying Global Variables

```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)
```

**Output:**
```text
20
```

---

## 10. Anonymous Functions (`lambda`)

A **lambda function** is a small unnamed function with a single expression.

```python
square = lambda x: x * x
print(square(5))

add = lambda a, b: a + b
print(add(3, 4))
```

**Output:**
```text
25
7
```

---

## 11. Higher-Order Functions

Functions that:
- Accept other functions as arguments
- Return functions

```python
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x * 2, 5))
```

**Output:**
```text
10
```

---

## 12. Recursive Functions

A function that **calls itself**.

Must have a **base condition** to avoid infinite recursion.

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

**Output:**
```text
120
```

---

## 13. `pass` in Functions

Used as a placeholder when implementation is pending.

```python
def my_function():
    pass
```

---

## 14. Nested Functions

Functions can exist **inside other functions**.

```python
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()

outer_function()
```

**Output:**
```text
This is the outer function.
This is the inner function.
```

---

## 15. Closures

A **closure** remembers variables from its enclosing scope.

```python
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hello_func = outer_function("Hello")
hello_func()
```

**Output:**
```text
Hello
```

---

## Common Mistakes & Errors

| Mistake | Reason |
|------|-------|
| Forgetting `return` | Function returns `None` |
| Modifying globals unnecessarily | Causes side effects |
| Infinite recursion | Missing base case |
| Overusing lambdas | Reduces readability |
| Large functions | Hard to debug |

---

## Summary

| Concept | Description |
|------|-------------|
| Functions | Reusable blocks of code |
| Parameters | Inputs to functions |
| Arguments | Values passed |
| `return` | Sends output back |
| `*args`, `**kwargs` | Variable arguments |
| Scope | Local vs global |
| Lambda | One-line anonymous functions |
| Recursion | Function calling itself |
| Closures | Functions remembering outer scope |

---

## Practice Tasks

1. Write a function to check if a number is even or odd.  
2. Create a function that returns the maximum of three numbers.  
3. Write a recursive function to calculate Fibonacci numbers.  
4. Use `*args` to calculate the product of numbers.  
5. Create a closure that remembers a counter value.  
