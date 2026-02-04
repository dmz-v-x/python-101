## Logical Operators in Python


### Overview

Logical operators are used to **combine or invert** Boolean expressions.  
They return a **Boolean value** (`True` or `False`) depending on the logical relationship between operands.

These operators are fundamental in **decision-making** and **conditional statements** (like `if`, `while`, etc.).

---

### Logical Operators Summary

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `and` | Returns `True` if **both** conditions are true | `True and True` | `True` |
| `or` | Returns `True` if **at least one** condition is true | `True or False` | `True` |
| `not` | Inverts the Boolean value | `not True` | `False` |

---

### 1. The `and` Operator

The `and` operator returns `True` only if **both** operands are `True`.

```python
x = 10
print(x > 5 and x < 20)
```

**Output:**
```text
True
```

**Explanation:**  
Both conditions are `True`, so the final result is `True`.

### Example with mixed results

```python
a = 5
b = 10
print(a > 2 and b < 5)
```

**Output:**
```text
False
```

**Explanation:**  
First condition → `True`  
Second condition → `False`  
Hence, `True and False → False`.

---

### 2. The `or` Operator

The `or` operator returns `True` if **any one** of the conditions is `True`.

```python
x = 15
print(x > 10 or x < 5)
```

**Output:**
```text
True
```

**Explanation:**  
The first condition (`x > 10`) is `True`, so Python doesn’t even check the second one (called **short-circuiting**).

---

### Example

```python
a = 2
b = 8
print(a > 5 or b > 5)
```

**Output:**
```text
True
```

---

### 3. The `not` Operator

The `not` operator **inverts** the Boolean result of a condition.

```python
x = 10
print(not (x > 5))
```

**Output:**
```text
False
```

**Explanation:**  
`x > 5` → `True`,  
`not True` → `False`.

---

### Example

```python
is_logged_in = False
print(not is_logged_in)
```

**Output:**
```text
True
```

**Explanation:**  
Negating `False` gives `True`.

---

### 4. Combining Logical Operators

You can combine multiple logical operators in one expression.

```python
x = 7
print(x > 5 and x < 10 or x == 15)
```

**Output:**
```text
True
```

**Explanation:**  
`x > 5` → True  
`x < 10` → True  
`x == 15` → False  
So `True and True or False` → `True`.

---

### 5. Operator Precedence (Order of Evaluation)

Python evaluates logical operators in the following order:

1. `not`
2. `and`
3. `or`

You can use parentheses `()` to **change** the default order.

```python
x = True
y = False
z = True

print(x or y and not z)
```

**Step-by-step:**
1. `not z` → `not True` → `False`
2. `y and False` → `False`
3. `x or False` → `True`

**Output:**
```text
True
```

✅ Use parentheses for clarity:
```python
print((x or y) and not z)
```

---

### 6. Logical Operators with Non-Boolean Values

In Python, logical operators can also be used with **non-Boolean values**.  
They return one of the operands instead of strictly `True` or `False`.

---

### Example: `and` with Non-Boolean Values

```python
print(10 and 20)
print(0 and 20)
print(10 and 0)
```

**Output:**
```text
20
0
0
```

**Explanation:**
- `and` returns the **first falsy value**, or the **last value** if all are truthy.
- `10 and 20` → both are truthy → returns `20` (last operand).
- `0 and 20` → `0` is falsy → returns `0`.

---

### Example: `or` with Non-Boolean Values

```python
print(10 or 20)
print(0 or 20)
print(0 or 0)
```

**Output:**
```text
10
20
0
```

**Explanation:**
- `or` returns the **first truthy value**, or the **last value** if all are falsy.
- `10 or 20` → `10` is truthy → returns `10`.
- `0 or 20` → `0` is falsy → returns `20`.

---

### Example: `not` with Non-Boolean Values

```python
print(not 0)     # True
print(not 5)     # False
print(not "")    # True
print(not "Hi")  # False
```

**Explanation:**
- `not` converts the value to a Boolean before negating it.
- Falsy values: `0`, `""`, `None`, `False`, `[]`, `{}`, `set()`
- Truthy values: Everything else.

---

### 7. Short-Circuit Evaluation

Python uses **short-circuiting** — it stops evaluating as soon as the result is determined.

### Example with `and`
```python
print(False and print("Hello"))
```
**Output:**
```text
False
```
**Explanation:**  
`and` stops at the first `False`, so `"Hello"` is **not printed**.

---

### Example with `or`
```python
print(True or print("Hi"))
```
**Output:**
```text
True
```
**Explanation:**  
`or` stops at the first `True`, so `"Hi"` is **not printed**.

---

### 8. Logical Operators with Expressions

```python
x = 5
y = 10
print((x < y) and (y < 20))   # True
print((x == 5) or (y == 5))   # True
print(not (x > y))            # True
```

**Output:**
```text
True
True
True
```

---

### 9. Real-World Example

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials")
```

**Output:**
```text
Login successful!
```

---

### 10. Common Mistakes

### ❌ Mistake 1: Using `&` and `|` instead of `and` and `or`
```python
print(True & False)  # Works, but bitwise
print(True | False)
```
**⚠️ Use `and` / `or` for logical comparisons**, not `&` or `|`.

---

### ❌ Mistake 2: Forgetting Short-Circuit Behavior

```python
x = 0
x and (1/x)   # ✅ No ZeroDivisionError because `x` is False
```

---

### 11. Practice Examples

Try to predict the output before running:

```python
print(True or False and False)
print(not (False or False))
print(0 or "Python")
print("" and "World")
print(not 5 > 10)
```

---

### Summary Table

| Operator | Description | Truth Table (A, B) | Result |
|-----------|--------------|--------------------|--------|
| `and` | True if both A and B are True | A=True, B=True | True |
| `or` | True if any one is True | A=True, B=False | True |
| `not` | Inverts Boolean value | A=True → `not A` | False |

---

### Key Takeaways

- Logical operators combine conditions and return Boolean results.  
- `and` → all must be True.  
- `or` → at least one must be True.  
- `not` → reverses the Boolean value.  
- Python supports **short-circuiting** for performance.  
- Logical operators can work with **non-Boolean** values and return operands directly.  
- Use parentheses `()` to control evaluation order clearly.

---
