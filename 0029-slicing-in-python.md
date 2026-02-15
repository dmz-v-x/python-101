## Slicing in Python

**Slicing** in Python is a technique used to **extract a portion (slice)** of a sequence.

Python supports slicing on **sequence types**, such as:
- Lists
- Strings
- Tuples
- Ranges  
*(Sets do not support slicing directly)*

Slicing allows you to:
- Extract subsets
- Reverse sequences
- Skip elements
- Modify lists efficiently

---

## General Slicing Syntax

```python
sequence[start:stop:step]
```

| Component | Meaning |
|--------|--------|
| `start` | Index to start from (inclusive) |
| `stop` | Index to stop at (exclusive) |
| `step` | How many elements to skip |

All three are **optional**  
Default `step` = `1`

---

## 1. Slicing Lists

```python
my_list = [10, 20, 30, 40, 50, 60]
```

---

### Slice from Index 1 to 4

```python
sublist = my_list[1:4]
print(sublist)
```

**Output:**
```text
[20, 30, 40]
```

---

### Slice the Entire List

```python
full_list = my_list[:]
print(full_list)
```

**Output:**
```text
[10, 20, 30, 40, 50, 60]
```

---

### Slice with Step

```python
step_list = my_list[::2]
print(step_list)
```

**Output:**
```text
[10, 30, 50]
```

Every 2nd element is selected

---

## 2. Slicing Strings

Strings are **immutable**, but slicing works the same way.

```python
my_string = "Python Programming"
```

---

### Basic String Slice

```python
sub_string = my_string[0:6]
print(sub_string)
```

**Output:**
```text
Python
```

---

### Slice with Step

```python
step_string = my_string[::2]
print(step_string)
```

**Output:**
```text
Pto rgamn
```

---

### Reverse a String

```python
reverse_string = my_string[::-1]
print(reverse_string)
```

**Output:**
```text
gnimmargorP nohtyP
```

---

## 3. Slicing Tuples

Tuples are immutable, but slicing is allowed.

```python
my_tuple = (1, 2, 3, 4, 5, 6)
```

---

### Slice a Tuple

```python
sub_tuple = my_tuple[2:5]
print(sub_tuple)
```

**Output:**
```text
(3, 4, 5)
```

---

### Slice with Step

```python
step_tuple = my_tuple[::2]
print(step_tuple)
```

**Output:**
```text
(1, 3, 5)
```

---

### Reverse a Tuple

```python
reverse_tuple = my_tuple[::-1]
print(reverse_tuple)
```

**Output:**
```text
(6, 5, 4, 3, 2, 1)
```

---

## 4. Slicing Sets (Indirectly)

Sets **do not support slicing** because they are **unordered**.

```python
my_set = {10, 20, 30, 40, 50}
```

Convert to list first:

```python
set_as_list = list(my_set)
print(set_as_list[:3])
```

**Output (order may vary):**
```text
[10, 20, 30]
```

---

## 5. Slicing `range()`

`range` objects are iterable but not sliceable directly.

```python
my_range = range(10)
```

Convert to list first:

```python
sub_range = list(my_range)[2:7]
print(sub_range)
```

**Output:**
```text
[2, 3, 4, 5, 6]
```

---

## 6. Negative Indexing in Slicing

Python supports **negative indexing**, where:
- `-1` → last element
- `-2` → second last element

---

### Example

```python
my_list = [10, 20, 30, 40, 50]
```

---

### Last Two Elements

```python
negative_slice = my_list[-2:]
print(negative_slice)
```

**Output:**
```text
[40, 50]
```

---

### All Except Last Element

```python
all_but_last = my_list[:-1]
print(all_but_last)
```

**Output:**
```text
[10, 20, 30, 40]
```

---

### Reverse Using Negative Step

```python
reverse_list = my_list[::-1]
print(reverse_list)
```

**Output:**
```text
[50, 40, 30, 20, 10]
```

---

## 7. Omitting `start`, `stop`, or `step`

```python
my_list = [1, 2, 3, 4, 5]
```

---

### Omit `start`

```python
print(my_list[:3])
```

**Output:**
```text
[1, 2, 3]
```

---

### Omit `stop`

```python
print(my_list[2:])
```

**Output:**
```text
[3, 4, 5]
```

---

### Omit All

```python
print(my_list[::])
```

**Output:**
```text
[1, 2, 3, 4, 5]
```

---

## 8. Modifying Lists Using Slices

This works **only for mutable sequences like lists**.

```python
my_list = [1, 2, 3, 4, 5]
```

---

### Replace Elements

```python
my_list[0:2] = [10, 20]
print(my_list)
```

**Output:**
```text
[10, 20, 3, 4, 5]
```

---

### Remove Elements

```python
my_list[1:3] = []
print(my_list)
```

**Output:**
```text
[10, 4, 5]
```

---

### Insert Elements

```python
my_list[1:1] = [30, 40]
print(my_list)
```

**Output:**
```text
[10, 30, 40, 4, 5]
```

---

## Common Mistakes & Pitfalls

| Mistake | Why It Happens |
|------|---------------|
| Expecting slicing to modify strings | Strings are immutable |
| Slicing sets directly | Sets are unordered |
| Off-by-one errors | `stop` index is exclusive |
| Overusing complex slices | Hurts readability |
| Forgetting step direction | Negative step reverses |

---

## Summary

| Feature | Description |
|------|-------------|
| Slicing syntax | `seq[start:stop:step]` |
| Supports | Lists, strings, tuples |
| Negative index | Slice from end |
| Negative step | Reverse sequence |
| List slicing | Can modify list |
| Set slicing | ❌ Not supported |

---

## Practice Tasks

1. Reverse a string using slicing.  
2. Extract the middle three elements from a list.  
3. Remove every second element from a list using slicing.  
4. Replace the last two elements of a list using slicing.  
5. Explain why slicing doesn’t work on sets.
