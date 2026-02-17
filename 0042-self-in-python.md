## `self` in python

In Python, `self` represents:

👉 **The current instance (object)** of a class.

It allows an object to:

✔ Access its own data (attributes)  
✔ Call its own methods  
✔ Maintain independent state

---

## Most Important Truth

**`self` is NOT a keyword**

Unlike `if`, `for`, `while`, etc.

It is just a **naming convention**.

You could technically write:

```python
class Person:
    def greet(this):
        print("Hello")
```

But:

✔ Always use `self`  
✔ This is Python’s universal convention

---

## Mental Model (CRITICAL)

Think of:

`self` = "this specific object"

Not the class  
Not a variable  
Not global  

---

## 1. Why Do We Need `self`?

Because multiple objects can exist.

Example:

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p1 = Person("Alice")
p2 = Person("Bob")
```

Each object must store **its own data**.

Without `self` → impossible.

---

## 2. What Actually Happens Internally?

This is where mastery begins 🔥

---

### Normal Method Call

```python
p1.greet()
```

Python transforms it into:

```python
Person.greet(p1)
```

Python **automatically passes the object**

---

## Golden Rule

```text
object.method() → Class.method(object)
```

---

## 3. Example: Understanding self Mechanically

```python
class Person:
    def greet(self):
        print("Hello")
```

```python
p1 = Person()

p1.greet()
Person.greet(p1)
```

Both are identical ✅

---

## 4. Accessing Object Attributes via self

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")
```

`self.name` = attribute of THIS object

---

## 5. self Enables Independent Object State

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
```

```python
c1 = Counter()
c2 = Counter()

c1.increment()

print(c1.count)
print(c2.count)
```

**Output:**
```text
1
0
```

✔ Each object has separate memory

---

## 6. Calling Methods Using self

```python
class Person:
    def greet(self):
        print("Hello")

    def welcome(self):
        self.greet()
        print("Welcome!")
```

self allows method chaining.

---

## 7. self vs Local Variables (VERY IMPORTANT)

---

### Wrong

```python
class Person:
    def __init__(self, name):
        name = name
```

Local variable only → LOST after constructor ends

---

### Correct

```python
self.name = name
```

✔ Stored inside object memory

---

## Rule

| Variable Type | Lifetime |
|--------------|----------|
| Local Variable | Temporary |
| self.attribute | Lives with object |

---

## 8. self vs Class Name Access

Both valid but behave differently.

---

### Using self (Preferred)

```python
self.method()
```

✔ Works with inheritance  
✔ Polymorphism safe

---

### Using Class Name (Less flexible)

```python
Class.method(self)
```

Hardcoded reference

---

## 9. Common Beginner Mistakes

---

### Forgetting self

```python
class Person:
    def greet():
        print("Hello")
```

**Error:**
```text
TypeError: greet() takes 0 positional arguments but 1 was given
```

Python always passes object.

---

### Forgetting self.attribute

```python
print(name)
```

Instead of:

```python
print(self.name)
```

---

### Misunderstanding self as value holder

`self` is NOT data  
It is reference to object

---

## 10. Visualizing self (Deep Intuition)

```text
p1 → Object in memory
self → Alias pointing to p1
```

Inside method:

```text
self = p1
```

---

## 11. Passing self Explicitly (Yes, Possible)

```python
Person.greet(p1)
```

Rarely used manually, but useful for understanding.

---

## 12. self & Memory Identity

```python
class Demo:
    def show(self):
        print(id(self))
```

```python
d = Demo()
d.show()
print(id(d))
```

✔ Both identities match

---

## Advanced Insight (Very Important)

👉 `self` is just a reference variable

Like:

```python
a = object_reference
```

---

## Why Python Needs Explicit self?

Unlike some languages:

✔ Python makes object access **explicit**  
✔ Improves readability  
✔ Removes ambiguity

---

## Summary

| Concept | Truth |
|----------|---------|
| self | Current object reference |
| Keyword? | ❌ No |
| Required? | ✅ Yes |
| Purpose | Access instance data |
| Passed Automatically? | ✅ Yes |
| Stores Data? | ❌ No |
| Naming Convention? | ✅ Yes |

---

## Practice Tasks

1. Call methods using both syntaxes  
2. Print `id(self)` vs `id(object)`  
3. Break code by removing self  
4. Create multiple objects & compare states  
5. Chain methods using self  
6. Experiment with wrong attribute assignment  
7. Rename self (just to observe behavior)  
