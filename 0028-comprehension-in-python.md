## Comprehension in Python

A **comprehension** in Python is a **concise and expressive way** to create collections (like lists, sets, or dictionaries) from existing iterables.

Comprehensions allow you to:
- Write **less code**
- Express logic **clearly**
- Avoid boilerplate loops
- Follow a **functional programming style**

Python supports:
- List comprehensions
- Set comprehensions
- Dictionary comprehensions  
*(Tuple comprehensions don’t exist — parentheses create generators)*

---

## Why Comprehensions Exist

Before comprehensions, collection-building required verbose loops.

### Without Comprehension (Traditional Loop)

```python
squares = []
for x in range(5):
    squares.append(x * x)
```

---

### With Comprehension

```python
squares = [x * x for x in range(5)]
```

✅ Shorter  
✅ Clear intent  
✅ Fewer chances for bugs  

---

## When to Use Comprehensions

Use comprehensions when:
- You are **creating a new collection**
- Logic is **simple and readable**
- One transformation + optional condition is enough

Avoid comprehensions when:
- Logic is complex
- Multiple nested conditions reduce readability
- Side effects are involved (e.g., printing, mutation)

---

## Comprehensions vs Loops

| Feature | Comprehension | Loop |
|------|--------------|-----|
| Code length | Short | Longer |
| Readability | High (if simple) | High (if complex) |
| Performance | Slightly faster | Slightly slower |
| Side effects | ❌ Avoided | ✅ Allowed |
| Debugging | Harder | Easier |

---

## General Comprehension Syntax

```python
[expression for item in iterable if condition]
```

- `expression` → what to include
- `item` → current element
- `iterable` → source
- `if condition` → optional filter

---

# List Comprehensions

---

## 1. What is a List Comprehension?

A **list comprehension** creates a **new list** by applying an expression to each item in an iterable.

---

## 2. Basic List Comprehension

```python
numbers = [1, 2, 3, 4]
squares = [x * x for x in numbers]
print(squares)
```

**Output:**
```text
[1, 4, 9, 16]
```

---

## 3. List Comprehension with Condition

```python
numbers = range(10)
evens = [x for x in numbers if x % 2 == 0]
print(evens)
```

**Output:**
```text
[0, 2, 4, 6, 8]
```

---

## 4. List Comprehension with `if-else`

```python
numbers = range(5)
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)
```

**Output:**
```text
['Even', 'Odd', 'Even', 'Odd', 'Even']
```

`if-else` must come **before** `for`

---

## 5. Nested List Comprehension

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

flattened = [num for row in matrix for num in row]
print(flattened)
```

**Output:**
```text
[1, 2, 3, 4, 5, 6]
```

---

## 6. List Comprehension vs Loop

### Loop Version

```python
result = []
for x in range(5):
    result.append(x * 2)
```

---

### Comprehension Version

```python
result = [x * 2 for x in range(5)]
```

---

# Set Comprehensions

---

## 7. What is a Set Comprehension?

A **set comprehension** creates a **set** using comprehension syntax.

- Automatically removes duplicates
- Order is not guaranteed

---

## 8. Basic Set Comprehension

```python
numbers = [1, 2, 2, 3, 4, 4]
unique_squares = {x * x for x in numbers}
print(unique_squares)
```

**Output (order may vary):**
```text
{16, 1, 4, 9}
```

---

## 9. Set Comprehension with Condition

```python
numbers = range(10)
odd_set = {x for x in numbers if x % 2 != 0}
print(odd_set)
```

**Output:**
```text
{1, 3, 5, 7, 9}
```

---

## 10. When to Use Set Comprehensions

Use set comprehensions when:
- You want **unique values**
- Order doesn’t matter
- You want fast membership checks

---

# Dictionary Comprehensions

---

## 11. What is a Dictionary Comprehension?

A **dictionary comprehension** creates a dictionary using key-value expressions.

### Syntax

```python
{key_expression: value_expression for item in iterable if condition}
```

---

## 12. Basic Dictionary Comprehension

```python
numbers = [1, 2, 3, 4]
squares = {x: x * x for x in numbers}
print(squares)
```

**Output:**
```text
{1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 13. Dictionary Comprehension with Condition

```python
numbers = range(10)
even_squares = {x: x * x for x in numbers if x % 2 == 0}
print(even_squares)
```

**Output:**
```text
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## 14. Inverting a Dictionary

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)
```

**Output:**
```text
{1: 'a', 2: 'b', 3: 'c'}
```

---

## 15. Dictionary Comprehension vs Loop

### Loop Version

```python
result = {}
for x in range(3):
    result[x] = x * x
```

---

### Comprehension Version

```python
result = {x: x * x for x in range(3)}
```

---

## Common Mistakes & Pitfalls

| Mistake | Why It Happens |
|------|---------------|
| Overly complex comprehensions | Hurts readability |
| Using side effects | Not allowed |
| Misplacing `if-else` | Syntax confusion |
| Expecting order in sets | Sets are unordered |
| Using comprehension for debugging | Hard to inspect |

---

## Summary

| Type | Creates | Syntax |
|----|-------|-------|
| List comprehension | List | `[ ]` |
| Set comprehension | Set | `{ }` |
| Dict comprehension | Dict | `{key: value}` |
| Loop alternative | Yes | Cleaner |
| Side effects | ❌ Avoided | |

---

## Practice Tasks

1. Create a list of squares of numbers from 1 to 10 using list comprehension.  
2. Remove duplicates from a list using set comprehension.  
3. Create a dictionary mapping numbers to their cubes.  
4. Convert a list of strings to their lengths using comprehension.  
5. Rewrite a complex loop using comprehension and compare readability.
