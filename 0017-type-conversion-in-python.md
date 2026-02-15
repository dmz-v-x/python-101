## Type Conversion in Python

**Type conversion** (also called **type casting**) is the process of converting one data type into another.  
Python supports **explicit type conversion** using built-in functions like:

- `int()`
- `float()`
- `str()`
- `bool()`
- `list()`
- `tuple()`
- `set()`
- `dict()`
- `complex()`

```python
x = "10"
y = int(x)  # string → int
```

Type conversion is commonly used when:
- Taking user input
- Parsing data
- Performing calculations
- Cleaning or transforming data

---

## Key Rules of Type Conversion

| Rule | Explanation |
|------|-------------|
| Explicit | Python does NOT auto-convert between most types |
| Data must be compatible | Invalid formats raise errors |
| Some data is lost | Example: `int(3.9)` → `3` |
| Containers behave differently | Dict → list gives keys only |

---

## 1. Integer (`int`) Conversion

### From Float to Int (Decimal Truncated)

```python
float_val = 3.14
int_val = int(float_val)
print(int_val)
```

**Output:**
```text
3
```

Decimal part is **discarded**, not rounded.

---

### From String to Int (Numeric Strings Only)

```python
str_val = "42"
int_val = int(str_val)
print(int_val)
```

**Output:**
```text
42
```

Invalid string:

```python
# int("abc")
```

**Error:**
```text
ValueError: invalid literal for int()
```

---

### From Boolean to Int

```python
print(int(True))
print(int(False))
```

**Output:**
```text
1
0
```

---

## 2. Float (`float`) Conversion

### From Int to Float

```python
int_val = 10
float_val = float(int_val)
print(float_val)
```

**Output:**
```text
10.0
```

---

### From String to Float

```python
str_val = "3.14"
float_val = float(str_val)
print(float_val)
```

**Output:**
```text
3.14
```

Invalid string:

```python
# float("abc")
```

**Error:**
```text
ValueError: could not convert string to float
```

---

### From Boolean to Float

```python
print(float(True))
print(float(False))
```

**Output:**
```text
1.0
0.0
```

---

## 3. String (`str`) Conversion

### From Int, Float, Boolean

```python
print(str(123))
print(str(4.56))
print(str(True))
```

**Output:**
```text
123
4.56
True
```

---

### From List to String

```python
list_val = [1, 2, 3]
print(str(list_val))
```

**Output:**
```text
[1, 2, 3]
```

This does **not** join elements — it creates a textual representation.

---

## 4. Boolean (`bool`) Conversion

### Truthy vs Falsy Values

| Value | Result |
|------|--------|
| `0`, `0.0` | `False` |
| Empty string `""` | `False` |
| Empty list `[]` | `False` |
| Empty tuple `()` | `False` |
| Empty dict `{}` | `False` |
| Everything else | `True` |

---

### Examples

```python
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1, 2, 3]))
```

**Output:**
```text
False
True
False
True
False
True
```

---

## 5. List (`list`) Conversion

### From String

```python
str_val = "Hello"
list_val = list(str_val)
print(list_val)
```

**Output:**
```text
['H', 'e', 'l', 'l', 'o']
```

---

### From Tuple

```python
tuple_val = (1, 2, 3)
print(list(tuple_val))
```

**Output:**
```text
[1, 2, 3]
```

---

### From Set

```python
set_val = {4, 5, 6}
print(list(set_val))
```

**Output (order may vary):**
```text
[4, 5, 6]
```

---

### From Dictionary (Keys Only)

```python
dict_val = {'a': 1, 'b': 2}
print(list(dict_val))
```

**Output:**
```text
['a', 'b']
```

---

## 6. Tuple (`tuple`) Conversion

### From String

```python
str_val = "Python"
print(tuple(str_val))
```

**Output:**
```text
('P', 'y', 't', 'h', 'o', 'n')
```

---

### From List / Set / Dict

```python
print(tuple([7, 8, 9]))
print(tuple({10, 11, 12}))
print(tuple({'x': 1, 'y': 2}))
```

**Output (order may vary):**
```text
(7, 8, 9)
(10, 11, 12)
('x', 'y')
```

---

## 7. Set (`set`) Conversion

### From String (Duplicates Removed)

```python
str_val = "banana"
print(set(str_val))
```

**Output:**
```text
{'b', 'a', 'n'}
```

---

### From List / Tuple / Dict

```python
print(set([1, 2, 2, 3]))
print(set((4, 5, 5, 6)))
print(set({'apple': 1, 'orange': 2}))
```

**Output:**
```text
{1, 2, 3}
{4, 5, 6}
{'apple', 'orange'}
```

---

## 8. Dictionary (`dict`) Conversion

### From List of Tuples

```python
list_of_tuples = [('a', 1), ('b', 2)]
print(dict(list_of_tuples))
```

**Output:**
```text
{'a': 1, 'b': 2}
```

---

### From List of Lists

```python
list_of_lists = [['x', 10], ['y', 20]]
print(dict(list_of_lists))
```

**Output:**
```text
{'x': 10, 'y': 20}
```

---

Invalid conversion:

```python
# dict([1, 2, 3])
```

**Error:**
```text
ValueError: dictionary update sequence element #0 has length 1; 2 is required
```

---

## 9. Complex (`complex`) Conversion

### From Int and Float

```python
print(complex(3))
print(complex(2.5))
```

**Output:**
```text
(3+0j)
(2.5+0j)
```

---

### From Real and Imaginary Parts

```python
real = 4
imaginary = 5
print(complex(real, imaginary))
```

**Output:**
```text
(4+5j)
```

---

## Common Errors

| Error | Cause | Example |
|------|------|---------|
| `ValueError` | Invalid numeric string | `int("abc")` |
| `TypeError` | Unsupported conversion | `dict([1,2,3])` |
| Data Loss | Truncation | `int(3.9)` → `3` |
| Order Loss | Set conversions | `set([3,1,2])` |

---

## Summary

| Conversion | Notes |
|-----------|------|
| `int()` | Truncates floats |
| `float()` | Supports numeric strings |
| `str()` | Converts anything to text |
| `bool()` | Uses truthy/falsy rules |
| `list()` | Breaks iterable into elements |
| `tuple()` | Immutable version of list |
| `set()` | Removes duplicates |
| `dict()` | Needs key-value pairs |
| `complex()` | Used for complex numbers |

---

## Practice Tasks

1. Convert user input `"25"` into an integer and add 10.  
2. Convert `[1, 2, 2, 3]` into a set, then back into a list.  
3. Convert `"Python"` into a tuple and reverse it.  
4. Try converting `"3.14"` to `int` — observe the error.  
5. Create a dictionary from `[("a",1), ("b",2)]` and access value `"b"`. 
