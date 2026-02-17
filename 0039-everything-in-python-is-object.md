## Everything in Python is Object

In Python, **everything is an object**.

That means:
- Numbers
- Strings
- Lists
- Functions
- Classes
- Even `None`, `True`, and `False`

**All of them are objects in memory**.

```python
x = 10
print(type(x))
```

**Output:**
```text
<class 'int'>
```

---

## What is an Object?

An **object** in Python is a **container in memory** that holds:

1. **Identity**
2. **Type**
3. **Value**

Every object in Python **must have all three**.

---

## Core Properties of an Object

### 1. Identity (`id()`)

- Identity is a **unique memory address**
- It never changes during the lifetime of the object
- Use `id()` to check it

```python
x = 10
print(id(x))
```

If two variables have the **same id**, they point to the **same object**.

---

### 2. Type (`type()`)

- Type defines **what kind of object it is**
- Type never changes

```python
x = 10
print(type(x))
```

**Output:**
```text
<class 'int'>
```

---

### 3. Value

- Value is the **data stored inside the object**
- Value **may or may not change** depending on mutability

```python
x = 10
print(x)
```

---

## Identity vs Value (Very Important)

**Never determine mutability by value**  
Always think in terms of **identity**

---

### Example: Immutable Object (`int`)

```python
x = 10
print(id(x))

x = x + 1
print(id(x))
```

**Output:**
```text
140540492896048
140540492896080
```

Identity changed → **new object created**

---

### Example: Mutable Object (`list`)

```python
my_list = [1, 2, 3]
print(id(my_list))

my_list.append(4)
print(id(my_list))
```

**Output:**
```text
140540492912640
140540492912640
```

Same identity → **object modified in place**

---

## Object Mutability

Objects in Python fall into **two categories**:

---

### Immutable Objects

Cannot be changed **after creation**  
Any “change” creates a **new object**

| Immutable Type |
|---------------|
| `int` |
| `float` |
| `str` |
| `tuple` |
| `bool` |
| `frozenset` |
| `NoneType` |

```python
s = "hello"
print(id(s))

s = s + " world"
print(id(s))
```

New object created

---

### Mutable Objects

Can be modified **in place**  
Identity remains the same

| Mutable Type |
|-------------|
| `list` |
| `dict` |
| `set` |
| `bytearray` |

```python
data = [1, 2, 3]
print(id(data))

data.append(4)
print(id(data))
```

Same object, modified in place

---

## Identity Helps Detect Mutability

| Observation | Meaning |
|------------|---------|
| `id()` changes | Object is immutable |
| `id()` same | Object is mutable |
| Value same but id different | New object |
| Value changed, id same | In-place modification |

---

## Examples Across Data Types

---

### String (Immutable)

```python
a = "Python"
b = a.replace("P", "J")

print(id(a))
print(id(b))
```

`a` and `b` are different objects

---

### Tuple with Mutable Element

```python
t = ([1, 2], 3)
t[0].append(99)

print(t)
```

Tuple is immutable  
List inside tuple **is mutable**

---

### Dictionary (Mutable)

```python
d = {"a": 1}
print(id(d))

d["b"] = 2
print(id(d))
```

Same object modified

---

## Common Misconceptions

| Myth | Reality |
|----|--------|
| Same value = same object | ❌ |
| Value change means mutation | ❌ |
| Immutable means no change at all | ❌ |
| Tuples are always safe | ❌ (if they contain mutable items) |
| Use value to check mutability | ❌ |

---

## Why Python Uses Objects Everywhere

Python’s object model enables:
- Dynamic typing
- Memory safety
- Garbage collection
- Uniform behavior
- Powerful abstractions

---

## Summary

| Concept | Explanation |
|------|-------------|
| Everything is object | Numbers, strings, functions, classes |
| Identity | Memory address (`id()`) |
| Type | Object category (`type()`) |
| Value | Data stored inside object |
| Mutability | Whether identity changes |
| Never check value | Always check identity |

---

## Practice Tasks

1. Check `id()` before and after modifying a list  
2. Compare `id()` of two equal integers  
3. Modify a tuple containing a list  
4. Test string reassignment identity  
5. Write a function that prints id before and after change  
