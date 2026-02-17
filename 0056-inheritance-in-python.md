## Inheritance in Python

**Inheritance** is one of the core pillars of **Object-Oriented Programming (OOP)**.

Inheritance allows a **child class** to:

✔ Reuse code from a **parent class**  
✔ Extend or override behavior  
✔ Create logical relationships between classes  

In Python:

```text
Inheritance = "IS-A" relationship
```

Example:

```text
Dog IS-A Animal
Car IS-A Vehicle
```

---

## Mental Model

Inheritance means:

```text
Child class automatically gets everything from Parent class
```

Unless:
✔ It overrides something  
✔ It blocks access  

---

## Basic Syntax of Inheritance

---

```python
class Parent:
    pass

class Child(Parent):
    pass
```

✔ `Parent` → Base / Super class  
✔ `Child` → Derived / Sub class  

---

## Example: Basic Inheritance

---

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

**Output:**
```text
Animal speaks
```

---

## What Happened Internally?

Python lookup order:

```text
1. Dog instance
2. Dog class
3. Animal class
4. object
```

---

## Why Use Inheritance?

---

✔ Avoid code duplication  
✔ Improve maintainability  
✔ Create logical hierarchies  
✔ Enable polymorphism  
✔ Promote extensibility  

---

## Types of Inheritance in Python

Python supports **ALL major inheritance types**.

---

## 1. Single Inheritance

---

```python
class Parent:
    def show(self):
        print("From Parent")

class Child(Parent):
    pass
```

✔ One parent  
✔ One child  

---

## 2. Multilevel Inheritance

---

```python
class A:
    def show_a(self):
        print("A")

class B(A):
    def show_b(self):
        print("B")

class C(B):
    def show_c(self):
        print("C")

c = C()
c.show_a()
c.show_b()
c.show_c()
```

**Output:**
```text
A
B
C
```

✔ Inheritance chain  
✔ All ancestors accessible  

---

## 3. Multiple Inheritance

---

```python
class Father:
    def skill(self):
        print("Gardening")

class Mother:
    def skill(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
```

**Output:**
```text
Gardening
```

✔ Left-to-right priority  
✔ Controlled by MRO  

---

## 4. Hierarchical Inheritance

---

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

✔ One parent  
✔ Multiple children  

---

## 5. Hybrid Inheritance

Combination of:

✔ Multiple  
✔ Multilevel  
✔ Hierarchical  

Handled safely using **MRO**.

---

## Method Resolution Order (MRO)

---

MRO defines:

```text
Exact order Python uses to search methods
```

---

## Check MRO

```python
print(ClassName.__mro__)
```

---

## Example

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.__mro__)
```

**Output:**
```text
(D, B, C, A, object)
```

✔ Python uses **C3 Linearization**  
✔ Predictable & safe  

---

## `super()` and Inheritance (VERY IMPORTANT)

---

`super()` allows a child class to call parent class methods **without hardcoding class names**.

---

## Example

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()
```

**Output:**
```text
Hello from Parent
Hello from Child
```

---

## Why `super()` Matters

✔ Supports multiple inheritance  
✔ Respects MRO  
✔ Prevents duplication  
✔ Cleaner design  

---

## Constructor Inheritance (`__init__`)

---

## Example Without `super()`

```python
class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        print("Child init")

c = Child()
```

**Output:**
```text
Child init
```

Parent constructor NOT called

---

## Correct Way

```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")
```

**Output:**
```text
Parent init
Child init
```

---

## Attribute Inheritance

---

```python
class Parent:
    x = 10

class Child(Parent):
    pass

print(Child.x)
```

**Output:**
```text
10
```

✔ Class attributes inherited  
✔ Instance attributes NOT shared  

---

## Attribute Shadowing Gotcha

---

```python
class Parent:
    x = 10

class Child(Parent):
    x = 20

print(Child.x)
```

**Output:**
```text
20
```

✔ Child shadows parent attribute  

---

## Method Overriding

---

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()
```

**Output:**
```text
Bark
```

✔ Child overrides parent  

---

## Overriding + `super()`

---

```python
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")
```

✔ Extends behavior instead of replacing  

---

## Common Inheritance Pitfalls

---

| Mistake | Problem |
|-------|--------|
| Hardcoding parent calls | Breaks MRO |
| Forgetting `super()` | Partial initialization |
| Overusing inheritance | Tight coupling |
| Deep inheritance trees | Hard to maintain |
| Conflicting methods | Unexpected behavior |

---

## Composition vs Inheritance

---

Inheritance:

```text
IS-A relationship
```

Composition:

```text
HAS-A relationship
```

---

## Prefer Composition When:

✔ Behavior changes frequently  
✔ Avoid tight coupling  
✔ Reuse logic flexibly  

---

## Best Practices

---

✔ Favor composition over inheritance  
✔ Keep hierarchies shallow  
✔ Always use `super()`  
✔ Understand MRO  
✔ Avoid unnecessary overrides  
✔ Design for extension, not modification  

---

## Summary

✔ Inheritance enables code reuse  
✔ Python supports multiple inheritance  
✔ MRO defines lookup order  
✔ `super()` is essential  
✔ Overriding enables polymorphism  
✔ Misuse leads to fragile systems  

---

## Practice Tasks

1. Create single & multilevel inheritance  
2. Override parent method  
3. Use `super()` correctly  
4. Inspect MRO  
5. Trigger attribute shadowing  
6. Build diamond inheritance  
7. Compare inheritance vs composition
