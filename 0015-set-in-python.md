## Set in Python

A **set** in Python is an **unordered**, **mutable**, and **unindexed** collection of **unique elements**.  
Sets are used when you want to store multiple items **without duplicates**, and **order doesn’t matter**.

```python
my_set = {1, 2, 3, 4, 5}
```

**Key Properties:**
- **Unordered:** Elements have no defined order  
- **Mutable:** You can add or remove items  
- **Unique:** Duplicate elements are automatically removed  
- **Unindexed:** Elements cannot be accessed using indexes  

---

## 1. Creating Sets

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)
```

**Output:**
```text
{1, 2, 3, 4, 5}
```

---

### Empty Set

Use `set()`, not `{}`, because `{}` creates an empty dictionary.

```python
empty_set = set()
print(empty_set)
```

**Output:**
```text
set()
```

---

## 2. Sets with Different Data Types

Sets can contain different immutable data types.

```python
mixed_set = {1, "apple", (2, 3)}
print(mixed_set)
```

**Output:**
```text
{1, 'apple', (2, 3)}
```

**Invalid Example:**
```python
# invalid_set = {1, [2, 3]}  # Raises TypeError
```

**Error:**
```text
TypeError: unhashable type: 'list'
```

Reason → Lists are mutable, and mutable types **cannot** be set elements.

---

## 3. Adding and Removing Elements

| Method | Description |
|---------|--------------|
| `add(item)` | Adds an element to the set |
| `remove(item)` | Removes the element (raises error if not found) |
| `discard(item)` | Removes element if it exists (no error if not) |
| `pop()` | Removes a random element |
| `clear()` | Removes all elements |

```python
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
```

**Output:**
```text
{1, 2, 3, 4, 5, 6}
```

---

### Removing Elements

```python
my_set.remove(3)
print(my_set)
```

**Output:**
```text
{1, 2, 4, 5, 6}
```

Using `discard()` avoids errors:

```python
my_set.discard(10)
```

---

### Random Removal with `pop()`

```python
popped_item = my_set.pop()
print(popped_item)
print(my_set)
```

**Output (may vary):**
```text
1
{2, 4, 5, 6}
```

---

### Clearing the Set

```python
my_set.clear()
print(my_set)
```

**Output:**
```text
set()
```

---

## 4. Union of Sets (`union()` or `|`)

Combines all elements from both sets, removing duplicates.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
```

**Output:**
```text
{1, 2, 3, 4, 5}
```

You can also use:
```python
print(set1 | set2)
```

---

## 5. Intersection (`intersection()` or `&`)

Returns elements present in **both** sets.

```python
print(set1.intersection(set2))
print(set1 & set2)
```

**Output:**
```text
{3}
```

---

## 6. Difference (`difference()` or `-`)

Elements that exist in the first set but not in the second.

```python
print(set1.difference(set2))
print(set1 - set2)
```

**Output:**
```text
{1, 2}
```

---

## 7. Symmetric Difference (`symmetric_difference()` or `^`)

Elements that are in **either** set, but **not both**.

```python
print(set1.symmetric_difference(set2))
print(set1 ^ set2)
```

**Output:**
```text
{1, 2, 4, 5}
```

---

## 8. Subset, Superset, and Disjoint

| Method | Description | Example | Output |
|---------|--------------|----------|---------|
| `issubset()` | Checks if a set is a subset of another | `{1,2}.issubset({1,2,3})` | `True` |
| `issuperset()` | Checks if a set is a superset | `{1,2,3}.issuperset({1,2})` | `True` |
| `isdisjoint()` | Checks if sets have no common elements | `{1,2,3}.isdisjoint({4,5,6})` | `True` |

---

## 9. Copying a Set

Creates a **shallow copy** of a set.

```python
set1 = {1, 2, 3}
copy_set = set1.copy()
print(copy_set)
```

**Output:**
```text
{1, 2, 3}
```

---

## 10. Looping Through a Set

Since sets are unordered, elements may appear in random order.

```python
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)
```

**Output (order may vary):**
```text
1
2
3
4
5
```

---

## 11. Working with Immutable Sets (`frozenset`)

A **frozenset** is an immutable version of a set — its contents cannot be changed.

```python
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)
```

**Output:**
```text
frozenset({1, 2, 3, 4})
```

Attempting to modify it will raise an error:

```python
# frozen_set.add(5)
```

**Error:**
```text
AttributeError: 'frozenset' object has no attribute 'add'
```

---

## 12. Removing Duplicates Using Sets

A common use-case of sets is to remove duplicates from lists.

```python
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)
```

**Output:**
```text
{1, 2, 3, 4, 5}
```

---

## Common Errors

| Error | Cause | Example |
|--------|--------|----------|
| `TypeError` | Adding mutable elements (like lists/dicts) | `{[1,2,3]}` |
| `KeyError` | Removing non-existent element with `.remove()` | `{1,2}.remove(5)` |
| `AttributeError` | Modifying a `frozenset` | `frozenset({1,2}).add(3)` |

---

## Summary

| Feature | Description |
|----------|--------------|
| **Unordered** | Elements do not have a fixed position |
| **Mutable** | You can add or remove elements |
| **Unique** | No duplicate elements allowed |
| **Unindexed** | Cannot access elements by index |
| **Supports Operations** | Union, intersection, difference, etc. |
| **Immutable Version** | `frozenset` |

---

## Practice Tasks

1. Create a set of favorite movies and add a new one using `.add()`.  
2. Find the intersection of `{1, 2, 3}` and `{3, 4, 5}` using both methods (`&` and `.intersection()`).  
3. Remove duplicates from `[10, 20, 10, 30, 20, 40]` using a set.  
4. Check if `{1, 2}` is a subset of `{1, 2, 3, 4}`.  
5. Create a `frozenset` and attempt to add a new element — observe the error.  
