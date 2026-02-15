## Conditional Statements in Python

**Conditional statements** allow a program to **make decisions** based on conditions.  
They control the **flow of execution** — deciding **which code runs and which doesn’t**.

In Python, conditions are evaluated to either:
- `True`
- `False`

Based on this result, Python executes the corresponding block of code.

---

## Core Conditional Tools in Python

| Tool | Purpose |
|-----|--------|
| `if` | Run code if condition is true |
| `elif` | Check another condition |
| `else` | Run code if all conditions fail |
| Comparison operators | Compare values |
| Logical operators | Combine conditions |
| Membership operators | Check presence |
| Ternary operator | One-line condition |
| `pass` | Placeholder block |

---

## 1. Comparison Operators

Comparison operators return **boolean values** (`True` or `False`).

| Operator | Meaning |
|--------|--------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

---

### Equality & Inequality Examples

```python
print(1 == 1.0)
print(1 == "1")
print([] == False)
print(None != 0)
```

**Output:**
```text
True
False
False
True
```

Explanation:
- Python compares **values and types**
- `1 == 1.0` → same numeric value
- Different data types usually evaluate to `False`

---

### Invalid Comparisons

```python
# print(1 < "2")
```

**Error:**
```text
TypeError: '<' not supported between instances of 'int' and 'str'
```

Python **does not allow ordering comparisons** between unrelated types.

---

## 2. Special Comparison Cases

```python
print(True == 1)
print(False < 1)
print(None == None)
```

**Output:**
```text
True
True
True
```

Invalid:
```python
# print(None > 1)
```

**Error:**
```text
TypeError: '>' not supported between instances of 'NoneType' and 'int'
```

---

## 3. `ord()` and `chr()` Functions

Used to work with **character codes**.

### `ord()` → Character → Number
### `chr()` → Number → Character

```python
print(ord('A'))
print(ord('a'))
print(ord('€'))

print(chr(65))
print(chr(97))
print(chr(8364))
```

**Output:**
```text
65
97
8364
A
a
€
```

Used internally when comparing strings character by character.

---

## 4. Basic `if` Statement

Executes code **only if condition is true**.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

**Output:**
```text
x is greater than 5
```

---

## 5. `if-else` Statement

Executes **one of two paths**.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

**Output:**
```text
x is less than or equal to 5
```

---

## 6. `if-elif-else` Statement

Used when **multiple conditions** need to be checked.

```python
x = 20
if x < 10:
    print("x is less than 10")
elif x < 20:
    print("x is less than 20 but >= 10")
else:
    print("x is 20 or greater")
```

**Output:**
```text
x is 20 or greater
```

Python stops checking once a condition becomes `True`.

---

## 7. Nested `if` Statements

An `if` inside another `if`.

```python
x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")
    else:
        print("x is 20 or more")
else:
    print("x is less than or equal to 10")
```

**Output:**
```text
x is between 10 and 20
```

---

## 8. Logical Operators in Conditions

| Operator | Meaning |
|--------|--------|
| `and` | All conditions must be true |
| `or` | At least one condition true |
| `not` | Reverses the condition |

---

### Using `and`

```python
x = 15
if x > 10 and x < 20:
    print("x is between 10 and 20")
```

**Output:**
```text
x is between 10 and 20
```

---

### Using `or`

```python
x = 25
if x < 10 or x > 20:
    print("x is either less than 10 or greater than 20")
```

**Output:**
```text
x is either less than 10 or greater than 20
```

---

### Using `not`

```python
is_logged_in = False
if not is_logged_in:
    print("Please log in")
```

**Output:**
```text
Please log in
```

---

## 9. Membership Operators (`in`, `not in`)

Used to check **existence** in collections.

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

if "orange" not in fruits:
    print("Orange is not in the list")
```

**Output:**
```text
Apple is in the list
Orange is not in the list
```

---

## 10. Chained Comparisons

Python allows **clean multi-condition comparisons**.

```python
x = 15
if 10 < x < 20:
    print("x is between 10 and 20")
```

**Output:**
```text
x is between 10 and 20
```

Equivalent to:
```python
if x > 10 and x < 20:
```

---

## 11. Conditional (Ternary) Operator

Used for **one-line conditions**.

### Syntax
```python
true_value if condition else false_value
```

### Example

```python
x = 10
y = 20
result = "x is greater" if x > y else "y is greater"
print(result)
```

**Output:**
```text
y is greater
```

---

## 12. `pass` Statement

Used as a **placeholder** where a statement is syntactically required.

```python
x = 10
if x > 5:
    pass
else:
    print("x is less than or equal to 5")
```

Useful during development to avoid syntax errors.

---

## Common Mistakes & Errors

| Mistake | Why It Happens |
|-------|----------------|
| Forgetting indentation | Python relies on indentation |
| Comparing incompatible types | `1 < "2"` |
| Using `=` instead of `==` | Assignment vs comparison |
| Overusing nested `if` | Reduces readability |
| Missing `else` handling | Leads to unexpected logic |

---

## Summary

| Concept | Description |
|-------|-------------|
| `if` | Executes when condition is true |
| `elif` | Checks alternative conditions |
| `else` | Fallback execution |
| Comparison operators | Compare values |
| Logical operators | Combine conditions |
| Membership operators | Check existence |
| Ternary operator | One-line condition |
| `pass` | Placeholder block |

---

## Practice Tasks

1. Write a program to check if a number is positive, negative, or zero.  
2. Check if a year is a leap year using conditions.  
3. Use a ternary operator to check if a number is even or odd.  
4. Create a list of usernames and check login access using `in`.  
5. Write a nested `if` program to validate age and citizenship.  
