## Lists in Python

A **list** in Python is a **collection data type** that can store **multiple items** in a single variable.  
Lists are one of the most powerful and flexible data structures in Python.

```python
my_list = [1, 2, 3, "apple", True, [5, 6]]
```

A list can contain **different data types** — integers, strings, booleans, and even other lists.

---

### Key Features of Lists

| Property | Description | Example |
|-----------|--------------|----------|
| Mutable | Lists can be modified after creation | `[1, 2, 3] → [10, 2, 3]` |
| Ordered | Items have a defined order that doesn’t change | `[3, 1, 4, 2]` |
| Indexable | Items can be accessed by their index | `my_list[1] → 20` |
| Heterogeneous | Can store different types of data | `[1, "apple", 3.14]` |
| Dynamic | You can add or remove items freely | `append()`, `pop()`, etc. |

---

### 1. Creating Lists

You can create lists using square brackets `[]` or the `list()` constructor.

```python
my_list = [1, 2, 3]
another_list = list(("apple", "banana", "cherry"))
```

---

### 2. Mutable (Can be Modified)

Lists are **mutable**, meaning their elements can be changed after creation.

```python
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)
```

**Output:**
```text
[10, 2, 3]
```

---

### 3. Ordered

Lists maintain the order of elements.

```python
my_list = [3, 1, 4, 2]
print(my_list)
```

**Output:**
```text
[3, 1, 4, 2]
```

---

### 4. Indexable

Each item in a list has an index (starting from 0).

```python
my_list = [10, 20, 30]
print(my_list[1])
```

**Output:**
```text
20
```

---

### 5. Heterogeneous

A list can store multiple data types.

```python
my_list = [1, "apple", 3.14, [4, 5]]
```

---

### 6. Dynamic Nature

You can add or remove elements at any time using built-in methods like `append()` or `pop()`.

---

## Common List Methods

Let’s explore commonly used **list methods** one by one.

---

### 1. `append()`
Adds an element to the end of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```

**Output:**
```text
[1, 2, 3, 4]
```

---

### 2. `extend(iterable)`
Extends the list by appending elements from another iterable (like another list).

```python
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)
```

**Output:**
```text
[1, 2, 3, 4]
```

---

### 3. `insert(index, item)`
Inserts an element at the specified index.

```python
my_list = [1, 3, 4]
my_list.insert(1, 2)
print(my_list)
```

**Output:**
```text
[1, 2, 3, 4]
```

---

### 4. `remove(item)`
Removes the first occurrence of the specified element.

```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)
```

**Output:**
```text
[1, 3, 2]
```

---

### 5. `pop([index])`
Removes and returns the element at the given index (last item by default).

```python
my_list = [1, 2, 3]
last_item = my_list.pop()
print(last_item)
print(my_list)
```

**Output:**
```text
3
[1, 2]
```

---

### 6. `index(item)`
Returns the index of the first occurrence of a given element.

```python
my_list = [10, 20, 30]
print(my_list.index(20))
```

**Output:**
```text
1
```

---

### 7. `clear()`
Removes all elements from the list.

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)
```

**Output:**
```text
[]
```

---

### 8. `count(item)`
Returns the number of times an element appears in the list.

```python
my_list = [1, 2, 2, 3]
print(my_list.count(2))
```

**Output:**
```text
2
```

---

### 9. `sort(reverse=False)`
Sorts the list in ascending order (or descending if `reverse=True`).

```python
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)
```

**Output:**
```text
[1, 2, 3, 4]
```

---

### 10. `reverse()`
Reverses the list in place.

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)
```

**Output:**
```text
[3, 2, 1]
```

---

### 11. `copy()`
Returns a shallow copy of the list.

```python
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)
```

**Output:**
```text
[1, 2, 3]
```

---

### 12. `len(list)`
Returns the number of elements in a list.

```python
my_list = [1, 2, 3]
print(len(my_list))
```

**Output:**
```text
3
```

---

### 13. `min(list)` and `max(list)`
Return the smallest and largest element in a list.

```python
my_list = [1, 2, 3]
print(min(my_list))
print(max(my_list))
```

**Output:**
```text
1
3
```

---

### 14. `sum(list)`
Returns the sum of all elements (must be numeric).

```python
my_list = [1, 2, 3]
print(sum(my_list))
```

**Output:**
```text
6
```

---

### 15. `sorted(list)`
Returns a sorted copy of the list without modifying the original.

```python
my_list = [3, 1, 2]
sorted_list = sorted(my_list)
print(sorted_list)
print(my_list)
```

**Output:**
```text
[1, 2, 3]
[3, 1, 2]
```

---

### 16. Slicing

You can extract sublists using slicing syntax.

```python
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4])
print(my_list[:3])
print(my_list[::2])
print(my_list[::-1])
```

**Output:**
```text
[1, 2, 3]
[0, 1, 2]
[0, 2, 4]
[5, 4, 3, 2, 1, 0]
```

---

### 17. Nested Lists

Lists can contain other lists, allowing multi-dimensional structures.

```python
matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

print(matrix[0])
print(matrix[1][1])
```

**Output:**
```text
[1, 2, 3]
5
```

---

### 18. List Comprehension

A compact way to create lists.

```python
squares = [x**2 for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

**Output:**
```text
[0, 1, 4, 9, 16]
[0, 2, 4, 6, 8]
```

---

### 19. Common Errors

| Error | Cause | Example |
|--------|--------|----------|
| `IndexError` | Accessing invalid index | `my_list[10]` |
| `ValueError` | Using `remove()` for non-existent item | `[1,2].remove(5)` |
| `TypeError` | Mixing non-comparable types in sort | `[1, "a"].sort()` |

---

## Summary

| Concept | Description |
|----------|--------------|
| Mutable | Can change contents after creation |
| Ordered | Maintains sequence of insertion |
| Indexable | Access elements by index |
| Heterogeneous | Supports multiple data types |
| Dynamic | Can grow or shrink dynamically |
| Common Methods | `append()`, `extend()`, `insert()`, `remove()`, etc. |
| Advanced Concepts | Slicing, Nested Lists, List Comprehension |
