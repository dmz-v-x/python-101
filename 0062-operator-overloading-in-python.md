## Operator Overloading in Python

**Operator Overloading** means:

```text
Giving special meaning to operators for user-defined objects
```

Python allows objects to define how operators behave using **dunder (magic) methods**.

Example:

```python
+  -  *  /  ==  <  []
```

Can work on **your own classes** 

---

## Mental Model

Operators are just:

```text
Method calls behind the scenes
```

Example:

```python
a + b
```

Actually becomes:

```python
a.__add__(b)
```

HUGE Insight.

---

## Why Operator Overloading Matters

---

✔ Makes objects intuitive  
✔ Improves readability  
✔ Enables mathematical models  
✔ Cleaner domain logic  
✔ Used heavily in libraries (NumPy, Pandas, etc.)

---

## Basic Example — Without Overloading

---

```python
class Number:
    def __init__(self, value):
        self.value = value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)   # ERROR
```

❌ Because Python doesn't know how to add objects.

---

## Adding Operator Overloading

---

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)
```

---

```python
n1 = Number(10)
n2 = Number(20)

result = n1 + n2
print(result.value)
```

**Output:**

```text
30
```

✔ Magic unlocked

---

## What Happened Internally?

---

```text
n1 + n2 → n1.__add__(n2)
```

---

## Common Operator Methods 

---

| Operator | Dunder Method |
|-------------|------------------|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `//` | `__floordiv__` |
| `%` | `__mod__` |
| `**` | `__pow__` |
| `==` | `__eq__` |
| `<` | `__lt__` |
| `>` | `__gt__` |
| `len(obj)` | `__len__` |
| `obj[index]` | `__getitem__` |

---

## Overloading Multiple Operators

---

```python
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
```

---

```python
v1 = Vector(2, 3)
v2 = Vector(1, 1)

result = v1 + v2
print(result.x, result.y)
```

**Output:**

```text
3 4
```

---

## Comparison Operator Overloading 

---

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks
```

---

```python
s1 = Student(85)
s2 = Student(75)

print(s1 > s2)
```

**Output:**

```text
True
```

---

## String Representation Overloading 🔥🔥🔥

Without this:

```text
Objects print ugly memory addresses 😱
```

---

## Using `__str__`

---

```python
class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"
```

---

```python
p = Person("Alice")
print(p)
```

**Output:**

```text
Person: Alice
```

Extremely important.

---

## Deadly Gotchas 🔥🔥🔥

---

## Gotcha #1 — Returning Wrong Type 😱

---

```python
def __add__(self, other):
    return self.value + other.value   # BAD
```

✔ Should return object, not raw value (usually).

---

## Gotcha #2 — Missing Type Checks

---

```python
def __add__(self, other):
    return Number(self.value + other.value)
```

Crashes if `other` isn't Number.

---

## Safer Version

---

```python
def __add__(self, other):

    if isinstance(other, Number):
        return Number(self.value + other.value)

    return NotImplemented
```

🔥 Best practice.

---

## Gotcha #3 — NotImplemented vs Error 

Returning:

```python
NotImplemented
```

✔ Allows Python fallback logic  
✔ Cleaner operator chaining  

---

## Gotcha #4 — Immutable vs Mutable Behavior 

Operator overloading usually:

Returns NEW objects  
Should NOT mutate existing ones (unless intentional)

---

## Gotcha #5 — Equality Requires Care

---

```python
def __eq__(self, other):
    return self.value == other.value
```

Works  
But hash consistency issues may arise

---

## Deep Design Insight

Operator overloading should:

✔ Improve clarity  
✔ Feel natural  
✔ Avoid surprising behavior  

Rule:

```text
"If it confuses → Don't overload"
```

---

## Real-World Usage

---

✔ Mathematical libraries  
✔ Domain modeling  
✔ DSL creation  
✔ Custom containers  
✔ Data science frameworks  

---

## Best Practices 

---

✔ Always return correct type  
✔ Use type checks  
✔ Return NotImplemented when needed  
✔ Keep behavior intuitive  
✔ Avoid overengineering  

---

## Summary

✔ Operators = Method calls  
✔ Implement via dunder methods  
✔ Enables custom object behavior  
✔ Used for arithmetic & comparisons  
✔ Critical for clean APIs  
✔ Must be used carefully  

---

## Practice Tasks

1. Overload `+` for custom class  
2. Overload `-` operator  
3. Overload comparison operator (`>`)  
4. Implement `__str__`  
5. Implement `__len__`  
6. Implement safe type checking  
7. Return NotImplemented properly  
8. Build Vector math example 
