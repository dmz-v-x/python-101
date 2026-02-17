## Shallow Copy vs Deep Copy

In Python, **copying objects** does not always mean duplicating everything inside them.

There are **two types of copies**:

| Copy Type | What It Copies |
|---------|---------------|
| Shallow Copy | Copies the outer object only (references inside stay the same) |
| Deep Copy | Copies everything recursively (fully independent copy) |

These concepts become **critical** when working with **nested mutable objects**.

---

## Mental Model (Very Important)

Think of objects like **boxes**:

- Shallow copy → New box, **same items inside**
- Deep copy → New box, **new items inside**

---

## Shallow Copy

### What is a Shallow Copy?

A **shallow copy**:
- Creates a **new outer object**
- Copies **references** to inner objects
- Inner mutable objects are **shared**

---

### Example 1: Shallow Copy with Simple List

```python
import copy

original_list = [1, 2, 3]
shallow_copy = copy.copy(original_list)

shallow_copy[1] = 99

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
```

**Output:**
```text
Original List: [1, 2, 3]
Shallow Copy: [1, 99, 3]
```

No issue here because integers are **immutable**

---

### Example 2: Shallow Copy with Nested List

```python
import copy

original_list = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_list)

shallow_copy[0][1] = 99

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
```

**Output:**
```text
Original List: [[1, 99], [3, 4]]
Shallow Copy: [[1, 99], [3, 4]]
```

**Why did original change?**

Because:
- Inner lists are **shared**
- Shallow copy copies references, not inner objects

---

## Deep Copy

### What is a Deep Copy?

A **deep copy**:
- Creates a new outer object
- Recursively copies **all nested objects**
- Fully **independent** from the original

---

### Example 3: Deep Copy with Nested List

```python
import copy

original_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original_list)

deep_copy[0][1] = 99

print("Original List:", original_list)
print("Deep Copy:", deep_copy)
```

**Output:**
```text
Original List: [[1, 2], [3, 4]]
Deep Copy: [[1, 99], [3, 4]]
```

Original remains untouched

---

## Dictionaries & Copying

---

### Example 4: Shallow Copy with Dictionary

```python
import copy

original_dict = {"a": 1, "b": [2, 3, 4]}
shallow_copy = copy.copy(original_dict)

shallow_copy["b"].append(5)

print("Original Dict:", original_dict)
print("Shallow Copy:", shallow_copy)
```

**Output:**
```text
Original Dict: {'a': 1, 'b': [2, 3, 4, 5]}
Shallow Copy: {'a': 1, 'b': [2, 3, 4, 5]}
```

Shared mutable list again

---

### Example 5: Deep Copy with Dictionary

```python
import copy

original_dict = {"a": 1, "b": [2, 3, 4]}
deep_copy = copy.deepcopy(original_dict)

deep_copy["b"].append(5)

print("Original Dict:", original_dict)
print("Deep Copy:", deep_copy)
```

**Output:**
```text
Original Dict: {'a': 1, 'b': [2, 3, 4]}
Deep Copy: {'a': 1, 'b': [2, 3, 4, 5]}
```

---

## Tuples & Copying

---

### Example 6: Shallow Copy with Tuple (Contains Mutable)

```python
import copy

original_tuple = ([1, 2], 3)
shallow_copy = copy.copy(original_tuple)

shallow_copy[0].append(99)

print("Original Tuple:", original_tuple)
print("Shallow Copy:", shallow_copy)
```

**Output:**
```text
Original Tuple: ([1, 2, 99], 3)
Shallow Copy: ([1, 2, 99], 3)
```

Tuples are immutable, but **contents may not be**

---

### Example 7: Deep Copy with Tuple

```python
import copy

original_tuple = ([1, 2], 3)
deep_copy = copy.deepcopy(original_tuple)

deep_copy[0].append(99)

print("Original Tuple:", original_tuple)
print("Deep Copy:", deep_copy)
```

**Output:**
```text
Original Tuple: ([1, 2], 3)
Deep Copy: ([1, 2, 99], 3)
```

---

## Custom Objects & Copying

---

### Example 8: Shallow Copy with Custom Object

```python
import copy

class MyClass:
    def __init__(self, data):
        self.data = data

obj1 = MyClass([1, 2, 3])
shallow_copy = copy.copy(obj1)

shallow_copy.data.append(4)

print("Original Object:", obj1.data)
print("Shallow Copy:", shallow_copy.data)
```

**Output:**
```text
Original Object: [1, 2, 3, 4]
Shallow Copy: [1, 2, 3, 4]
```

---

### Example 9: Deep Copy with Custom Object

```python
import copy

class MyClass:
    def __init__(self, data):
        self.data = data

obj1 = MyClass([1, 2, 3])
deep_copy = copy.deepcopy(obj1)

deep_copy.data.append(4)

print("Original Object:", obj1.data)
print("Deep Copy:", deep_copy.data)
```

**Output:**
```text
Original Object: [1, 2, 3]
Deep Copy: [1, 2, 3, 4]
```

---

## Common Mistakes

| Mistake | Result |
|------|------|
| Assuming copy() duplicates everything | Unexpected mutations |
| Forgetting nested mutability | Bugs in production |
| Using shallow copy for configs | Shared state issues |
| Copying objects without `deepcopy` | Data corruption |

---

## When to Use What?

| Scenario | Use |
|-------|-----|
| Flat data (no nesting) | Shallow Copy |
| Nested mutable objects | Deep Copy |
| Performance critical | Shallow Copy |
| Isolation required | Deep Copy |

---

## Summary

| Feature | Shallow Copy | Deep Copy |
|------|-------------|-----------|
| New outer object | ✅ | ✅ |
| New inner objects | ❌ | ✅ |
| Shared references | ✅ | ❌ |
| Safe for nesting | ❌ | ✅ |
| Memory usage | Low | Higher |

---

## Practice Tasks

1. Create a nested list and test both copy types  
2. Write a function showing mutation via shallow copy  
3. Create a config dictionary and protect it using deepcopy  
4. Copy a class object with nested attributes  
5. Predict outputs before running copy examples 
