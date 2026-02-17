## Classes & Object Namespace in Python

In Python, both:

✔ Classes  
✔ Objects  

Have their **own separate namespaces**.

A **namespace** is simply:

👉 A container that stores variables.

---

## What is a Namespace?

A namespace is like a **dictionary of variables**.

Python internally stores variables using mappings.

Example:

```python
print(object.__dict__)
print(Class.__dict__)
```

---

## Critical Mental Model

Think of:

✔ Object → Personal Storage  
✔ Class → Shared Storage

Each has **independent memory containers**.

---

## 1. Object (Instance) Namespace

Stores:

✔ Instance variables  
✔ Object-specific data  

Accessible via:

```python
object.__dict__
```

---

### Example

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p = Person("Alice")

print(p.__dict__)
```

**Output:**
```text
{'name': 'Alice'}
```

📌 Stored inside object namespace

---

## 2. Class Namespace

Stores:

✔ Class variables  
✔ Methods  
✔ Static data  

Accessible via:

```python
Class.__dict__
```

---

### Example

```python
class Person:
    species = "Human"

    def greet(self):
        print("Hello")
```

```python
print(Person.__dict__)
```

📌 Contains:

✔ species  
✔ greet  
✔ __init__  
✔ Other internal attributes

---

## Namespace Separation (VERY IMPORTANT)

| Namespace | Stores |
|------------|------------|
| Object Namespace | Instance variables |
| Class Namespace | Methods + class variables |

They are **completely independent containers**.

---

## 3. Attribute Lookup Rule 

When accessing:

```python
object.attribute
```

Python searches in this order:

```text
1. Object Namespace
2. Class Namespace
3. Parent Class Namespace (Inheritance)
```

---

## Example: Lookup Behavior

```python
class Demo:
    x = 10

d = Demo()
print(d.x)
```

✔ Not found in object  
✔ Found in class

---

## 4. Shadowing Explained

When you assign via object:

```python
d.x = 99
```

Python creates:

✔ NEW variable in object namespace

---

### Example

```python
class Demo:
    x = 10

d = Demo()
d.x = 99

print(d.__dict__)
print(Demo.__dict__['x'])
```

**Output:**
```text
{'x': 99}
10
```

Class variable untouched

---

## Critical Insight

```text
Object variables OVERRIDE class variables
```

But only via **lookup priority**, not mutation.

---

## 5. Methods Live in Class Namespace

Methods are stored in:

✔ Class namespace

---

### Example

```python
class Demo:
    def greet(self):
        print("Hello")
```

```python
print(Demo.__dict__)
```

✔ greet stored here

---

## Why Objects Can Call Methods?

Because Python lookup finds methods in class namespace.

```text
d.greet() → Demo.greet(d)
```

---

## 6. Object Namespace Grows Dynamically

Python allows dynamic attribute creation.

```python
d.new_var = 123
print(d.__dict__)
```

---

## 7. Subtle Bug Generator

---

### Mutable Class Variable Nightmare

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

Because hobbies stored in **class namespace**

---

## Why This Happens

Lookup finds hobbies in class namespace.

Mutation modifies shared memory.

---

## 8. Inspecting Namespaces (Master Skill)

---

### Object Namespace

```python
print(obj.__dict__)
```

---

### Class Namespace

```python
print(Class.__dict__)
```

---

## 9. Lookup Visualization

```text
obj.attribute
   ↓
Object Namespace?
   ↓
Class Namespace?
   ↓
Parent Classes?
```

---

## 10. Common Beginner Confusions 

| Confusion | Reality |
|--------------|------------|
| Object stores methods? | ❌ No |
| Class stores instance data? | ❌ No |
| Same variable name means mutation? | ❌ |
| Assignment via object modifies class? | ❌ |
| Namespace = scope? | ❌ Different concept |

---

## Namespace vs Scope (Important Distinction)

| Concept | Meaning |
|-----------|-------------|
| Namespace | Where variables are stored |
| Scope | Where variables are accessible |

---

## Best Practices

✔ Instance variables → Object namespace  
✔ Shared constants → Class namespace  
✔ Avoid mutable class variables  
✔ Understand lookup order  
✔ Use namespaces intentionally  

---

## Summary

| Concept | Truth |
|-------------|------------|
| Namespace | Variable container |
| Object Namespace | Instance storage |
| Class Namespace | Methods + shared data |
| Lookup Order | Object → Class |
| Shadowing | Object overrides class |
| Methods Stored In | Class namespace |

---

## Practice Tasks

1. Print object vs class namespaces  
2. Create shadowing examples  
3. Inspect __dict__ contents  
4. Add dynamic attributes  
5. Trigger mutable class variable bug  
6. Predict lookup behavior  
7. Rename attributes & observe effects  
