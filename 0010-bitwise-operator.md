## Bitwise Operators in Python


### Overview

Bitwise operators in Python are used to perform operations **on bits** (binary digits) directly.  
They operate on the **binary representations** of integers (0s and 1s).

Bitwise operations are commonly used in:
- **Low-level programming** (e.g., hardware control, networking)
- **Data compression**
- **Cryptography**
- **Optimization tasks**

---

### List of Bitwise Operators

| Operator | Name | Description | Example | Result (Decimal) |
|-----------|------|--------------|----------|------------------|
| `&` | AND | Sets each bit to 1 if both bits are 1 | `5 & 3` | `1` |
| `|` | OR | Sets each bit to 1 if one of two bits is 1 | `5 | 3` | `7` |
| `^` | XOR | Sets each bit to 1 if only one of the bits is 1 | `5 ^ 3` | `6` |
| `~` | NOT | Inverts all bits (1 → 0, 0 → 1) | `~5` | `-6` |
| `<<` | Left Shift | Shifts bits to the left by given number | `5 << 1` | `10` |
| `>>` | Right Shift | Shifts bits to the right by given number | `5 >> 1` | `2` |

---

### 1. Understanding Binary Representation

Before diving deeper, let’s understand how numbers look in binary.

```python
a = 5
b = 3
print(bin(a))  # Binary representation of 5
print(bin(b))  # Binary representation of 3
```

**Output:**
```text
0b101
0b11
```

- `5` in binary → `101`
- `3` in binary → `011`

---

### 2. Bitwise AND (`&`)

Performs **AND operation** on each bit:
- 1 & 1 → 1
- 1 & 0 → 0
- 0 & 1 → 0
- 0 & 0 → 0

```python
a = 5  # 101
b = 3  # 011
print(a & b)
print(bin(a & b))
```

**Output:**
```text
1
0b1
```

**Explanation:**  
```
  101
& 011
= 001 → 1
```

---

### 3. Bitwise OR (`|`)

Sets each bit to 1 if **either** bit is 1.

```python
a = 5  # 101
b = 3  # 011
print(a | b)
print(bin(a | b))
```

**Output:**
```text
7
0b111
```

**Explanation:**  
```
  101
| 011
= 111 → 7
```

---

### 4. Bitwise XOR (`^`)

Sets each bit to 1 if **only one** bit is 1 (exclusive OR).

```python
a = 5  # 101
b = 3  # 011
print(a ^ b)
print(bin(a ^ b))
```

**Output:**
```text
6
0b110
```

**Explanation:**  
```
  101
^ 011
= 110 → 6
```

---

### 5. Bitwise NOT (`~`)

Inverts all bits (1 becomes 0, 0 becomes 1).

```python
a = 5
print(~a)
```

**Output:**
```text
-6
```

**Explanation:**  
In Python, integers are stored using **two’s complement** representation for negative numbers.

Formula:  
`~n = -(n + 1)`

So:
```
~5 = -(5 + 1) = -6
```

---

### 6. Left Shift (`<<`)

Shifts bits to the **left**, adding zeros on the right.

```python
a = 5  # 101
print(a << 1)
print(bin(a << 1))
print(a << 2)
```

**Output:**
```text
10
0b1010
20
```

**Explanation:**  
Each left shift multiplies the number by 2.  
`a << n` → `a * (2ⁿ)`

```
  101  (5)
<< 1 → 1010 (10)
```

---

### 7. Right Shift (`>>`)

Shifts bits to the **right**, removing bits from the right side.

```python
a = 5  # 101
print(a >> 1)
print(bin(a >> 1))
print(a >> 2)
```

**Output:**
```text
2
0b10
1
```

**Explanation:**  
Each right shift divides the number by 2 (integer division).  
`a >> n` → `a // (2ⁿ)`

```
  101  (5)
>> 1 → 10 (2)
```

---

### 8. Bitwise Operations with Negative Numbers

```python
a = -10
b = 4
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
```

**Output:**
```text
4
-10
-14
9
```

**Explanation:**  
Negative numbers are stored in **two’s complement**, so their binary representation differs.  
You usually don’t deal with bitwise operations on negatives unless you know binary-level details.

---

### 9. Bitwise Operators in Conditional Logic

Bitwise operators can be used in **boolean logic**, but it’s recommended to use logical operators (`and`, `or`, `not`) instead.

```python
print(True & False)  # 0 (acts like AND)
print(True | False)  # 1 (acts like OR)
print(True ^ True)   # 0 (acts like XOR)
```

**Output:**
```text
False
True
False
```

✅ Still works, but **less readable** than logical operators.

---

### Practical Examples

### Example 1: Check if a Number is Even or Odd

You can check the **last bit**:
```python
num = 7
if num & 1:
    print("Odd")
else:
    print("Even")
```

**Output:**
```text
Odd
```

**Explanation:**  
Last bit of an odd number is always `1`.

---

### Example 2: Swapping Two Numbers Without Temporary Variable

```python
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
```

**Output:**
```text
10 5
```

**Explanation:**  
XOR properties allow swapping values without extra storage.

---

### Example 3: Turn a Specific Bit On (Set)

```python
num = 8  # 1000
position = 1
num = num | (1 << position)
print(bin(num))
```

**Output:**
```text
0b1010
```

**Explanation:**  
Bitwise OR sets the bit at the specified position.

---

### Example 4: Turn a Specific Bit Off (Clear)

```python
num = 10  # 1010
position = 1
num = num & ~(1 << position)
print(bin(num))
```

**Output:**
```text
0b1000
```

---

### Example 5: Toggle a Bit

```python
num = 10  # 1010
position = 1
num = num ^ (1 << position)
print(bin(num))
```

**Output:**
```text
0b1000
```

---

### Summary Table

| Operator | Name | Description | Example | Result |
|-----------|------|--------------|----------|---------|
| `&` | Bitwise AND | 1 if both bits are 1 | `5 & 3` | `1` |
| `|` | Bitwise OR | 1 if any bit is 1 | `5 | 3` | `7` |
| `^` | Bitwise XOR | 1 if only one bit is 1 | `5 ^ 3` | `6` |
| `~` | Bitwise NOT | Inverts all bits | `~5` | `-6` |
| `<<` | Left Shift | Shifts bits left | `5 << 1` | `10` |
| `>>` | Right Shift | Shifts bits right | `5 >> 1` | `2` |

---

### Key Takeaways

- Bitwise operators work directly on binary digits.  
- Useful for optimization, encryption, and bit manipulation.  
- `~n` = `-(n + 1)` (Two’s complement).  
- Left shift (`<<`) → Multiply by 2.  
- Right shift (`>>`) → Divide by 2.  
- Avoid bitwise operations on negative numbers unless necessary.  
- Use `and`, `or`, `not` for Boolean logic instead of bitwise `&`, `|`, `^`.

---
