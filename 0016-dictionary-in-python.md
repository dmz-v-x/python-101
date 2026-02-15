## Dictionary in Python

A **dictionary** in Python is a **collection of key-value pairs**, where each **key** maps to a specific **value**.  
Dictionaries are:
- **Unordered** (no fixed position)
- **Mutable** (can be changed)
- **Indexed by keys** (not by position)
- **Fast for lookups** (use hashing internally)

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

**Keys** must be **unique** and **immutable** (like strings, numbers, or tuples).  
**Values** can be of **any data type** — even lists or other dictionaries.

---

## 1. Creating Dictionaries

### Empty Dictionary
```python
empty_dict = {}
print(empty_dict)
```

**Output:**
```text
{}
```

---

### Dictionary with Key-Value Pairs
```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)
```

**Output:**
```text
{'name': 'John', 'age': 30, 'city': 'New York'}
```

---

## 2. Accessing Dictionary Values

Access values using **keys** or the safer `get()` method.

```python
print(person["name"])     # Direct access
print(person.get("age"))  # Using get()
print(person.get("gender", "Not specified"))  # Default value if key missing
```

**Output:**
```text
John
30
Not specified
```

---

## 3. Modifying Dictionaries

### Adding a New Key-Value Pair
```python
person["gender"] = "Male"
print(person)
```

**Output:**
```text
{'name': 'John', 'age': 30, 'city': 'New York', 'gender': 'Male'}
```

---

### Updating an Existing Value
```python
person["age"] = 31
print(person)
```

**Output:**
```text
{'name': 'John', 'age': 31, 'city': 'New York', 'gender': 'Male'}
```

---

### Removing a Key-Value Pair
```python
del person["city"]
print(person)
```

**Output:**
```text
{'name': 'John', 'age': 31, 'gender': 'Male'}
```

---

## 4. Common Dictionary Methods

| Method | Description | Example | Output |
|--------|--------------|----------|---------|
| `keys()` | Returns all keys | `person.keys()` | `dict_keys(['name', 'age', 'gender'])` |
| `values()` | Returns all values | `person.values()` | `dict_values(['John', 31, 'Male'])` |
| `items()` | Returns key-value pairs as tuples | `person.items()` | `dict_items([('name', 'John'), ('age', 31), ('gender', 'Male')])` |
| `pop(key)` | Removes the key and returns its value | `person.pop('age')` | `31` |
| `update()` | Updates dictionary with another dictionary | `person.update({'city': 'SF'})` | Merged result |

---

### Example:
```python
person.update({"age": 32, "city": "San Francisco"})
print(person)
```

**Output:**
```text
{'name': 'John', 'gender': 'Male', 'age': 32, 'city': 'San Francisco'}
```

---

## 5. Different Types of Keys and Values

Dictionaries allow **keys and values** of different types.

```python
my_dict = {
    1: "one",
    "two": 2,
    (3, 4): [1, 2, 3],
    "nested_dict": {"a": 1, "b": 2}
}
```

**Accessing Values:**
```python
print(my_dict[1])
print(my_dict["two"])
print(my_dict[(3, 4)])
print(my_dict["nested_dict"]["a"])
```

**Output:**
```text
one
2
[1, 2, 3]
1
```

---

## 6. Lists or Tuples as Values

```python
student_scores = {
    "Alice": [85, 90, 92],
    "Bob": (88, 79, 95),
    "Charlie": [78, 81, 85]
}

print(student_scores["Alice"])
print(student_scores["Bob"][1])
```

**Output:**
```text
[85, 90, 92]
79
```

---

## 7. Tuples as Keys

Since tuples are immutable, they can be dictionary keys.

```python
coordinates = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(coordinates[(1, 2)])
```

**Output:**
```text
Point A
```

---

## 8. Looping Through a Dictionary

```python
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

**Output (order may vary):**
```text
name
gender
age
city

John
Male
32
San Francisco

name: John
gender: Male
age: 32
city: San Francisco
```

---

## 9. Dictionary Comprehension

Compact way to create dictionaries.

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)
```

**Output:**
```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 10. Nested Dictionaries

Dictionaries can contain other dictionaries.

```python
students = {
    "Alice": {"age": 24, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 23, "grade": "C"}
}

print(students["Alice"]["age"])
print(students["Charlie"]["grade"])
```

**Output:**
```text
24
C
```

---

## 11. Handling Missing Keys — `setdefault()`

Adds the key with a default value if it doesn’t exist.

```python
person.setdefault("nationality", "Unknown")
print(person)
```

**Output:**
```text
{'name': 'John', 'gender': 'Male', 'age': 32, 'city': 'San Francisco', 'nationality': 'Unknown'}
```

---

## Common Errors

| Error | Cause | Example |
|--------|--------|----------|
| `KeyError` | Accessing a non-existent key directly | `person["salary"]` |
| `TypeError` | Using a mutable object as a key | `{[1,2]: "list"}` |
| `AttributeError` | Using non-existent methods | `person.append("age")` |

---

## Summary

| Concept | Description |
|----------|--------------|
| **Key-Value Pair** | Maps unique keys to values |
| **Mutable** | Can add, remove, or modify items |
| **Unordered** | Keys are not stored in order (before Python 3.7) |
| **Hashable Keys** | Keys must be immutable (string, number, tuple) |
| **Supports Nesting** | Dictionaries can hold other dictionaries |
| **Useful Methods** | `keys()`, `values()`, `items()`, `pop()`, `update()`, `setdefault()` |

---

## Practice Tasks

1. Create a dictionary to store student names and their grades, then print all students with grade “A”.  
2. Merge two dictionaries using `.update()` and print the result.  
3. Use a dictionary comprehension to map numbers (1–5) to their cubes.  
4. Create a nested dictionary for three employees containing their name, department, and salary.  
5. Try accessing a missing key using both `[]` and `.get()` — note the difference.  
