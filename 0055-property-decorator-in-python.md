## Property Decorator in Python

In Python, the **property decorator** allows you to:

✔ Control attribute access  
✔ Add validation logic  
✔ Compute values dynamically  
✔ Keep clean attribute syntax  

👉 Most important idea:

```text
Methods behaving like attributes
```

---

## Mental Model

A property is:

```text
Function Disguised as Variable
```

You define a method…

But access it like:

```python
obj.attribute
```

---

## Why Use `@property`?

---

Without properties:

```python
obj.get_salary()
obj.set_salary(5000)
```

With properties:

```python
obj.salary
obj.salary = 5000
```

✔ Cleaner  
✔ Pythonic  
✔ Encapsulated  

---

## Basic Getter Using `@property`

---

## Example

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary   # Internal attribute

    @property
    def salary(self):
        return self._salary

emp = Employee(5000)

print(emp.salary)
```

**Output:**
```text
5000
```

---

## What Happened Internally?

```python
emp.salary
```

Actually becomes:

```python
Employee.salary(emp)
```

✔ Method call  
✔ Clean syntax  

---

## Adding Setter Using `@<property>.setter`

---

## Example

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        print("Getter called")
        return self._salary

    @salary.setter
    def salary(self, value):
        print("Setter called")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

emp = Employee(5000)

print(emp.salary)
emp.salary = 6000
```

**Output:**
```text
Getter called
5000
Setter called
```

---

## Key Insight

✔ Read → Getter  
✔ Write → Setter  

---

## CRITICAL Rule

Always store real data in:

```python
_internal_variable
```

NOT property name.

---

## DEADLY Gotcha #1 — Infinite Recursion

---

WRONG:

```python
class Test:
    @property
    def salary(self):
        return self.salary   
```

✔ Infinite recursion crash

---

CORRECT:

```python
return self._salary
```

---

## DEADLY Gotcha #2 — Setter Recursion 

---

WRONG:

```python
@salary.setter
def salary(self, value):
    self.salary = value   
```

---

CORRECT:

```python
self._salary = value
```

---

## Read-Only Property

---

If setter NOT defined:

```python
@property
def salary(self):
    return self._salary
```

Attempting:

```python
emp.salary = 100
```

**Error:**
```text
AttributeError: can't set attribute
```

✔ Safe computed attribute 

---

## Computed Property

---

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.1416 * (self.radius ** 2)

c = Circle(5)

print(c.area)
```

**Output:**
```text
78.54
```

✔ No stored `_area` needed 

---

## Why This is Powerful

✔ Always up-to-date  
✔ No redundant storage  
✔ Cleaner logic  

---

## Validation via Setter

---

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

✔ Prevents invalid state

---

## Deep Internal Understanding

---

Property decorator ≈

```python
attribute = property(getter, setter)
```

Equivalent:

```python
class Test:
    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, set_x)
```

✔ Same behavior

---

## DEADLY Gotcha #3 — Direct Attribute Bypass

---

User can still do:

```python
emp._salary = -999   
```

✔ Python trusts developers  
✔ No strict private enforcement  

---

## DEADLY Gotcha #4 — Heavy Logic in Getter

---

Bad design:

```python
@property
def data(self):
    return expensive_operation()   
```

✔ Performance issue

Better:

✔ Cache result  
✔ Memoization  

---

## Property vs Normal Methods

| Feature | Property | Method |
|-------------|-------------|-------------|
| Syntax | `obj.value` | `obj.value()` |
| Best For | Attributes / Computed Data | Actions / Operations |
| Expected Cost | Fast | Can be heavy |
| Side Effects | Minimal | Acceptable |

---

## Summary

✔ `@property` → Getter  
✔ `@property.setter` → Setter  
✔ Enables validation & logic  
✔ Clean attribute syntax  
✔ Avoid recursion traps  
✔ Use internal variables  

---

## Practice Tasks

1. Create read-only property  
2. Add validation setter  
3. Trigger recursion bug intentionally  
4. Build computed property  
5. Block invalid assignments  
6. Convert property() → decorator  
7. Predict outputs  
