## Identity and Membership Operators

## 1. Identity Operators

Identity operators are used to **check if two variables refer to the same object in memory** — not just if their values are equal.

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `is` | Returns `True` if both operands refer to the same object | `x is y` | True / False |
| `is not` | Returns `True` if both operands do **not** refer to the same object | `x is not y` | True / False |

---

## Example 1: Using `is` and `is not`

```python
a = 10
b = 10
print(a is b)
print(a is not b)
```

**Output:**
```text
True
False
```

**Explanation:**  
Small integers (from -5 to 256) are **interned** (cached) by Python, meaning identical values may point to the **same memory location**.

---

## Example 2: With Larger Numbers

```python
a = 1000
b = 1000
print(a == b)
print(a is b)
```

**Output:**
```text
True
False
```

**Explanation:**  
- `==` → checks **values** → `True` (same numeric value).  
- `is` → checks **object identity** → `False` (different memory locations).  

So even if two variables *look the same*, they might not be the **same object**.

---

## Example 3: With Mutable and Immutable Types

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)   # True → Same values
print(x is y)   # False → Different memory locations
```

**Output:**
```text
True
False
```

**Explanation:**  
Lists are **mutable**, so even though they hold the same values, they occupy different memory addresses.

---

## Example 4: Assigning Same Reference

```python
a = [1, 2, 3]
b = a
print(a is b)
```

**Output:**
```text
True
```

**Explanation:**  
Here, `b` references the **same object** as `a`.  
Any modification through `b` also affects `a`.

---

## Example 5: Checking `None`

`is` is often used to check if a variable is `None`.

```python
value = None
if value is None:
    print("No value assigned")
```

**Output:**
```text
No value assigned
```

**Why `is` instead of `==`?**  
`is` checks *identity* — `None` is a **singleton** object in Python, so it’s the right way to check for it.

---

## 2. Membership Operators

Membership operators test whether a **value exists** in a **sequence** (like a string, list, tuple, set, or dictionary).

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `in` | Returns `True` if value is present in the sequence | `"a" in "apple"` | True |
| `not in` | Returns `True` if value is **not** present | `"z" not in "apple"` | True |

---

## Example 1: With Strings

```python
text = "Python is fun"
print("Python" in text)
print("Java" not in text)
```

**Output:**
```text
True
True
```

**Explanation:**  
- `"Python"` exists inside the string → `True`.  
- `"Java"` does not → `True` for `not in`.

---

## Example 2: With Lists

```python
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)
print(7 not in numbers)
```

**Output:**
```text
True
True
```

---

## Example 3: With Tuples

```python
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("mango" not in fruits)
```

**Output:**
```text
True
True
```

---

## Example 4: With Sets

```python
colors = {"red", "blue", "green"}
print("blue" in colors)
print("yellow" not in colors)
```

**Output:**
```text
True
True
```

---

## Example 5: With Dictionaries

When used with dictionaries, membership operators check **keys**, not values.

```python
student = {"name": "Alice", "age": 21}
print("name" in student)
print("Alice" in student)
```

**Output:**
```text
True
False
```

**Explanation:**  
- `"name"` is a **key** → returns `True`.  
- `"Alice"` is a **value** → returns `False`.

---

## Example 6: Nested Membership

```python
data = [[1, 2], [3, 4], [5, 6]]
print([1, 2] in data)
print(2 in data)
```

**Output:**
```text
True
False
```

**Explanation:**  
The first comparison checks **sublists** directly.  
The second comparison fails because `2` is not a **direct element** of the outer list.

---

## 3. Combining Identity and Membership Operators

You can combine both in practical scenarios:

```python
x = None
if x is None or x not in [1, 2, 3]:
    print("x is either None or not in the list")
```

**Output:**
```text
x is either None or not in the list
```

---

## 4. Difference Between `is` and `==`

| Comparison | `is` | `==` |
|-------------|------|------|
| Compares | Object identity (memory location) | Value equality |
| Returns | True if both refer to same object | True if values are same |
| Works with | All objects | All objects |
| Example | `a is b` | `a == b` |

### Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True → same values
print(a is b)  # False → different memory locations
```

---

## 5. Real-World Examples

### Checking for `None`
```python
config = None
if config is None:
    print("No configuration found")
```

### Checking User Input
```python
name = "Alice"
if "A" in name:
    print("Name starts with A")
```

### Comparing Cached Objects
```python
a = 100
b = 100
print(a is b)  # True (due to interning)
```

---

## 6. Common Mistakes

###  Mistake 1: Using `== None` instead of `is None`
```python
value = None
if value == None:  # Works, but not recommended
    print("Use 'is None' instead")
```

### Mistake 2: Confusing `in` with `==`
```python
name = "Python"
if "Py" == name:
    print("Wrong check!")   # ❌
if "Py" in name:
    print("Correct check!") # ✅
```

---

## 7. Advanced Example

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True  (same content)
print(a is b)  # True  (same object)
print(a == c)  # True  (same content)
print(a is c)  # False (different objects)
print(2 in a)  # True  (membership)
```

**Output:**
```text
True
True
True
False
True
```

---

## Summary Table

| Operator | Category | Meaning | Example | Result |
|-----------|-----------|----------|----------|--------|
| `is` | Identity | True if same object | `a is b` | True / False |
| `is not` | Identity | True if not same object | `a is not b` | True / False |
| `in` | Membership | True if element exists | `"a" in "cat"` | True |
| `not in` | Membership | True if element doesn’t exist | `"z" not in "cat"` | True |

---

## Key Takeaways

- **Identity (`is`, `is not`)** checks *object identity*, not *value equality*.  
- **Membership (`in`, `not in`)** checks *presence* of elements in sequences.  
- Use `is None` when checking for `None`.  
- Don’t confuse `==` (value) with `is` (identity).  
- Membership works on **iterable containers** (string, list, tuple, set, dict).  
- Dictionaries check **keys**, not values, for membership.
