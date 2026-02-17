## Encapsulation in Python

**Encapsulation** means:

```text
Bundling data + methods that operate on that data into a single unit
```

AND

```text
Restricting direct access to internal details
```

👉 Protect object integrity  
👉 Prevent accidental misuse  
👉 Enable controlled interaction  

---

## Mental Model

Think of a **capsule** 

✔ Internal state hidden  
✔ Interaction via safe interface  

Instead of:

```text
Direct access → Dangerous 
```

We use:

```text
Getter / Setter → Controlled
```

---

## Why Encapsulation Matters

---

✔ Protects data integrity  
✔ Prevents invalid states  
✔ Adds validation rules  
✔ Improves maintainability  
✔ Enables abstraction  
✔ Makes debugging easier  

---

## The Python Reality Check 

---

Unlike Java/C++:

```text
Python does NOT have true private variables
```

Python uses:

```text
Naming conventions + name mangling
```

👉 It's about **intent**, not strict enforcement.

---

## Public vs Protected vs Private (Convention-Based)

---

| Type | Syntax | Meaning |
|------|---------|----------|
| Public | `variable` | Accessible everywhere |
| Protected | `_variable` | "Internal use" (convention) |
| Private | `__variable` | Name mangling applied |

---

## Public Attributes (No Encapsulation)

---

```python
class Person:
    def __init__(self, name):
        self.name = name   # Public

p = Person("Alice")
print(p.name)
p.name = "Bob"
```

✔ Fully accessible  
✔ Fully modifiable  
✔ No protection

---

## Protected Attributes (Soft Restriction)

---

```python
class Person:
    def __init__(self, name):
        self._name = name   # Protected (convention)

p = Person("Alice")
print(p._name)   # Allowed, but discouraged 
```

👉 Only signals developer intent.

---

## Private Attributes (Name Mangling)

---

```python
class Person:
    def __init__(self, name):
        self.__name = name   # Private

p = Person("Alice")

# print(p.__name) # ERROR
print(p._Person__name) 
```

---

## What Happened?

Python transforms:

```text
__name → _ClassName__name
```

✔ Prevents accidental access  
✔ NOT true privacy  

---

## Proper Encapsulation via Getter & Setter

---

```python
class Person:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value
```

Usage:

```python
p = Person("Alice")

print(p.get_name())
p.set_name("Bob")
```

---

## Pythonic Encapsulation → Property Decorator

Cleaner syntax:

---

```python
class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Invalid name")
        self.__name = value
```

Usage:

```python
p = Person("Alice")

print(p.name)    # Getter
p.name = "Bob"   # Setter
```

✔ Looks like attribute access  
✔ Behaves like method call

---

## Core Benefit → Validation Shield 

---

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit")
        self.__balance += amount
```

✔ Prevents illegal state  
✔ Protects invariants

---

## Deadly Gotchas

---

## Gotcha #1 — Python Has No Real Private

Even private variables:

```python
obj._Class__var
```

Still accessible.

👉 Privacy is **by convention**.

---

## Gotcha #2 — Overusing Double Underscore

`__var` triggers name mangling.

✔ Good for avoiding subclass conflicts  
✔ Bad for readability if abused

Use sparingly.

---

## Gotcha #3 — Thinking _var is Protected Enforcement

Single underscore:

```text
Only convention — no restriction
```

---

## Gotcha #4 — Bypassing Setters

Bad:

```python
obj._Person__name = ""
```

✔ Breaks validation logic

---

## Gotcha #5 — Mutable Internal State

---

```python
class Data:
    def __init__(self, items):
        self.__items = items

    def get_items(self):
        return self.__items
```

Problem:

```python
lst = data.get_items()
lst.append(999) 
```

✔ Encapsulation broken

---

## Fix → Defensive Copy

```python
def get_items(self):
    return self.__items.copy()
```

---

## Gotcha #6 — Property Infinite Recursion 

---

Wrong:

```python
@property
def name(self):
    return self.name   # Infinite loop 
```

Correct:

```python
return self.__name
```

---

## Best Practices

---

✔ Protect critical state  
✔ Validate during modification  
✔ Prefer @property over getters/setters  
✔ Avoid unnecessary name mangling  
✔ Use defensive copying for mutables  
✔ Encapsulation = Design discipline  

---

## Advanced Insight

Encapsulation helps enforce:

✔ Invariants  
✔ Business rules  
✔ State consistency  
✔ Controlled mutation  
✔ Clean APIs  

---

## Summary

✔ Encapsulation = Data hiding + controlled access  
✔ Python → Convention-based privacy  
✔ `_var` → Intent signal  
✔ `__var` → Name mangling  
✔ `@property` → Pythonic encapsulation 🔥  
✔ Prevents invalid object states  
✔ Requires discipline ⚠️  

---

## Practice Tasks

1. Create class with private attribute  
2. Add validation using setter  
3. Break encapsulation intentionally  
4. Fix using property decorator  
5. Demonstrate name mangling  
6. Show mutable encapsulation bug  
7. Fix using defensive copy
