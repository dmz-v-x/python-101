## Mutability in Python

In Python, **mutability** refers to whether an object’s **internal state (value)** can be changed **after it is created**.

Python objects fall into two broad categories:

- **Mutable objects** → Can be changed in place
- **Immutable objects** → Cannot be changed after creation

Understanding mutability is **critical** for:
- Debugging unexpected behavior
- Writing safe functions
- Avoiding side effects
- Mastering references and memory

---

## Mutable vs Immutable (At a Glance)

| Category | Types |
|------|------|
| Mutable | `list`, `dict`, `set`, `bytearray` |
| Immutable | `int`, `float`, `str`, `tuple`, `frozenset`, `bool` |

---

## Key Mental Model (Very Important)

> **Variables do NOT store values — they store references to objects.**

- Mutable objects → Same object, same memory address
- Immutable objects → New object created on modification

---

## 1. Mutability in Lists (Mutable)

```python
my_list = [1, 2, 3]
print(id(my_list))      # Memory address before modification

my_list.append(4)
print(my_list)
print(id(my_list))      # Memory address remains the same
```

**Output:**
```text
[1, 2, 3, 4]
```

The list is modified **in place**  
No new object is created

---

## 2. Immutability in Strings

```python
my_str = "Hello"
print(id(my_str))

my_str += " World"
print(my_str)
print(id(my_str))
```

**Output:**
```text
Hello World
```

A **new string object** is created  
Original string remains unchanged

---

## 3. Lists Are Mutable

```python
my_list = [10, 20, 30]
my_list[1] = 25
print(my_list)
```

**Output:**
```text
[10, 25, 30]
```

---

## 4. Dictionaries Are Mutable

```python
my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26
my_dict["city"] = "New York"
print(my_dict)
```

**Output:**
```text
{'name': 'Alice', 'age': 26, 'city': 'New York'}
```

---

## 5. Sets Are Mutable

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)
```

**Output (order may vary):**
```text
{1, 3, 4}
```

---

## 6. Tuples Are Immutable (But Watch Closely 👀)

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ TypeError
```

---

### Mutable Objects Inside Immutable Tuples

```python
my_tuple = ([1, 2, 3], 4)
my_tuple[0][1] = 10
print(my_tuple)
```

**Output:**
```text
([1, 10, 3], 4)
```

Tuple is immutable  
The **list inside it is mutable**

---

## 7. Strings Are Immutable

```python
my_str = "hello"
new_str = my_str.replace("h", "y")

print(new_str)
print(my_str)
```

**Output:**
```text
yello
hello
```

---

## 8. Integers & Floats Are Immutable

```python
x = 10
print(id(x))

x += 1
print(id(x))
print(x)
```

**Output:**
```text
11
```

New integer object is created

---

## 9. Booleans Are Immutable

```python
b = True
print(id(b))

b = False
print(id(b))
```

`True` and `False` are separate immutable objects

---

## 10. Frozenset Is Immutable

```python
my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # ❌ AttributeError
```

---

## 11. Copying Objects (Very Important Topic)

### Shallow Copy
- Copies outer object
- Inner objects are **shared**

### Deep Copy
- Copies everything recursively
- No shared references

---

### Example

```python
import copy

original_list = [[1, 2], [3, 4]]

# Shallow copy
shallow_copy = copy.copy(original_list)
shallow_copy[0][1] = 10

print(original_list)
```

**Output:**
```text
[[1, 10], [3, 4]]
```

---

### Deep Copy

```python
deep_copy = copy.deepcopy(original_list)
deep_copy[0][1] = 5

print(original_list)
```

**Output:**
```text
[[1, 10], [3, 4]]
```

Deep copy prevents side effects

---

## Common Mutability Pitfalls

| Pitfall | Why It Happens |
|------|---------------|
| Unexpected list changes | Shared references |
| Function modifying arguments | Mutable parameters |
| Shallow copy bugs | Nested objects |
| Assuming tuple immutability is deep | Mutable elements inside |
| Using mutable default args | Very dangerous |

---

## Best Practices

✅ Use immutable types when possible  
✅ Use `deepcopy` for nested structures  
✅ Avoid mutable default arguments  
✅ Understand reference sharing  
❌ Don’t assume assignment creates copies  

---

## Summary

| Concept | Key Idea |
|------|--------|
| Mutable | Changeable in place |
| Immutable | New object created |
| `id()` | Memory identity |
| Reference | Variables point to objects |
| Shallow copy | Shared inner objects |
| Deep copy | Fully independent |

---

## Practice Tasks

1. Demonstrate how modifying a list inside a function affects the original list.  
2. Show how shallow copy behaves with nested dictionaries.  
3. Explain why tuples can “appear mutable”.  
4. Fix a bug caused by shared mutable references.  
5. Convert a mutable design into an immutable one.
