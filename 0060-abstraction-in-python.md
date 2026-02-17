## Abstraction in Python

**Abstraction** means:

```text
Showing ONLY essential features
Hiding implementation details
```

👉 Focus on *what an object does*, not *how it does it*.

---

## Mental Model

Think of driving a car 🚗

✔ You use steering, brakes, accelerator  
✔ You DON'T care about engine internals  

That’s abstraction.

```text
Interface → Visible
Implementation → Hidden
```

---

## Why Abstraction Matters

---

✔ Reduces complexity  
✔ Improves readability  
✔ Encourages modular design  
✔ Allows interchangeable implementations  
✔ Makes systems scalable  
✔ Enables clean architecture  

---

## Encapsulation vs Abstraction 

---

| Concept | Focus |
|----------|----------|
| Encapsulation | Hiding data / protecting state |
| Abstraction | Hiding complexity / exposing behavior |

👉 Encapsulation = Safety  
👉 Abstraction = Simplicity  

They work **together**, not separately.

---

## How Python Implements Abstraction 

---

Python uses:

```text
Abstract Base Classes (ABC)
```

Provided by:

```python
from abc import ABC, abstractmethod
```

---

## Abstract Base Class (ABC)

---

An **abstract class**:

✔ Cannot be instantiated directly  
✔ Defines required methods  
✔ Forces subclasses to implement behavior  

---

## Basic Example

---

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

This is illegal:

```python
a = Animal()   # ERROR 
```

✔ Because it has abstract methods.

---

## Concrete Implementation

---

```python
class Dog(Animal):

    def speak(self):
        return "Woof!"
```

```python
d = Dog()
print(d.speak())
```

**Output:**

```text
Woof!
```

✔ Subclass must implement `speak()`.

---

## What Just Happened?

---

Abstract class = Contract 

```text
"If you inherit → You MUST implement"
```

---

## Multiple Abstract Methods

---

```python
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

---

```python
class Rectangle(Shape):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)
```

✔ Enforces full implementation.

---

## Abstraction = Interface Design

---

Abstract class behaves like:

```text
Blueprint / Contract / Interface
```

Defines:

✔ Required behaviors  
✔ NOT actual logic  

---

## Real-World Analogy

---

Payment System 

```python
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Implementations:

✔ CreditCardProcessor  
✔ UPIProcessor  
✔ CryptoProcessor  

All interchangeable 

---

## Deadly Gotchas

---

## Gotcha #1 — Forgetting Implementation 

---

```python
class Cat(Animal):
    pass
```

ERROR:

```text
TypeError: Can't instantiate abstract class
```

✔ Because method missing.

---

## Gotcha #2 — Abstract Class CAN Have Logic 

---

YES 

```python
class Animal(ABC):

    def breathe(self):
        return "Breathing..."

    @abstractmethod
    def speak(self):
        pass
```

✔ Abstract ≠ Empty  
✔ Can contain shared behavior 

---

## Gotcha #3 — Abstract Methods Can Have Code 

---

```python
class Example(ABC):

    @abstractmethod
    def method(self):
        print("Some base logic")
```

✔ Still abstract  
✔ Still must override 

---

## Gotcha #4 — Instantiation Check Happens at Runtime 

Python enforces abstraction **ONLY at runtime**.

✔ No compile-time enforcement like Java.

---

## Gotcha #5 — Static Methods Can Be Abstract 

---

```python
class Example(ABC):

    @staticmethod
    @abstractmethod
    def utility():
        pass
```

✔ Perfectly valid.

---

## Gotcha #6 — Class Methods Can Be Abstract 🔥

---

```python
class Example(ABC):

    @classmethod
    @abstractmethod
    def create(cls):
        pass
```

---

## Gotcha #7 — Thinking Abstraction = Data Hiding 

NOPE 

Abstraction hides:

✔ Behavior complexity  
NOT  
✔ Data visibility  

---

## Deep Insight

Abstraction enables:

✔ Loose coupling  
✔ Dependency inversion  
✔ Plugin systems  
✔ Strategy pattern  
✔ Swappable components  

Core of **clean architecture** 

---

## Abstraction vs Polymorphism

---

| Concept | Role |
|----------|----------|
| Abstraction | Defines interface |
| Polymorphism | Uses interface flexibly |

👉 Abstraction = Rules  
👉 Polymorphism = Flexibility  

---

## Best Practices 

---

✔ Use ABC for contracts  
✔ Define behaviors, not implementation  
✔ Keep abstract classes minimal  
✔ Avoid unnecessary abstraction  
✔ Prefer composition when suitable  
✔ Use abstraction for large systems  

---

## When To Use Abstraction 

---

Multiple implementations needed  
Framework / plugin design  
Large scalable systems  
Clean architecture layers  
Enforcing API consistency  

Avoid for tiny scripts.

---

## Summary

✔ Abstraction = Hide complexity  
✔ Python uses ABC module  
✔ Abstract classes = Contracts  
✔ Cannot instantiate directly  
✔ Subclasses MUST implement methods  
✔ Supports instance/class/static methods  
✔ Runtime enforcement 
✔ Key for scalable design  

---

## Practice Tasks

1. Create abstract class with 2 methods  
2. Try instantiating abstract class (observe error)  
3. Implement concrete subclass  
4. Add shared logic inside ABC  
5. Create abstract static method  
6. Create abstract class method  
7. Build payment system example  
8. Demonstrate polymorphism via abstraction  
