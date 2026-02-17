## Methods in Python

In Python, a **method** is simply a **function defined inside a class**.

👉 But conceptually:

✔ A method *belongs to* an object  
✔ A method operates on object/class data  
✔ Python automatically passes context (`self` / `cls`)  

---

## Mental Model

A method is just:

```text
Function + Object Binding
```

Python treats methods as **descriptors**.

Meaning:

👉 Functions become methods when accessed through instances.

---

## Function vs Method (Core Understanding)

---

## 1. Normal Function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

**Output:**
```text
Hello, Alice!
```

---

## 2. Method Inside Class

```python
class Person:
    def greet(self):
        return "Hello!"

p = Person()
print(p.greet())
```

**Output:**
```text
Hello!
```

---

## What Actually Happened?

Python internally converts:

```python
p.greet()
```

Into:

```python
Person.greet(p)
```

✔ Instance automatically passed  
✔ `self` = calling object  

---

## Why `self` Exists

---

`self` represents:

👉 The current instance calling the method.

Without `self` → Python cannot know WHICH object.

---

## Types of Methods (CRITICAL)

Python has **three types** of methods:

1. Instance Methods
2. Class Methods  
3. Static Methods  

---

## 1. Instance Methods

---

## Definition

✔ Bound to instance  
✔ Access instance data  
✔ First parameter → `self`

---

## Example

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Buddy")
d.bark()
```

**Output:**
```text
Buddy says Woof!
```

---

## Key Insight

✔ Each object has its own data  
✔ Method works on object state  

---

## Gotcha #1 — Forgetting `self`

```python
class Dog:
    def bark():   # ❌ ERROR
        print("Woof")
```

**Error:**
```text
TypeError: bark() takes 0 positional arguments but 1 was given
```

✔ Python ALWAYS passes instance

---

## 2. Class Methods

---

## Definition

✔ Bound to class  
✔ Access class data  
✔ First parameter → `cls`  
✔ Uses `@classmethod`

---

## Example

```python
class Dog:
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs

d1 = Dog("Buddy")
d2 = Dog("Max")

print(Dog.get_total_dogs())
```

**Output:**
```text
2
```

---

## Key Insight

✔ Works with shared state  
✔ No instance required  

---

## Gotcha #2 — Misunderstanding `cls`

`cls` is NOT magic.

It simply refers to:

👉 The class calling the method.

Works beautifully with inheritance 🔥

---

## Example with Inheritance

```python
class Animal:
    species = "Animal"

    @classmethod
    def get_species(cls):
        return cls.species

class Dog(Animal):
    species = "Dog"

print(Dog.get_species())
```

**Output:**
```text
Dog
```

✔ `cls` respects child class ✅🔥

---

## 3. Static Methods

---

## Definition

✔ No instance  
✔ No class  
✔ Utility logic  
✔ Uses `@staticmethod`

---

## Example

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 20))
```

**Output:**
```text
30
```

---

## Key Insight

Static methods are:

```text
Namespaced Functions
```

✔ Organization only  
✔ No binding  

---

## Gotcha #3 — Expecting Access to `self`

```python
class Test:
    x = 10

    @staticmethod
    def show():
        print(self.x)  # ❌ ERROR
```

✔ No `self` available

---

## Deep Internal Behavior 

---

## Methods are Descriptors

When accessing:

```python
obj.method
```

Python returns:

👉 Bound Method Object

---

## Demonstration

```python
class Demo:
    def greet(self):
        print("Hello")

d = Demo()

print(d.greet)
```

**Output:**
```text
<bound method Demo.greet of <__main__.Demo object>>
```

✔ Function wrapped with instance

---

## Method Binding Explained

| Access Pattern | Result |
|----------------|-------------|
| `Class.method` | Function (unbound) |
| `obj.method` | Bound Method |

---

## Example

```python
class Demo:
    def greet(self):
        print("Hello")

print(Demo.greet)     # Function
d = Demo()
print(d.greet)        # Bound Method
```

---

## Common Errors & Deadly Pitfalls

---

| Mistake | Why It Happens |
|-------------|------------------|
| Missing `self` | Python auto-passes instance |
| Calling instance method via class incorrectly | No instance provided |
| Using staticmethod when classmethod needed | No access to class |
| Hardcoding class names | Breaks inheritance |
| Shadowing class attributes | Confusing behavior |
| Mutable default arguments | VERY dangerous 🔥 |

---

## Gotcha #4 — Mutable Default Arguments 🔥🔥🔥

```python
class Test:
    def add_item(self, item, lst=[]):  # ❌ DANGEROUS
        lst.append(item)
        return lst
```

✔ Shared across calls 😱

---

## Correct Version

```python
def add_item(self, item, lst=None):
    if lst is None:
        lst = []
```

---

## Comparing Method Types

| Feature | Instance | Class | Static |
|-------------|-------------|-------------|-------------|
| Bound To | Object | Class | Nothing |
| First Param | `self` | `cls` | None |
| Access Instance Data | ✅ | ❌ | ❌ |
| Access Class Data | ✅ | ✅ | ❌ |
| Use Case | Object Behavior | Shared Behavior | Utility Logic |

---

## Summary

✔ Methods = Functions inside classes  
✔ Python auto-passes context  
✔ Three types exist  
✔ Binding mechanics matter  
✔ `super()` respects method chain  
✔ Descriptors control behavior  

---

## Practice Tasks

1. Create class with all 3 method types  
2. Demonstrate method binding  
3. Break code by removing `self`  
4. Use classmethod with inheritance  
5. Implement utility staticmethod  
6. Show mutable default argument bug  
7. Predict outputs 
