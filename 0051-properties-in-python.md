## Properties in Python

In Python, **properties** allow you to control access to class attributes while keeping **clean attribute syntax**.

👉 Without properties:

```python
obj.get_salary()
obj.set_salary(5000)
```

👉 With properties:

```python
obj.salary
obj.salary = 5000
```

✔ Cleaner  
✔ More Pythonic  
✔ Supports validation & logic  

---

## Mental Model

A property is:

```text
Method Disguised as Attribute
```

You write a method…

But access it like a variable.

Python magic ✨

---

## Why Properties Exist

---

## 1. Encapsulation

Hide internal implementation.

Users interact with:

```python
obj.salary
```

Instead of:

```python
obj._salary
```

---

## 2. Data Validation

Control assignments safely.

✔ Prevent invalid states  
✔ Add constraints  
✔ Add transformation logic  

---

## 3. Computed Attributes

Dynamically calculate values.

✔ No stored data needed  
✔ Always up-to-date  

---

## Basic Property Syntax

---

```python
class ClassName:
    def __init__(self, value):
        self._value = value   # Internal variable

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value
```

---

## Key Insight

✔ Getter → Read access  
✔ Setter → Write access  
✔ Deleter → Delete access  

All behind:

```python
obj.value
```

---

## Example 1 — Classic Getter & Setter

---

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        print("Getting salary...")
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        print("Setting salary...")
        self._salary = value

emp = Employee("Alice", 5000)

print(emp.salary)
emp.salary = 6000
```

**Output:**
```text
Getting salary...
5000
Setting salary...
```

---

## What Just Happened?

```python
emp.salary
```

Becomes:

```python
Employee.salary(emp)
```

✔ Method call disguised as attribute

---

## Example 2 — Read-Only Property 🔥

---

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.1416 * (self._radius ** 2)

c = Circle(5)

print(c.area)
```

**Output:**
```text
78.54
```

---

## Why Read-Only?

No setter defined.

```python
c.area = 100   # ❌ ERROR
```

**Error:**
```text
AttributeError: can't set attribute
```

✔ Perfect for computed values

---

## Example 3 — Property with Deleter

---

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)

del p.price
```

**Output:**
```text
Deleting price...
```

---

## Deep Internal Understanding (ADVANCED 🔥)

---

## Properties are Descriptors

Under the hood:

```python
property()
```

Creates a descriptor object.

Equivalent to:

```python
value = property(getter, setter, deleter)
```

---

## Demonstration

```python
class Demo:
    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, set_x)
```

✔ Same as `@property`

---

## CRITICAL Gotchas 🔥🔥🔥

---

## Gotcha #1 — Infinite Recursion 😱

---

❌ WRONG:

```python
class Test:
    @property
    def x(self):
        return self.x   # ❌ Calls itself forever
```

✔ Causes recursion crash

✅ CORRECT:

```python
return self._x
```

---

## Gotcha #2 — Direct Attribute Bypass

---

Users can still do:

```python
obj._salary = -999   # ❌ Bypass validation
```

✔ Python trusts developers

👉 Properties ≠ strict private enforcement

---

## Gotcha #3 — Naming Convention Matters

---

Standard practice:

```python
_attribute   # Internal
attribute    # Property
```

Avoid:

```python
salary → salary  # Causes confusion
```

---

## Gotcha #4 — Setter Validation Errors

---

```python
emp.salary = -100
```

**Error:**
```text
ValueError: Salary cannot be negative!
```

✔ Validation logic executed

---

## Gotcha #5 — Expensive Computed Properties

---

Bad practice:

```python
@property
def data(self):
    return heavy_calculation()  # Runs EVERY access 😱
```

✔ May cause performance issues

✅ Solution:

✔ Cache result  
✔ Use memoization  
✔ Use functools.lru_cache  

---

## When to Use Properties ✅🔥

---

✔ Validation required  
✔ Derived/computed values  
✔ Backward compatibility  
✔ Lazy evaluation  
✔ Controlled mutation  

---

## When NOT to Use Properties

---

❌ Heavy business logic  
❌ Complex workflows  
❌ Side-effect-heavy operations  

👉 Use methods instead.

---

## Property vs Normal Methods

| Feature | Property | Method |
|-------------|-------------|-------------|
| Syntax | `obj.value` | `obj.value()` |
| Best For | Attributes / computed values | Actions / operations |
| Side Effects | Should be minimal | Acceptable |
| Performance Expectation | Fast | Can be heavy |

---

## Summary

✔ Properties = Methods with attribute syntax  
✔ Enable encapsulation & validation  
✔ Backed by descriptor protocol  
✔ Getter / Setter / Deleter control behavior  
✔ Naming conventions are critical  
✔ Avoid recursion traps 🔥  

---

## Practice Tasks

1. Create read-only property  
2. Add validation setter  
3. Trigger recursion bug intentionally  
4. Implement computed property  
5. Cache expensive property  
6. Use property() manually  
7. Compare method vs property  
