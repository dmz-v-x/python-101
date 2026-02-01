## Arithmetic Operators in Python — Complete Guide

### Overview

Python provides standard arithmetic operators for numbers and some special behaviors when using other types (like strings).  
This guide covers:

1. The operators themselves with examples  
2. How Python handles operations between different data types (type coercion)  
3. Edge cases and errors you can encounter (and why)  
4. Operator precedence and evaluation order

---

### List of Arithmetic Operators

| Operator | Symbol | Meaning |
|---------:|:------:|:--------|
| Addition | `+` | Add two numbers or concatenate strings |
| Subtraction | `-` | Subtract right operand from left |
| Multiplication | `*` | Multiply numbers or repeat strings |
| Division (true) | `/` | Floating-point division |
| Floor division | `//` | Division that floors to an integer (or floored float) |
| Modulus (remainder) | `%` | Remainder after integer division |
| Exponentiation | `**` | Power (raise to exponent) |

---

### 1. Addition (`+`)

### Numeric addition
```python
a = 5
b = 3
result = a + b
print(f"The sum of {a} and {b} is {result}")
```
**Output:**
```text
The sum of 5 and 3 is 8
```

### Addition with mixed numeric types (int + float)
Python **automatically promotes** `int` to `float` when necessary.
```python
x = 3
y = 4.5
print(x + y)
```
**Output:**
```text
7.5
```

### String concatenation with `+`
```python
str1 = "Hello"
str2 = " World"
print(str1 + str2)
```
**Output:**
```text
Hello World
```

### ❗ Error case: mixing strings and numbers with `+`
```python
"Age: " + 26   # This causes an error
```
**Reason & Error:**
You cannot directly add `str` and `int` — Python raises `TypeError` because these are different types and automatic coercion *does not* convert `int` to `str` for `+` concatenation.
**Fix:** Convert the number to `str` (or use f-strings):
```python
print("Age: " + str(26))
print(f"Age: {26}")
```

---

### 2. Subtraction (`-`)

```python
a = 10
b = 4
result = a - b
print(result)
```
**Output:**
```text
6
```

### With floats
```python
a = 10.5
b = 5
print(a - b)  # 5.5
```
**Output:**
```text
5.5
```

### ❗ Invalid: `str - str` not supported
Attempting to subtract strings or incompatible types raises `TypeError`.

---

### 3. Multiplication (`*`)

### Numeric multiplication
```python
a = 7
b = 5
print(a * b)  # 35
```
**Output:**
```text
35
```

### String repetition
```python
print("Hello" * 3)
```
**Output:**
```text
HelloHelloHello
```

### Mixed numeric types
```python
print(3 * 4.5)  # 13.5
```
**Output:**
```text
13.5
```

---

### 4. Division (`/`) — True division (always float)

```python
a = 10
b = 4
print(a / b)  # 2.5
```
**Output:**
```text
2.5
```

**Notes:**
- In Python 3, `/` always returns a `float` (even if division is exact).
- Division by zero raises a `ZeroDivisionError`:
  ```python
  5 / 0  # ZeroDivisionError
  ```

---

### 5. Floor Division (`//`)

Floor division returns the **floor** (largest integer ≤ result) of the quotient.

```python
a = 10
b = 4
print(a // b)  # 2
```
**Output:**
```text
2
```

### Important: Floor division with negative numbers
Floor division **floors toward negative infinity**, not just truncation.

```python
print(7 // 3)    # 2
print(-7 // 3)   # -3  (because -7/3 ≈ -2.333 -> floor is -3)
```
**Output:**
```text
2
-3
```

---

### 6. Modulus (`%`) — Remainder

```python
a = 10
b = 4
print(a % b)  # 2
```
**Output:**
```text
2
```

### Relationship with floor division
For integers: `a == (a // b) * b + (a % b)` always holds (consistent with floor division behavior).

### Negative values and modulus
Because `//` floors toward negative infinity, `%` ensures the equation above holds:

```python
print(-7 % 3)   # 2, since -7 == (-3)*3 + 2
```
**Output:**
```text
2
```

---

### 7. Exponentiation (`**`)

```python
a = 2
b = 3
print(a ** b)  # 8
```
**Output:**
```text
8
```

You can use non-integer exponents:
```python
print(9 ** 0.5)  # 3.0 (square root)
```
**Output:**
```text
3.0
```

---

### Combining Operators (Examples)

```python
print(2 + 3 * 4)        # 14  (multiplication first)
print((2 + 3) * 4)      # 20  (parentheses change order)
print(2 ** 3 ** 2)      # 512 (right-associative: 3**2=9 -> 2**9=512)
```
**Output:**
```text
14
20
512
```

---

### Operator Precedence (Highest → Lowest)

1. Parentheses `()`  
2. Exponentiation `**` (right-associative)  
3. Multiplication, Division, Floor division, Modulus `*`, `/`, `//`, `%`  
4. Addition, Subtraction `+`, `-`

Always use parentheses to make your intent explicit.

---

### Mixing Data Types — Rules & Reasoning

