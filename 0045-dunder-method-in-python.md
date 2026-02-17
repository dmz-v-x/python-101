## Dunder Methods in Python

**Dunder = Double Underscore**

Dunder methods are special methods in Python that:

✔ Start and end with double underscores  
✔ Are invoked automatically by Python  
✔ Define object behavior  

Example:

```python
__init__
__str__
__len__
__add__
```

They are also called:

- Magic Methods
- Special Methods

---

## What Are Dunder Methods?

Dunder methods allow your objects to behave like:

✔ Numbers  
✔ Strings  
✔ Containers  
✔ Functions  
✔ Built-in types  

They define **how objects interact with Python syntax**.

---

## Critical Mental Model

Dunder methods = **Hooks into Python's internals**

They tell Python:

👉 “What should happen when someone uses operators / built-ins on my object?”

---

## 1. Why Do Dunder Methods Exist?

Because Python is deeply object-oriented.

Even basic operations:

```python
len(obj)
obj + other
print(obj)
obj[index]
```

Internally translate into:

```python
obj.__len__()
obj.__add__(other)
obj.__str__()
obj.__getitem__(index)
```

---

## Golden Rule

```text
Python Syntax → Dunder Method Call
```

---

## 2. `__init__()` — Object Initialization

Runs when object is created.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p = Person("Alice")
```

---

## 3. `__str__()` — User-Friendly String

Controls how object appears when printed.

---

### Without __str__()

```python
class Person:
    pass
```

```python
p = Person()
print(p)
```

**Output:**
```text
<__main__.Person object at 0x...>
```

---

### With __str__()

```python
class Person:
    def __str__(self):
        return "Person Object"
```

```python
print(p)
```

**Output:**
```text
Person Object
```

---

## 4. `__repr__()` — Developer Representation

More detailed/debug-friendly representation.

```python
class Person:
    def __repr__(self):
        return "Debug View"
```

Used in:

✔ Interpreter  
✔ Debugging  
✔ Logging  

---

## Difference: __str__ vs __repr__

| Method | Purpose |
|----------|----------|
| __str__ | Human-readable |
| __repr__ | Developer/debug view |

---

## 5. `__len__()` — Length Behavior

Enables `len(obj)`.

```python
class Demo:
    def __len__(self):
        return 5
```

```python
d = Demo()
print(len(d))
```

**Output:**
```text
5
```

---

## 6. `__add__()` — Operator Overloading

Defines `+` behavior.

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
```

```python
n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
```

**Output:**
```text
30
```

---

## Operator Overloading Explained

You redefine how operators behave for custom objects.

---

## 7. `__eq__()` — Equality Behavior

Defines `==`.

```python
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age
```

```python
p1 = Person(25)
p2 = Person(25)

print(p1 == p2)
```

**Output:**
```text
True
```

---

## 8. Comparison Dunder Methods

| Method | Operator |
|----------|------------|
| __lt__ | < |
| __gt__ | > |
| __le__ | <= |
| __ge__ | >= |

---

## 9. `__getitem__()` — Indexing Behavior

Enables:

```python
obj[index]
```

---

### Example

```python
class Demo:
    def __getitem__(self, index):
        return index * 10
```

```python
d = Demo()
print(d[3])
```

**Output:**
```text
30
```

---

## 10. `__setitem__()` — Assignment via Index

Enables:

```python
obj[index] = value
```

---

## 11. `__call__()` — Function-Like Objects

Allows objects to be called like functions.

---

### Example

```python
class Demo:
    def __call__(self):
        print("Object called!")
```

```python
d = Demo()
d()
```

**Output:**
```text
Object called!
```

---

## Objects Can Behave Like Functions

Powerful abstraction technique.

---

## 12. `__contains__()` — Membership Testing

Defines:

```python
value in obj
```

---

## 13. `__iter__()` — Iteration Behavior

Allows:

```python
for item in obj
```

---

## Why This Matters

Dunder methods enable:

✔ Custom containers  
✔ Smart objects  
✔ Operator overloading  
✔ Pythonic APIs  
✔ Framework design  
✔ Advanced abstractions  

---

## Common Beginner Mistakes

| Mistake | Problem |
|------------|-------------|
| Calling dunder methods directly | Rarely needed |
| Overusing magic methods | Confusing design |
| Returning wrong types | Runtime errors |
| Forgetting return values | Bugs |
| Misunderstanding __str__ vs __repr__ | Debugging issues |

---

## Best Practices

✔ Implement only what you need  
✔ Keep behavior intuitive  
✔ Respect Python conventions  
✔ Avoid surprising operator logic  
✔ Use __repr__ for debugging  
✔ Use __str__ for UI/logging  

---

## Summary

| Concept | Truth |
|------------|----------|
| Dunder | Double underscore methods |
| Purpose | Define object behavior |
| Triggered by | Python syntax |
| Direct calls | Rare |
| Operator Overloading | Yes |
| Makes objects | Powerful & Pythonic |

---

## Practice Tasks

1. Implement custom __str__()  
2. Create object supporting len()  
3. Overload + operator  
4. Implement == comparison  
5. Create indexable object  
6. Create callable object  
7. Implement iteration behavior  
8. Compare __repr__ vs __str__ outputs  
