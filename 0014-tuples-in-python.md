## Tuples in Python

A **tuple** in Python is an **ordered, immutable collection** of elements.  
Tuples are similar to lists, but once created, **their values cannot be changed**.  

Tuples can contain **different data types** and are often used to represent **fixed collections** of items (like coordinates, RGB values, or database records).

```python
my_tuple = (1, 2, 3, "apple", True)
```

Tuples are:
- **Ordered** → Maintain insertion order  
- **Immutable** → Cannot be modified  
- **Heterogeneous** → Can store multiple data types  
- **Iterable** → Can be looped through  

---

## Key Features of Tuples

| Property | Description | Example |
|-----------|--------------|----------|
| Ordered | Elements maintain the order in which they are added | `(1, 2, 3)` |
| Immutable | Cannot change, add, or remove items | `(1, 2, 3)` → cannot modify |
| Heterogeneous | Can store mixed data types | `(1, "apple", 3.14)` |
| Iterable | Can be iterated using loops | `for x in t: print(x)` |
| Supports Nesting | Tuples can contain other tuples/lists | `(1, (2, 3), [4, 5])` |
| Can Contain Duplicates | Yes | `(1, 2, 2, 3)` |

---

## 1. Creating Tuples

```python
# Tuple with multiple elements
my_tuple = (1, 2, 3, "apple", True)
print(my_tuple)
```

**Output:**
```text
(1, 2, 3, 'apple', True)
```

---

### Single-Element Tuple
Tuples with a single element **require a trailing comma**.

```python
single_element_tuple = (5,)
print(single_element_tuple)
```

**Output:**
```text
(5,)
```

---

### Tuple Without Parentheses
You can also create tuples **without using parentheses** (just commas).

```python
another_tuple = 10, 20, 30
print(another_tuple)
```

**Output:**
```text
(10, 20, 30)
```

---

## 2. Immutability

Tuples cannot be changed after creation.

```python
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ Error
```

**Output:**
```text
TypeError: 'tuple' object does not support item assignment
```

---

## 3. Ordered and Indexable

Tuples maintain order and support indexing.

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple[1])
print(my_tuple[-1])
```

**Output:**
```text
2
4
```

---

## 4. Heterogeneous

Tuples can store multiple types of data.

```python
my_tuple = (1, "apple", 3.14, True)
```

---

## 5. Iterable

You can loop through a tuple easily.

```python
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
```

**Output:**
```text
1
2
3
```

---

## 6. Duplicate Elements

Tuples can contain repeated elements.

```python
my_tuple = (1, 2, 2, 3, 4)
```

---

## 7. Nested Tuples

Tuples can contain other tuples or lists.

```python
nested_tuple = (1, (2, 3), [4, 5])
print(nested_tuple[1])
```

**Output:**
```text
(2, 3)
```

---

## 8. Common Tuple Methods

### `count()`
Counts how many times a value occurs.

```python
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))
```

**Output:**
```text
3
```

---

### `index()`
Returns the index of the first occurrence of a value.

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple.index(3))
```

**Output:**
```text
2
```

---

## 9. Tuple Operations

### Concatenation
Combine two tuples using the `+` operator.

```python
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)
```

**Output:**
```text
(1, 2, 3, 4)
```

---

### Repetition
Repeat tuple elements using `*`.

```python
my_tuple = (1, 2)
print(my_tuple * 3)
```

**Output:**
```text
(1, 2, 1, 2, 1, 2)
```

---

## 10. Slicing Tuples

Tuples support slicing just like lists.

```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])
print(my_tuple[::-1])
```

**Output:**
```text
(2, 3, 4)
(5, 4, 3, 2, 1)
```

---

## 11. Membership Operator

```python
my_tuple = (1, 2, 3)
print(2 in my_tuple)
print(4 in my_tuple)
```

**Output:**
```text
True
False
```

---

## 12. Tuple Unpacking

Unpack tuple elements into variables.

```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)
```

**Output:**
```text
1 2 3
```

---

## 13. Tuple with Mixed Data Types

```python
my_tuple = (1, "hello", 3.14, [4, 5], (6, 7))
print(my_tuple)
```

**Output:**
```text
(1, 'hello', 3.14, [4, 5], (6, 7))
```

---

## 14. Built-in Functions

| Function | Description | Example | Output |
|-----------|--------------|----------|---------|
| `len()` | Returns number of elements | `len((1, 2, 3))` | `3` |
| `max()` | Returns largest element | `max((1, 5, 3))` | `5` |
| `min()` | Returns smallest element | `min((1, 5, 3))` | `1` |
| `sum()` | Adds all numeric elements | `sum((1, 2, 3))` | `6` |
| `sorted()` | Returns a sorted list | `sorted((3, 1, 2))` | `[1, 2, 3]` |

---

## 15. Converting Other Iterables to Tuple

You can convert lists, strings, or sets to tuples using the `tuple()` constructor.

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)
```

**Output:**
```text
(1, 2, 3)
```

---

## Common Errors

| Error | Cause | Example |
|--------|--------|----------|
| `TypeError` | Trying to modify tuple elements | `(1,2,3)[0] = 5` |
| `ValueError` | Using `index()` for non-existent items | `(1,2,3).index(5)` |
| `TypeError` | Using `sum()` on non-numeric elements | `sum((1, "a", 3))` |

---

## Summary

| Concept | Description |
|----------|--------------|
| Immutable | Cannot be changed after creation |
| Ordered | Elements have a defined order |
| Heterogeneous | Can store multiple data types |
| Supports Nesting | Tuples can include other tuples/lists |
| Efficient | Faster and memory-optimized compared to lists |
| Use Case | Suitable for fixed data that shouldn’t change |

---

## Practice Tasks

1. Create a tuple with 5 favorite fruits and print the second and last one.  
2. Write a Python program to find the number of times an element appears in a tuple.  
3. Create two tuples and concatenate them.  
4. Convert a list of numbers into a tuple and find its max and min values.  
5. Unpack a tuple into three variables and print them individually.
