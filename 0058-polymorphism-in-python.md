## Polymorphism in Python

**Polymorphism** means:

```text
"Same interface, different behavior"
```

👉 One name → Many forms

Instead of worrying about **what type an object is**,  
we care about **what behavior it provides**.

---

## Mental Model

Polymorphism allows:

✔ Different objects  
✔ Same method name  
✔ Different implementations  

Example:

```text
Dog → speak()
Cat → speak()
Human → speak()
```

All respond to:

```text
speak()
```

---

## Basic Polymorphism Example

---

```python
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

**Output:**
```text
Woof
Meow
```

---

## What Happened?

✔ Same method name → `speak()`  
✔ Different behavior → depends on object  

Python decides **at runtime**.

---

## Why Polymorphism Matters

---

✔ Flexible code  
✔ No type checking needed  
✔ Extensible systems  
✔ Cleaner architecture  
✔ Plug-and-play behavior  

---

## Python’s Superpower → Duck Typing 🐍🔥

---

Python polymorphism relies heavily on:

```text
Duck Typing
```

Rule:

```text
"If it behaves like a duck → it's a duck"
```

👉 Type does NOT matter  
👉 Behavior matters  

---

## Duck Typing Example

```python
class Dog:
    def speak(self):
        print("Woof")

class Robot:
    def speak(self):
        print("Beep")

def make_it_speak(entity):
    entity.speak()

make_it_speak(Dog())
make_it_speak(Robot())
```

**Output:**
```text
Woof
Beep
```

✔ No inheritance required 

---

## Polymorphism with Functions

---

Many built-ins are polymorphic:

---

## Example → `len()`

```python
print(len("Hello"))     # String
print(len([1, 2, 3]))   # List
print(len((1, 2)))      # Tuple
```

✔ Same function → Different objects  

---

## Polymorphism via Inheritance

---

Classic OOP polymorphism:

---

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

✔ Method overriding 

---

## Runtime Method Resolution

---

Python determines behavior using:

```text
Dynamic Dispatch
```

✔ Happens at runtime  
✔ Based on object type  

---

## Real-World Polymorphism Example

---

```python
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

def process_payment(method, amount):
    method.pay(amount)

process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
```

✔ Same interface → Multiple implementations 

---

## Polymorphism Without Inheritance

---

Python encourages:

```text
Behavior-based polymorphism
```

---

```python
class Bird:
    def move(self):
        print("Flying")

class Fish:
    def move(self):
        print("Swimming")

def make_it_move(creature):
    creature.move()

make_it_move(Bird())
make_it_move(Fish())
```

✔ Pure duck typing 

---

## Deadly Gotchas

---

## Gotcha #1 — Assuming Type Safety

Python does NOT enforce interfaces.

---

```python
def make_it_speak(entity):
    entity.speak()
```

If missing:

```text
AttributeError
```

---

## Gotcha #2 — Wrong Mental Model

Polymorphism is NOT about inheritance.

✔ It's about shared behavior.

---

## Gotcha #3 — Overusing isinstance()

Bad design:

```python
if isinstance(obj, Dog):
    ...
```

✔ Breaks polymorphism

Better:

```python
obj.speak()
```

---

## Gotcha #4 — Method Signature Mismatch

---

```python
class Dog:
    def speak(self): pass

class Robot:
    def speak(self, volume): pass
```

✔ Runtime error risk

Keep interface consistent.

---

## Gotcha #5 — Silent Bugs 

Duck typing can hide errors:

✔ Wrong method → No immediate crash  
✔ Logic failure 😱

---

## Best Practices 

---

✔ Design around behavior  
✔ Keep method names consistent  
✔ Avoid explicit type checking  
✔ Prefer duck typing  
✔ Use ABCs for strict contracts  
✔ Keep interfaces stable  

---

## Advanced Polymorphism → Abstract Base Classes (ABC)

---

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

✔ Enforces contract

---

## Real-World Design Insight

---

Polymorphism enables:

✔ Strategy Pattern  
✔ Plugin Systems  
✔ Dependency Injection  
✔ Flexible APIs  
✔ Clean Architecture  

---

## Summary

✔ Polymorphism = Same interface, different behavior  
✔ Python → Duck typing driven  
✔ No inheritance required  
✔ Runtime behavior resolution  
✔ Extremely flexible design  
✔ Dangerous if misunderstood ⚠️  

---

## Practice Tasks

1. Create multiple classes sharing same method  
2. Use duck typing without inheritance  
3. Break polymorphism using isinstance()  
4. Fix using pure behavior calls  
5. Create payment strategy system  
6. Cause signature mismatch bug  
7. Fix interface consistency