### 1. Numeric combinations (int, float)
- `int` and `int` → `int` (for operators that produce integers, e.g., `//`, `%` depending)  
- `int` and `float` → Python **promotes** `int` to `float` and the operation yields a `float`.

**Example:**
```python
print(type(3 + 4))      # int
print(type(3 + 4.0))    # float (3 promoted to 3.0)
```
**Output:**
```text
<class 'int'>
<class 'float'>
```

**Reason:** Python uses a predictable coercion rule to avoid loss of fractional data.

---

### 2. `bool` with numbers
`bool` is a subclass of `int` in Python: `True == 1`, `False == 0`.  
So arithmetic works naturally:

```python
print(True + 3)   # 4
print(False * 10) # 0
```
**Output:**
```text
4
0
```

---

### 3. Strings and numbers
- `str + str` → concatenation (`"a" + "b" -> "ab"`)  
- `str * int` → repetition (`"a" * 3 -> "aaa"`)  
- `str + int` → **TypeError** — Python does not implicitly convert `int` to `str` for `+`.

**Example of error:**
```python
"Age: " + 26
```
**Raises:**
```text
TypeError: can only concatenate str (not "int") to str
```

**Fixes:**
- Convert number to string: `"Age: " + str(26)`  
- Use f-strings: `f"Age: {26}"`  
- Use `print("Age:", 26)` which separates by spaces (no concatenation).

---

### 4. Division by zero
Any numeric division where denominator is zero raises `ZeroDivisionError`:
```python
10 / 0   # ZeroDivisionError
10 // 0  # ZeroDivisionError
10 % 0   # ZeroDivisionError
```

---

### 5. Complex numbers
Python supports complex numbers: `1 + 2j`. Arithmetic between complex and real numbers is allowed; result is complex.

```python
z = 1 + 2j
print(z * 2)      # (2+4j)
print(type(z))    # <class 'complex'>
```
**Output:**
```text
(2+4j)
<class 'complex'>
```

---

### 6. Float precision & rounding issues
Floating-point numbers are represented in binary and are **not exact** for many decimal fractions.

```python
print(0.1 + 0.2)  # 0.30000000000000004
```
**Output:**
```text
0.30000000000000004
```

**Reason:** Binary floating-point cannot exactly represent 0.1 or 0.2.  
**Workarounds:**
- Use `round()` for display: `round(0.1 + 0.2, 2)` → `0.3`  
- Use the `decimal` module for precise decimal arithmetic when needed.

---

### Common Errors & Why They Happen (Quick Reference)

- `TypeError: can only concatenate str (not "int") to str`  
  *Cause:* Trying to `+` a `str` and `int`. Convert or use formatting.

- `ZeroDivisionError: division by zero`  
  *Cause:* Denominator is zero in `/`, `//`, or `%`.

- `TypeError: unsupported operand type(s)`  
  *Cause:* Operation between unsupported types (e.g., `list + int`, or `str - str`).

- Unexpected floating-point results (not an exception)  
  *Cause:* Binary representation of decimals. Use rounding or `decimal`.

---

### Quick Examples (All together)

```python
# Addition
print(5 + 3)             # 8

# Subtraction
print(10 - 4)            # 6

# Multiplication
print(7 * 5)             # 35
print("Hi" * 3)          # HiHiHi

# Division
print(10 / 4)            # 2.5

# Floor division
print(10 // 4)           # 2
print(-7 // 3)           # -3

# Modulus
print(10 % 4)            # 2
print(-7 % 3)            # 2

# Exponentiation
print(2 ** 3)            # 8

# Mixed types
print(3 + 4.5)           # 7.5
print(True + 4)          # 5

# Errors (examples; uncomment to see them)
# print("Age: " + 26)    # TypeError
# print(5 / 0)           # ZeroDivisionError

# Float precision
print(0.1 + 0.2)         # 0.30000000000000004
print(round(0.1 + 0.2, 2))  # 0.3
```

**Expected Output:**
```text
8
6
35
HiHiHi
2.5
2
-3
2
2
8
7.5
5
0.30000000000000004
0.3
```

---

### Summary & Best Practices

- Use `+`, `-`, `*`, `/`, `//`, `%`, `**` for standard arithmetic.  
- Mixing `int` and `float` is safe — Python promotes `int` to `float`.  
- `bool` behaves like `int` (True=1, False=0).  
- Avoid concatenating `str` with numeric types using `+`. Use `str()`, f-strings, or `print()` with comma separation.  
- Be mindful of float precision; use `round()` or `decimal` for exact decimal calculations.  
- Watch out for `ZeroDivisionError` and for floor-division behavior with negatives.  
- Use parentheses to make complex expressions readable and unambiguous.

---

### Practice Exercises

1. Write a function that takes two integers and returns a tuple: `(sum, difference, product, quotient, floor_div, remainder, power)`. Handle division by zero safely.  
2. Show examples where `//` and `%` behave differently for negative numbers. Explain the results.  
3. Demonstrate float rounding errors and solve them with the `decimal` module (research `decimal.Decimal`).  
4. Try combining `str` and `int` using `+` and fix it using `f-strings`.

---
