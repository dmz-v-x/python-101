## Assignment Operators in Python

### Overview

**Assignment operators** are used to **assign values** to variables.  
They can also **combine arithmetic or bitwise operations** with assignment to make code more concise.

Example:
```python
x = 10      # Assign 10 to x
x += 5      # Add 5 to x and assign the result back to x
print(x)    # Output: 15
```

Python executes `x += 5` as `x = x + 5`.

---

### List of Assignment Operators

| Operator | Example | Equivalent To | Description |
|-----------|----------|----------------|--------------|
| `=`  | `x = 5`   | — | Assigns value 5 to `x` |
| `+=` | `x += 3`  | `x = x + 3` | Adds and assigns |
| `-=` | `x -= 3`  | `x = x - 3` | Subtracts and assigns |
| `*=` | `x *= 3`  | `x = x * 3` | Multiplies and assigns |
| `/=` | `x /= 3`  | `x = x / 3` | Divides and assigns (result is always float) |
| `//=` | `x //= 3` | `x = x // 3` | Floor divides and assigns |
| `%=` | `x %= 3`  | `x = x % 3` | Modulus and assigns |
| `**=` | `x **= 3` | `x = x ** 3` | Exponentiation and assigns |
| `&=` | `x &= y`  | `x = x & y` | Bitwise AND and assign |
| `|=` | `x |= y`  | `x = x | y` | Bitwise OR and assign |
| `^=` | `x ^= y`  | `x = x ^ y` | Bitwise XOR and assign |
| `>>=` | `x >>= 2` | `x = x >> 2` | Bitwise right shift and assign |
| `<<=` | `x <<= 2` | `x = x << 2` | Bitwise left shift and assign |

---

### 1. Basic Assignment (`=`)

Assigns a value to a variable.

```python
x = 10
name = "Himanshu"
is_active = True

print(x)
print(name)
print(is_active)
```

**Output:**
```text
10
Himanshu
True
```

---

### 2. Add and Assign (`+=`)

```python
x = 5
x += 3   # same as x = x + 3
print(x)
```

**Output:**
```text
8
```

**With strings:**
```python
s = "Hello"
s += " World"
print(s)
```
**Output:**
```text
Hello World
```

**Explanation:**  
When used on strings, `+=` performs **concatenation**.

---

### 3. Subtract and Assign (`-=`)

```python
x = 10
x -= 4
print(x)
```

**Output:**
```text
6
```

**Explanation:**  
Subtracts `4` from `x`, then stores the result back in `x`.

---

### 4. Multiply and Assign (`*=`)

```python
x = 7
x *= 5
print(x)
```

**Output:**
```text
35
```

**String repetition with `*=`:**
```python
msg = "Hi"
msg *= 3
print(msg)
```

**Output:**
```text
HiHiHi
```

---

### 5. Divide and Assign (`/=`)

```python
x = 10
x /= 4
print(x)
```

**Output:**
```text
2.5
```

**Note:**  
Even if `x` was an integer, `/=` converts it to a **float** because true division always returns a float.

---

### 6. Floor Divide and Assign (`//=`)

```python
x = 10
x //= 4
print(x)
```

**Output:**
```text
2
```

**Explanation:**  
Performs floor division and assigns the floored result.

---

### 7. Modulus and Assign (`%=`)

```python
x = 10
x %= 4
print(x)
```

**Output:**
```text
2
```

**Explanation:**  
Stores the remainder after division (`10 % 4 = 2`) back into `x`.

---

### 8. Exponentiation and Assign (`**=`)

```python
x = 2
x **= 3
print(x)
```

**Output:**
```text
8
```

**Explanation:**  
`x **= 3` → raise `x` to the power of 3.

---

### 9. Bitwise Assignment Operators

These modify the bits of numbers directly. Useful in low-level or performance-sensitive code.

### Bitwise AND and Assign (`&=`)
```python
x = 5   # 0101
y = 3   # 0011
x &= y
print(x)
```
**Output:**
```text
1
```
**Reason:**  
0101 & 0011 = 0001 → 1

