## Comparison Operators in Python

---

### Overview

**Comparison operators** are used to **compare two values**.  
They always return a **Boolean result** — either `True` or `False`.

These operators are fundamental to **decision-making** in Python (e.g., in `if`, `while`, or conditional expressions).

---

### List of Comparison Operators

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 7` | `True` |
| `<` | Less than | `3 < 8` | `True` |
| `>=` | Greater than or equal to | `7 >= 7` | `True` |
| `<=` | Less than or equal to | `4 <= 5` | `True` |

---

### 1. Equal To (`==`)

Checks if the **values** of two operands are equal.

```python
a = 10
b = 10
print(a == b)
```

**Output:**
```text
True
```

**Explanation:**  
Both `a` and `b` store the same value (`10`), so the comparison is `True`.

---

### Example with strings

```python
name1 = "Python"
name2 = "python"
print(name1 == name2)
```

**Output:**
```text
False
```

**Explanation:**  
String comparison is **case-sensitive** in Python. `"Python"` ≠ `"python"`.

---

### Example with different data types (but same value)

```python
print(10 == 10.0)
```

**Output:**
```text
True
```

**Explanation:**  
`10` (int) and `10.0` (float) are considered **equal in value**, even though they have different types.

---

### 2. Not Equal To (`!=`)

Checks if two operands are **not equal**.

```python
x = 5
y = 10
print(x != y)
```

**Output:**
```text
True
```

**Explanation:**  
Since `5` is not equal to `10`, the result is `True`.

---

### 3. Greater Than (`>`)

Returns `True` if the left operand is **strictly greater** than the right.

```python
a = 15
b = 10
print(a > b)
```

**Output:**
```text
True
```

---

### 4. Less Than (`<`)

Returns `True` if the left operand is **strictly smaller** than the right.

```python
a = 5
b = 9
print(a < b)
```

**Output:**
```text
True
```

---

### 5. Greater Than or Equal To (`>=`)

```python
a = 10
b = 10
print(a >= b)
```

**Output:**
```text
True
```

**Explanation:**  
The expression checks if `a` is either greater than or equal to `b`.

---

### 6. Less Than or Equal To (`<=`)

```python
a = 3
b = 7
print(a <= b)
```

**Output:**
```text
True
```

**Explanation:**  
`3` is indeed less than `7`, so it evaluates to `True`.

---

### 7. Chained Comparisons (Pythonic Style)

Python allows chaining multiple comparisons elegantly.

```python
x = 5
print(1 < x < 10)
```

**Output:**
```text
True
```

**Explanation:**  
This is equivalent to:
```python
1 < x and x < 10
```

---

### Another example:

```python
age = 20
print(18 <= age < 60)
```

**Output:**
```text
True
```

**Explanation:**  
The expression checks that age is between 18 and 60 (inclusive of 18, exclusive of 60).

---

### Comparing Different Data Types

Python allows comparisons between **numeric types** (`int`, `float`, `bool`).

```python
print(10 == 10.0)     # True (same value)
print(10 > True)      # True (True is 1)
print(False < 1)      # True
```

**Output:**
```text
True
True
True
```

---

### Incompatible Type Comparisons

Trying to compare **unrelated types** (e.g., `str` and `int`) raises a `TypeError`.

```python
print("10" > 5)
```

**Error:**
```text
TypeError: '>' not supported between instances of 'str' and 'int'
```

**Why?**  
Python doesn’t know how to order `"10"` (a string) and `5` (an integer).

✅ Correct approach:
```python
print(int("10") > 5)
```

---

### String Comparison Rules

Strings are compared **lexicographically** (like dictionary order), based on Unicode code points.

```python
print("apple" < "banana")  # True
print("a" < "B")           # False
```

**Output:**
```text
True
False
```

**Explanation:**
- `"apple"` comes before `"banana"` alphabetically.  
- `"a"` has a Unicode value of 97, while `"B"` is 66 — hence `"a" > "B"`.

You can check Unicode values using:
```python
print(ord("a"))  # 97
print(ord("B"))  # 66
```

---

### Boolean Comparison Examples

```python
print(True == 1)     # True
print(False == 0)    # True
print(True > False)  # True
print(False < True)  # True
```

**Output:**
```text
True
True
True
True
```

**Explanation:**  
In numeric context: `True` → 1, `False` → 0.

---

### Comparing Complex Numbers

Complex numbers (`a + bj`) **cannot** be compared using `<`, `>`, `<=`, `>=`.

```python
z1 = 2 + 3j
z2 = 3 + 2j
# print(z1 > z2)  # ❌ Error
```

**Error:**
```text
TypeError: '>' not supported between instances of 'complex' and 'complex'
```

✅ You can compare equality though:
```python
print(z1 == z2)  # False
```

---

### Combining Comparison Results

You can use **logical operators** (`and`, `or`, `not`) with comparison results.

```python
x = 7
print(x > 5 and x < 10)  # True
print(x < 5 or x == 7)   # True
print(not (x == 7))      # False
```

**Output:**
```text
True
True
False
```

---

### Complete Example

```python
a = 10
b = 20
c = 10

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= c)   # True
print(a <= c)   # True

# Chained comparison
print(5 < a <= 20)  # True
```

**Output:**
```text
False
True
False
True
True
True
True
```

---

### Summary Table

| Operator | Meaning | Example | Result |
|-----------|----------|----------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 3` | `True` |
| `<` | Less than | `2 < 5` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 4` | `True` |

---

### Key Takeaways

- Comparison operators **return Boolean values** (`True` or `False`).  
- Strings are compared **lexicographically** (alphabetical order, case-sensitive).  
- You can **chain comparisons** in Python for cleaner logic.  
- Comparing unrelated types (like `str` and `int`) raises `TypeError`.  
- Complex numbers can only be checked for equality (`==`, `!=`).  
- Booleans behave like integers (`True → 1`, `False → 0`) in comparisons.  

---

### Practice Exercises

1. Compare two numbers and print whether they are equal, greater, or smaller.  
2. Compare two strings — one lowercase and one uppercase — and explain why the result occurs.  
3. Demonstrate `chained comparisons` to check if a number lies within a given range.  
4. Try comparing `"25"` (string) and `25` (int) and handle the error using `int()` conversion. 
5. Compare boolean values with integers and explain the result.

---
