## Composition in Python

**Composition** is an OOP design principle where:

👉 A class is built using **other classes**.

Instead of:

```text
IS-A relationship (Inheritance)
```

Composition uses:

```text
HAS-A relationship
```

Example:

```text
Car HAS-A Engine
House HAS-A Room
Computer HAS-A CPU
```

---

## Mental Model

Composition means:

```text
Objects working together to build behavior
```

✔ One object contains another  
✔ Reuse via collaboration  
✔ Flexible & modular design  

---

## Basic Idea of Composition

---

A class stores **another object** as an attribute.

---

## Example

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Composition

    def start_car(self):
        self.engine.start()

c = Car()
c.start_car()
```

**Output:**
```text
Engine started
```

---

## What Happened?

✔ Car does NOT inherit Engine  
✔ Car CONTAINS Engine  
✔ Behavior delegated  

---

#3 Why Use Composition?

---

✔ Avoid tight coupling  
✔ Increase flexibility  
✔ Reuse logic cleanly  
✔ Change components easily  
✔ Better real-world modeling  

---

## Composition vs Inheritance

---

## Core Difference

| Concept | Relationship |
|----------|----------------|
| Inheritance | IS-A |
| Composition | HAS-A |

---

## Inheritance Example

```python
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):   
    pass
```

Car IS-A Engine

---

## Composition Example

```python
class Car:
    def __init__(self):
        self.engine = Engine()
```

👉 Car HAS-A Engine 

✔ Logical  
✔ Cleaner design  

---

## Deep Intuition

---

Inheritance:

```text
Couples classes tightly
```

Composition:

```text
Connects objects loosely
```

✔ Easier to modify  
✔ Easier to extend  
✔ Easier to maintain  

---

## Real-World Composition Example

---

```python
class Battery:
    def charge(self):
        print("Battery charging")

class Phone:
    def __init__(self):
        self.battery = Battery()

    def charge_phone(self):
        self.battery.charge()

p = Phone()
p.charge_phone()
```

✔ Phone HAS-A Battery

---

## Composition with Parameters

---

```python
class Engine:
    def __init__(self, power):
        self.power = power

    def show_power(self):
        print(f"Power: {self.power}")

class Car:
    def __init__(self, power):
        self.engine = Engine(power)

c = Car(200)
c.engine.show_power()
```

**Output:**
```text
Power: 200
```

✔ Flexible component injection  

---

## Dynamic Composition

---

```python
class PetrolEngine:
    def start(self):
        print("Petrol Engine")

class ElectricEngine:
    def start(self):
        print("Electric Engine")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

c1 = Car(PetrolEngine())
c2 = Car(ElectricEngine())

c1.start()
c2.start()
```

**Output:**
```text
Petrol Engine
Electric Engine
```

✔ EXTREMELY powerful design

👉 Swap behaviors easily

---

## Composition Enables Polymorphism

---

✔ No inheritance needed  
✔ Duck typing friendly 

---

## Deadly Gotchas

---

## Gotcha #1 — Confusing Composition with Inheritance

---

Wrong thinking:

```text
"Why not just inherit?"
```

Inheritance creates rigid hierarchies.

Composition → Flexible systems.

---

## Gotcha #2 — Overexposing Internal Objects

---

```python
car.engine.start()
```

✔ Works BUT leaks internals

Better design:

```python
car.start()
```

✔ Encapsulation maintained

---

## Gotcha #3 — Deep Object Chains

---

Bad design:

```python
obj.a.b.c.d.method()
```

✔ Hard to maintain

✔ Use delegation wrappers

---

## Gotcha #4 — Circular Dependencies

Avoid:

```text
A has B  
B has A
```

✔ Creates chaos

---

## Best Practices

---

✔ Prefer composition over inheritance  
✔ Keep components loosely coupled  
✔ Hide internal objects  
✔ Delegate behavior cleanly  
✔ Avoid deep nesting  
✔ Use dependency injection  

---

## When to Prefer Composition

---

✔ Behavior varies  
✔ Components interchangeable  
✔ Avoid tight coupling  
✔ Real-world modeling  
✔ Plugin architectures  
✔ Strategy pattern 🔥  

---

## When Inheritance is Better

---

✔ True IS-A relationship  
✔ Shared core identity  
✔ Stable hierarchies  

Example:

```text
Dog IS-A Animal
```

---

## Summary

✔ Composition = HAS-A relationship  
✔ More flexible than inheritance  
✔ Enables dynamic behavior  
✔ Promotes loose coupling  
✔ Cleaner architecture  
✔ Used heavily in real systems 

---

## Practice Tasks

1. Convert inheritance → composition  
2. Build interchangeable engine system  
3. Hide internal components  
4. Create plugin architecture  
5. Trigger deep nesting problem  
6. Fix using delegation  
7. Compare flexibility
