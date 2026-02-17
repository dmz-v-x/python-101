## Constructor & Object Initialization in Python

When you create an object in Python:

```python
obj = MyClass()
```

Python performs **two major steps** internally:

1. **Object Creation → `__new__()`**  
2. **Object Initialization → `__init__()`**

Most beginners only learn `__init__()`  
Real mastery requires understanding **both**

---

## Mental Model (CRITICAL)

Think of object creation like building a house:

| Step | Meaning |
|------|----------|
| `__new__()` | Builds the empty house |
| `__init__()` | Furnishes the house |

---

## 1. What is a Constructor?

A constructor is a **special method** that runs automatically when an object is created.

In Python:

```python
__init__()
```

But technically:

👉 Constructor mechanism = `__new__()` + `__init__()`

---

## 2. Object Creation Flow (VERY IMPORTANT)

When you write:

```python
p = Person("Alice")
```

Python internally executes:

```text
1. Call Person.__new__()
2. Create empty object
3. Call Person.__init__()
4. Initialize object data
```

---

## 3. `__init__()` — The Initializer

`__init__()` is used to:

✔ Assign attributes  
✔ Set object state  
✔ Perform setup logic

---

### Basic Example

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p = Person("Alice")
print(p.name)
```

**Output:**
```text
Alice
```

Runs automatically

---

## 4. `__init__()` is NOT Object Creation 🚨

Huge misconception.

`__init__()` does NOT create objects  
It only initializes existing objects

Actual creation happens in:

```python
__new__()
```

---

## 5. `__new__()` — The Real Creator (Advanced)

`__new__()`:

✔ Creates the object  
✔ Returns the instance  
✔ Runs BEFORE `__init__()`

Rarely overridden, but extremely important conceptually.

---

### Example: Visualizing `__new__()`

```python
class Demo:
    def __new__(cls):
        print("Creating object...")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object...")
```

```python
d = Demo()
```

**Output:**
```text
Creating object...
Initializing object...
```

Creation → Initialization

---

## Golden Rule

```text
__new__() → Creates object
__init__() → Configures object
```

---

## 6. Constructor with Multiple Parameters

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

```python
p = Person("Alice", 25)
```

---

## 7. Default Values in Constructors

```python
class Person:
    def __init__(self, name="Guest"):
        self.name = name
```

```python
p1 = Person()
p2 = Person("Alice")
```

---

## 8. Constructor Logic & Validation (REAL WORLD)

Constructors often enforce rules.

---

### Example: Input Validation

```python
class Person:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age
```

Protects object integrity

---

## 9. Heavy vs Light Constructors

---

### Heavy Constructor (Bad Practice)

```python
def __init__():
    # Database calls
    # API requests
    # File IO
```

Slows object creation

---

### Preferred Approach

✔ Keep constructor lightweight  
✔ Move heavy logic to methods

---

## 10. Instance Attributes Initialization

Constructor commonly defines **object state**.

```python
class Counter:
    def __init__(self):
        self.count = 0
```

Each object → Independent state

---

## 11. Alternative Constructors (Very Important)

Python allows **multiple ways to create objects**.

Using **class methods**.

---

### Example: Alternative Constructor

```python
class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, data):
        name = data.upper()
        return cls(name)
```

```python
p = Person.from_string("alice")
print(p.name)
```

**Output:**
```text
ALICE
```

Clean object creation patterns

---

## 12. Constructor vs Normal Method

| Feature | Constructor | Method |
|----------|--------------|----------|
| Called Automatically? | ✅ Yes | ❌ No |
| Purpose | Setup object | Behavior |
| Return Value | None | Optional |

---

## 13. Common Constructor Mistakes 🚨

---

### Forgetting self

```python
def __init__(name):
```

**Error:**
```text
TypeError
```

---

### Forgetting attribute assignment

```python
name = name
```

Local variable only → LOST

---

### Returning value from `__init__()`

```python
return something
```

**Error:**
```text
TypeError: __init__() should return None
```

Constructors must return None

---

### Confusing class & instance attributes

```python
self.shared = []
```

vs

```python
Class.shared = []
```

---

## 14. Constructor & Memory Identity

```python
class Demo:
    def __init__(self):
        print(id(self))
```

```python
d = Demo()
print(id(d))
```

✔ Same identity

---

## 15. Constructor Best Practices ✅

✔ Always initialize required attributes  
✔ Validate inputs when necessary  
✔ Keep constructor lightweight  
✔ Avoid complex logic  
✔ Use alternative constructors for flexibility  
✔ Maintain object consistency

---

## Summary

| Concept | Truth |
|----------|---------|
| `__new__()` | Creates object |
| `__init__()` | Initializes object |
| Constructor | Creation + Initialization |
| Called automatically | ✅ Yes |
| Must return None | ✅ Yes |
| Used for validation | ✅ Yes |
| Heavy logic inside? | ❌ Avoid |

---

## Practice Tasks

1. Print execution order of `__new__()` & `__init__()`  
2. Create constructor with validation  
3. Implement default parameters  
4. Build alternative constructor  
5. Try returning value from `__init__()`  
6. Create multiple objects & inspect states  
7. Compare instance vs class attribute initialization  
