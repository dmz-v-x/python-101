## Reading User Input in Python

In Python, **user input** allows programs to interact with users at runtime.  
Python reads input from the user using the built-in `input()` function.

**Important Rule:**  
`input()` **always returns a string**, even if the user types numbers.

---

## Basic Input Function

```python
input(prompt)
```

- `prompt` → Message shown to the user
- Return type → `str`

---

## 1. Basic Input Example

```python
name = input("Enter your name: ")
print(f"Hello, {name}")
```

**Sample Input:**
```text
Himanshu
```

**Output:**
```text
Hello, Himanshu
```

---

## 2. Converting Input to Other Data Types

Since `input()` returns a string, you must **explicitly convert** it.

---

### Converting Input to Integer

```python
age = int(input("Enter your age: "))
print(age)
```

If the user enters non-numeric input → `ValueError`

---

## 3. Input Validation with `try-except`

```python
try:
    age = int(input("Enter your age: "))
    while age < 1 or age > 120:
        print("Please enter a valid age between (1 - 120)")
        age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
```

---

### Why This Works

- Prevents program crash
- Re-prompts user until valid input
- Handles both **type errors** and **range errors**

---

## 4. Multiple Inputs Using `split()`

### Space-Separated Input

```python
name, age = input("Enter your name and age (space-separated): ").split()
print(f"Name: {name}, Age: {age}")
```

**Input:**
```text
Alice 25
```

---

### Comma-Separated Input

```python
name, age = input("Enter your name and age (comma-separated): ").split(',')
print(f"Name: {name}, Age: {age}")
```

**Input:**
```text
Bob,30
```

---

## 5. Using `map()` with Input

### Reading Multiple Integers

```python
numbers = list(map(int, input("Enter three numbers: ").split()))
print(numbers)
```

**Input:**
```text
1 2 3
```

**Output:**
```text
[1, 2, 3]
```

---

### How This Works

| Step | Description |
|----|------------|
| `input()` | Reads string |
| `.split()` | Converts to list of strings |
| `map(int, ...)` | Converts each string to int |
| `list()` | Stores result |

---

## 6. Handling Empty Input

```python
user_input = input("Enter something (or press enter to exit): ")

if not user_input:
    print("No input provided")
else:
    print(f"You entered: {user_input}")
```

---

### Why `if not user_input` Works

- Empty string `""` evaluates to `False`
- Non-empty string evaluates to `True`

---

## 7. Taking Input Until a Condition Is Met

### Quit-Based Loop

```python
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
```

---

### Controlled Integer Input

```python
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"You are {age} years old")
```

---

## 8. Reading Input as a List

### List of Strings

```python
fruits = input("Enter fruits separated by spaces: ").split()
print(fruits)
```

---

### List of Integers

```python
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(numbers)
```

---

## 9. User Input Inside a Function

```python
def get_user_info():
    name = input("Enter your name: ")

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    city = input("Enter your city: ")

    print(f"\nUser Info:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

get_user_info()
```

---

## Common Mistakes & Pitfalls

| Mistake | Why It Happens |
|------|---------------|
| Assuming input is numeric | `input()` returns string |
| No validation | Program crashes |
| Infinite loops | Missing break condition |
| Forgetting `.split()` | Input not separated |
| Not handling empty input | Unexpected behavior |

---

## Best Practices

✅ Always validate user input  
✅ Use `try-except` for conversions  
✅ Keep input logic separate from business logic  
✅ Re-prompt user politely  
❌ Never trust raw user input  

---

## Summary

| Concept | Explanation |
|------|------------|
| `input()` | Reads user input as string |
| Type casting | Convert to `int`, `float`, etc. |
| `split()` | Break input into parts |
| `map()` | Apply conversion to multiple values |
| Validation | Prevent invalid input |
| Loops | Repeat input until valid |

---

## Practice Tasks

1. Write a program that keeps asking for a number until the user enters an even number.  
2. Read 5 integers from the user and calculate their average.  
3. Create a function that asks for name, age, and email with validation.  
4. Accept comma-separated values and store them in a list.  
5. Modify a program to allow quitting with both `q` and `Q`.
