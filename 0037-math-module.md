## Math Module in Python

Python provides **powerful mathematical capabilities** through:
- Built-in math-related functions
- The **`math` module** (part of the standard library)

The `math` module offers:
- Precise mathematical operations
- Trigonometric functions
- Logarithms
- Factorials
- Number theory utilities

---

## Why Use the `math` Module?

- High precision (written in C)
- Faster than manual implementations
- Clean, readable, and reliable
- Industry standard for mathematical computation

---

## Importing the `math` Module

```python
import math
```

---

## Built-in Math Functions (No `math` Needed)

---

### 1. `abs(x)` — Absolute Value

Returns the **non-negative** value of a number.

```python
print(abs(-5))
print(abs(3.14))
```

**Output:**
```text
5
3.14
```

---

### 2. `pow(x, y)` — Power

Raises `x` to the power of `y`.

```python
print(pow(2, 3))
print(pow(5, 2))
```

**Output:**
```text
8
25
```

Equivalent to `x ** y`, but safer for large numbers.

---

### 3. `round(x, n)` — Rounding

Rounds a number to `n` decimal places.

```python
print(round(3.14159, 2))
print(round(3.75))
```

**Output:**
```text
3.14
4
```

Python uses **banker’s rounding** (rounds to even).

---

## Trigonometric Functions (`math`)

---

### 4. `math.sin(x)` — Sine

Angle must be in **radians**.

```python
print(math.sin(math.pi / 2))
```

**Output:**
```text
1.0
```

---

### 5. `math.tan(x)` — Tangent

```python
print(math.tan(math.pi / 4))
```

**Output:**
```text
1.0
```

---

### 6. `math.radians(deg)` — Degrees → Radians

```python
print(math.radians(180))
```

**Output:**
```text
3.141592653589793
```

---

## Factorials & Combinatorics

---

### 7. `math.factorial(x)`

Computes `x!` (x factorial).

```python
print(math.factorial(5))
```

**Output:**
```text
120
```

⚠️ Only works with **non-negative integers**.

---

### 8. `math.comb(n, k)` — Combinations

Number of ways to choose `k` items from `n`.

```python
print(math.comb(5, 2))
```

**Output:**
```text
10
```

---

## Number Theory Functions

---

### 9. `math.gcd(a, b)` — Greatest Common Divisor

```python
print(math.gcd(24, 36))
```

**Output:**
```text
12
```

---

### 10. `math.lcm(a, b)` — Least Common Multiple (Python 3.9+)

```python
print(math.lcm(12, 15))
```

**Output:**
```text
60
```

---

## Square Roots

---

### 11. `math.sqrt(x)` — Square Root

```python
print(math.sqrt(16))
```

**Output:**
```text
4.0
```

⚠️ Returns `float` only.

---

### 12. `math.isqrt(x)` — Integer Square Root

```python
print(math.isqrt(17))
```

**Output:**
```text
4
```

Largest integer whose square ≤ `x`

---

## Rounding Utilities

---

### 13. `math.ceil(x)` — Ceiling

Smallest integer ≥ `x`.

```python
print(math.ceil(3.4))
```

**Output:**
```text
4
```

---

### 14. `math.floor(x)` — Floor

Largest integer ≤ `x`.

```python
print(math.floor(3.9))
```

**Output:**
```text
3
```

---

## Mathematical Constants

---

### 15. `math.pi`

```python
print(math.pi)
```

**Output:**
```text
3.141592653589793
```

Other constants:
- `math.e`
- `math.tau`
- `math.inf`
- `math.nan`

---

## Common Mistakes & Pitfalls

| Mistake | Why It Happens |
|------|---------------|
| Using degrees instead of radians | Trig functions expect radians |
| Using `sqrt()` on negative numbers | Raises `ValueError` |
| Forgetting to import `math` | NameError |
| Expecting `round()` to always round up | Banker’s rounding |
| Using `math.sqrt()` for integers only | Use `math.isqrt()` |

---

## Best Practices

✅ Use `math` for precision  
✅ Convert degrees to radians explicitly  
✅ Prefer `math.isqrt()` for integer math  
✅ Use built-in functions when possible  
❌ Don’t reimplement math logic  

---

## Summary

| Function | Purpose |
|------|--------|
| `abs()` | Absolute value |
| `pow()` | Power |
| `round()` | Rounding |
| `sin`, `tan` | Trigonometry |
| `factorial()` | Factorials |
| `comb()` | Combinations |
| `gcd()`, `lcm()` | Number theory |
| `sqrt()`, `isqrt()` | Square roots |
| `ceil()`, `floor()` | Rounding |
| `math.pi` | Constant |

---

## Practice Tasks

1. Convert degrees to radians and calculate sine.  
2. Find GCD and LCM of two user-input numbers.  
3. Write a program to calculate combinations using `math.comb`.  
4. Compare `sqrt()` vs `isqrt()` outputs.  
5. Demonstrate banker’s rounding behavior in Python.
