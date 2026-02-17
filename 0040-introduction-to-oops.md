## Introduction to Oops

**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of **objects**.

Instead of writing code as a sequence of instructions,  
👉 we organize code around **real-world entities**.

Example:

- A Car 🚗
- A Student 🎓
- A Bank Account 💳

Each entity has:

✔ Data (attributes)  
✔ Behavior (methods)

---

## Why OOP Exists

Before OOP, programs were mostly **procedural**:

- Code = sequence of steps
- Data & logic loosely connected
- Harder to scale & maintain

OOP solves this by providing:

| Benefit | Explanation |
|----------|-------------|
| Modularity | Break programs into reusable units |
| Reusability | Reuse code via classes |
| Maintainability | Easier to modify large systems |
| Scalability | Better structure for big applications |
| Real-world modeling | Natural representation of entities |

---

## Procedural vs OOP Thinking

---

### Procedural Style

```python
name = "Alice"
age = 25

def greet():
    print(f"Hello {name}")
```

Data & logic are separate

---

### OOP Style

```python
class Person:
    def greet(self):
        print(f"Hello {self.name}")
```

Data + behavior bundled together

---

## Core Building Blocks of OOP

OOP is built from several fundamental concepts.

---

## 1. Class — The Blueprint

A **class** is like a **template / blueprint**.

👉 It defines what an object will look like.

```python
class Person:
    pass
```

📌 A class itself does nothing until objects are created.

---

## 2. Object — The Instance

An **object** is a **real entity created from a class**.

```python
p1 = Person()
```

📌 Class = design  
📌 Object = actual creation

---

## Mental Model

Class → Blueprint of a house  
Object → Actual house built from blueprint

---

## 3. Attributes — Object Data

Attributes = **variables inside objects**

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p1 = Person("Alice")
print(p1.name)
```

**Output:**
```text
Alice
```

---

## 4. Methods — Object Behavior

Methods = **functions inside classes**

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

## 5. The `self` Keyword (CRITICAL)

`self` refers to the **current object**

```python
class Person:
    def greet(self):
        print(self)
```

Python automatically passes the object

```python
p1.greet() → Person.greet(p1)
```

---

## 6. Constructor — `__init__`

Constructor = special method used to **initialize objects**

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Runs automatically when object is created

---

## Four Pillars of OOP

These are the **core principles** of OOP.

---

## 1. Encapsulation — Data Protection

Encapsulation = Bundling data + methods together

Also implies **data hiding**.

Python uses **naming conventions**:

```python
class Person:
    def __init__(self):
        self._protected = "Protected"
        self.__private = "Private"
```

| Prefix | Meaning |
|---------|----------|
| `_var` | Protected (convention) |
| `__var` | Private (name mangling) |

---

## 2. Abstraction — Hide Complexity

Abstraction = Show only necessary details

Example:

You use a car without knowing engine internals.

In Python → achieved via methods / interfaces.

---

## 3. Inheritance — Code Reuse

Inheritance = One class derives from another

```python
class Animal:
    def speak(self):
        print("Sound")
```

```python
class Dog(Animal):
    pass
```

```python
d = Dog()
d.speak()
```

✅ Dog reuses Animal behavior

---

## 4. Polymorphism — Many Forms

Polymorphism = Same interface, different behavior

```python
class Dog:
    def speak(self):
        print("Bark")
```

```python
class Cat:
    def speak(self):
        print("Meow")
```

Same method name → different results

---

## Instance Variables vs Class Variables

---

### Instance Variable (Per Object)

```python
class Person:
    def __init__(self, name):
        self.name = name
```

Each object has its own copy.

---

### Class Variable (Shared)

```python
class Person:
    species = "Human"
```

Shared by all objects.

---

## Special (Dunder) Methods

Python provides built-in magic methods.

| Method | Purpose |
|---------|----------|
| `__init__` | Constructor |
| `__str__` | String representation |
| `__len__` | Length behavior |
| `__add__` | Addition behavior |

Example:

```python
class Person:
    def __str__(self):
        return "Person Object"
```

---

## Static Methods vs Class Methods

---

### Static Method → No object access

```python
@staticmethod
def helper():
    pass
```

---

### Class Method → Access class

```python
@classmethod
def modify_class(cls):
    pass
```

---

## Composition (Has-A Relationship)

Instead of inheritance:

👉 Objects contain other objects.

Example:

Car **has an** Engine

---

## Common Beginner Confusions

| Confusion | Reality |
|------------|----------|
| Class = object | ❌ |
| `self` optional | ❌ |
| Private variables enforced strictly | ❌ (convention) |
| Inheritance always best | ❌ |
| OOP = mandatory | ❌ (depends on use case) |

---

## When Should You Use OOP?

Use OOP when:

✔ Modeling real entities  
✔ Building large systems  
✔ Need reusable components  
✔ Working with complex state  
✔ Designing scalable software

Avoid when:

✔ Small scripts  
✔ Simple linear logic  
✔ One-time utilities

---

## Summary

| Concept | Meaning |
|----------|------------|
| Class | Blueprint |
| Object | Instance |
| Attribute | Object data |
| Method | Object behavior |
| self | Current object |
| Constructor | Object initializer |
| Encapsulation | Data bundling |
| Abstraction | Hide complexity |
| Inheritance | Reuse code |
| Polymorphism | Many forms |
| Composition | Has-A relationship |

---

## Practice Tasks

1. Create a `Car` class with attributes & methods  
2. Create multiple objects from one class  
3. Implement inheritance (`Animal → Dog`)  
4. Write a class with class variables  
5. Override `__str__()`  
6. Build polymorphism example  
7. Compare composition vs inheritance  