---

### Bitwise OR and Assign (`|=`)
```python
x = 5   # 0101
y = 3   # 0011
x |= y
print(x)
```
**Output:**
```text
7
```
**Reason:**  
0101 | 0011 = 0111 → 7

---

### Bitwise XOR and Assign (`^=`)
```python
x = 5   # 0101
y = 3   # 0011
x ^= y
print(x)
```
**Output:**
```text
6
```
**Reason:**  
0101 ^ 0011 = 0110 → 6

---

### Bitwise Right Shift and Assign (`>>=`)
```python
x = 8   # binary 1000
x >>= 2
print(x)
```
**Output:**
```text
2
```
**Explanation:**  
Right shift by 2 bits → 1000 → 0010 (2 in decimal)

---

### Bitwise Left Shift and Assign (`<<=`)
```python
x = 3   # binary 0011
x <<= 2
print(x)
```
**Output:**
```text
12
```
**Explanation:**  
Left shift by 2 bits → 0011 → 1100 (12 in decimal)

---

### Combining Assignment Operators

You can chain or reuse assignment operators for multiple updates:

```python
x = 10
x += 5
x *= 2
x -= 4
print(x)
```

**Step-by-step:**
- Start with 10  
- Add 5 → 15  
- Multiply by 2 → 30  
- Subtract 4 → 26

**Output:**
```text
26
```

---

### Type Behavior & Caveats

### 1. String + Number with `+=`
```python
s = "Age: "
# s += 25  # ❌ TypeError
s += str(25)  # ✅ Convert explicitly
print(s)
```
**Output:**
```text
Age: 25
```

### 2. Division always makes float
```python
x = 5
x /= 2
print(x, type(x))
```
**Output:**
```text
2.5 <class 'float'>
```

### 3. Mixed int–float arithmetic
```python
x = 5
x += 2.3
print(x)
```
**Output:**
```text
7.3
```
Python promotes `int` to `float` automatically.

---

### Complete Example

```python
x = 10

x += 2   # 12
x -= 4   # 8
x *= 3   # 24
x /= 6   # 4.0
x **= 2  # 16.0
x %= 5   # 1.0
print(x)
```

**Output:**
```text
1.0
```

---

### Summary Table

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `=` | Simple assignment | `x = 10` | `x = 10` |
| `+=` | Add and assign | `x += 5` | `x = x + 5` |
| `-=` | Subtract and assign | `x -= 5` | `x = x - 5` |
| `*=` | Multiply and assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and assign | `x /= 3` | `x = x / 3` |
| `//=` | Floor divide and assign | `x //= 3` | `x = x // 3` |
| `%=` | Modulus and assign | `x %= 3` | `x = x % 3` |
| `**=` | Exponentiation and assign | `x **= 2` | `x = x ** 2` |
| `&=` | Bitwise AND and assign | `x &= y` | `x = x & y` |
| `|=` | Bitwise OR and assign | `x |= y` | `x = x | y` |
| `^=` | Bitwise XOR and assign | `x ^= y` | `x = x ^ y` |
| `>>=` | Right shift and assign | `x >>= 2` | `x = x >> 2` |
| `<<=` | Left shift and assign | `x <<= 2` | `x = x << 2` |

---

### Key Takeaways

- Assignment operators combine updating and assigning into one concise step.  
- Arithmetic assignment operators (`+=`, `-=`, etc.) work with both numbers and strings (only `+=` and `*=` for strings).  
- Bitwise assignment operators manipulate data at the binary level.  
- `/=` always produces a float — even from integer division.  
- Python performs **automatic type conversion** when possible, but explicit conversions prevent surprises.  

---

### Practice Exercises

1. Write a program that updates a number using all arithmetic assignment operators in sequence.  
2. Create a string variable and use `+=` and `*=` to modify it.  
3. Demonstrate how `x //= y` and `x %= y` behave with negative numbers.  
4. Perform bitwise assignments on integers and explain their binary transformations step-by-step.  
5. Try mixing data types with `+=` and observe which cases cause errors.

---
