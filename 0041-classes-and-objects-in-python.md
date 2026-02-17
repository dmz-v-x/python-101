## Classes & Objects in Python

In Python:

👉 **Class = Blueprint**  
👉 **Object = Instance created from blueprint**

A class defines:

✔ Data (attributes)  
✔ Behavior (methods)

An object is the **actual entity in memory**.

---

## Mental Model (CRITICAL)

Think of:

- Class → Design of a Car 🚗  
- Object → Actual Car Built

You can build many objects from one class.

---

## 1. Creating a Class

A class is defined using the `class` keyword.

```python
class Person:
    pass
```

`pass` means “empty placeholder”

---

## 2. Creating an Object (Instance)

Objects are created by calling the class like a function.

```python
p1 = Person()
p2 = Person()
```

Each object:

✔ Lives in memory  
✔ Has a unique identity  

```python
print(id(p1))
print(id(p2))
```

---

## 3. Attributes — Object Data

Attributes are variables stored inside objects.

---

### Instance Attributes

Defined inside the constructor.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

```python
p1 = Person("Alice", 25)

print(p1.name)
print(p1.age)
```

**Output:**
```text
Alice
25
```

Each object gets its own copy.

---

### Class Attributes (Shared)

Defined directly inside the class.

```python
class Person:
    species = "Human"
```

```python
p1 = Person()
p2 = Person()

print(p1.species)
print(p2.species)
```

Shared across all objects.

---

## Instance vs Class Attribute

| Feature | Instance Attribute | Class Attribute |
|----------|--------------------|----------------|
| Belongs To | Object | Class |
| Shared? | ❌ No | ✅ Yes |
| Memory | Per object | Single copy |

---

## 4. Methods — Object Behavior

Methods are functions defined inside classes.

```python
class Person:
    def greet(self):
        print("Hello!")
```

```python
p1 = Person()
p1.greet()
```

---

## What Really Happens?

```text
p1.greet() → Person.greet(p1)
```

Python automatically passes the object.

---

## 5. The `self` Keyword (ABSOLUTELY CRITICAL)

`self` refers to:

👉 **The current object calling the method**

```python
class Person:
    def greet(self):
        print(self)
```

---

## 6. Constructor — `__init__`

Constructor runs automatically during object creation.

```python
class Person:
    def __init__(self):
        print("Object created!")
```

```python
p1 = Person()
```

**Output:**
```text
Object created!
```

---

## 7. Object State (Why Objects Exist)

Objects store **state (data)**.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
```

```python
c1 = Counter()
c1.increment()
c1.increment()

print(c1.count)
```

**Output:**
```text
2
```

---

## 8. Dynamic Attribute Creation

Python allows attributes to be added dynamically.

```python
class Person:
    pass

p1 = Person()
p1.name = "Alice"

print(p1.name)
```

Flexible but dangerous in large systems.

---

## 9. Inspecting Object Internals

---

### View Object Attributes

```python
print(p1.__dict__)
```

Shows stored data.

---

### View Class Attributes

```python
print(Person.__dict__)
```

---

## 10. Method Types

---

### Instance Method (Default)

```python
def method(self)
```

Works with objects.

---

### Class Method

Works with class itself.

```python
@classmethod
def method(cls)
```

---

### Static Method

No object / class access.

```python
@staticmethod
def method()
```

---

## Why Different Method Types Exist?

| Method Type | Access |
|-------------|--------|
| Instance Method | Object data |
| Class Method | Class data |
| Static Method | Utility logic |

---

## 11. Object Identity & Equality

---

### Identity (`is`)

Checks memory location.

```python
a = [1, 2]
b = a

print(a is b)
```

**Output:**
```text
True
```

---

### Equality (`==`)

Checks values.

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

**Output:**
```text
True
False
```

---

## 12. Object Lifecycle

Objects:

✔ Created → `__init__()`  
✔ Used → Methods  
✔ Destroyed → Garbage Collector

---

## 13. Memory Behavior

Each object:

✔ Separate identity  
✔ Separate instance attributes  

Class attributes → Shared memory

---

## Common Errors

| Error | Cause |
|--------|--------|
| `TypeError: missing self` | Forgot `self` parameter |
| `AttributeError` | Accessing non-existent attribute |
| Overwriting class attribute | Accidentally shadowing |
| Mutable class attributes bug | Shared mutation |

---

### Dangerous Bug: Mutable Class Attribute

```python
class Person:
    hobbies = []
```

```python
p1 = Person()
p2 = Person()

p1.hobbies.append("Coding")

print(p2.hobbies)
```

**Output:**
```text
['Coding']
```

🚨 Shared across objects → subtle bug

---

## Best Practices

✔ Use instance attributes for object data  
✔ Avoid mutable class attributes  
✔ Always include `self`  
✔ Use constructor for initialization  
✔ Keep responsibilities clear

---

## Summary

| Concept | Meaning |
|----------|------------|
| Class | Blueprint |
| Object | Instance |
| Instance Attribute | Per object data |
| Class Attribute | Shared data |
| Method | Behavior |
| self | Current object |
| __init__ | Constructor |
| __dict__ | Internal storage |

---

## Practice Tasks

1. Create a `Car` class with attributes & methods  
2. Create multiple objects & compare identities  
3. Implement instance vs class attributes  
4. Demonstrate mutable class attribute bug  
5. Inspect `__dict__`  
6. Write class method & static method  
7. Build stateful object (Counter, BankAccount)  
