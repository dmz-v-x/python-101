## Exception Handling in Python

An **exception** in Python is an **error that occurs during program execution**.  
If not handled properly, exceptions **crash the program** and stop execution.

Python provides a powerful mechanism called **exception handling** to:
- Catch runtime errors
- Prevent program crashes
- Handle errors gracefully
- Keep applications stable and predictable

---

## What Happens When an Exception Occurs?

1. Python encounters an error
2. Python **raises an exception**
3. Normal execution stops
4. Python looks for an exception handler
5. If none is found → program crashes

---

## Common Built-in Exceptions

| Exception | When It Occurs |
|--------|---------------|
| `ZeroDivisionError` | Division by zero |
| `TypeError` | Invalid operation between types |
| `ValueError` | Correct type, wrong value |
| `IndexError` | Invalid list/tuple index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File does not exist |
| `ImportError` | Module import fails |
| `AttributeError` | Attribute not found |
| `NameError` | Variable not defined |

---

## Basic Syntax of Exception Handling

```python
try:
    # code that may raise an exception
except SomeException:
    # code that runs if exception occurs
else:
    # runs if no exception occurs (optional)
finally:
    # always runs (optional)
```

---

## 1. Handling Division by Zero

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print("Division successful.")
finally:
    print("This will always execute.")
```

**Output:**
```text
Error: Cannot divide by zero!
This will always execute.
```

---

### Explanation

- `try` → risky code
- `except` → error handler
- `else` → runs only if no error
- `finally` → cleanup (always runs)

---

## 2. Catching Multiple Exceptions (Multiple `except`)

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid integer!")
```

---

## 3. Catching Multiple Exceptions (Single `except`)

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")
```

Cleaner when error handling logic is the same.

---

## 4. Accessing Exception Information

Use `as` to inspect the error message.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
```

**Output:**
```text
Error occurred: division by zero
```

---

## 5. Raising Exceptions Manually (`raise`)

You can raise exceptions intentionally when business rules fail.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    else:
        print("Age is valid.")

try:
    check_age(16)
except ValueError as e:
    print(f"Error: {e}")
```

**Output:**
```text
Error: Age must be 18 or older.
```

---

## 6. Why Raise Exceptions?

✅ Enforce validation  
✅ Signal invalid states  
✅ Fail fast with clarity  
✅ Improve debugging  

---

## 7. Custom Exceptions

Sometimes built-in exceptions are not expressive enough.

### Creating a Custom Exception

```python
class AgeTooSmallError(Exception):
    """Exception raised when age is below allowed limit."""
    def __init__(self, age, message="Age must be 18 or older."):
        self.age = age
        self.message = message
        super().__init__(self.message)
```

---

### Using the Custom Exception

```python
def check_age(age):
    if age < 18:
        raise AgeTooSmallError(age)
    else:
        print("Age is valid.")

try:
    check_age(15)
except AgeTooSmallError as e:
    print(f"Error: {e}")
```

**Output:**
```text
Error: Age must be 18 or older.
```

---

## 8. `else` and `finally` in Detail

### `else`
- Runs **only if no exception occurs**
- Keeps `try` block clean

### `finally`
- Always runs
- Used for cleanup (closing files, DB connections)

---

### Example: File Handling

```python
try:
    f = open("test.txt", "r")
    f.write("Test data")
except IOError:
    print("Error: Could not write to file.")
else:
    print("File written successfully.")
finally:
    print("Closing the file.")
    f.close()
```

---

## 9. Exception Hierarchy (Important Concept)

All exceptions inherit from `BaseException`.

```text
BaseException
 └── Exception
     ├── ValueError
     ├── TypeError
     ├── IndexError
     └── ...
```

Catching `Exception` catches **almost all runtime errors**.

---

### Example (Catch-All)

```python
try:
    risky_code()
except Exception as e:
    print("Something went wrong:", e)
```

Use sparingly — may hide bugs.

---

## Common Mistakes & Pitfalls

| Mistake | Why It’s Bad |
|------|-------------|
| Catching broad `Exception` | Hides real bugs |
| Empty `except` block | Silent failures |
| Ignoring exception info | Hard to debug |
| No cleanup | Resource leaks |
| Using exceptions for flow control | Poor design |

---

## Best Practices

✅ Catch **specific exceptions**  
✅ Use `finally` for cleanup  
✅ Raise meaningful exceptions  
✅ Log errors properly  
❌ Don’t suppress errors silently  

---

## Summary

| Concept | Purpose |
|------|--------|
| Exception | Runtime error |
| `try` | Risky code |
| `except` | Error handling |
| `else` | Runs on success |
| `finally` | Cleanup |
| `raise` | Manual exception |
| Custom exception | Domain-specific errors |

---

## Practice Tasks

1. Handle a `ValueError` when converting input to integer.  
2. Write a function that raises an exception for negative numbers.  
3. Create a custom exception for password validation.  
4. Use `try-except-finally` with file handling.  
5. Explain why catching `Exception` blindly is dangerous.
