## Static Methods in Python

A **static method** in Python is a method that:

✔ Belongs to a class  
✔ Does NOT access instance (`self`)  
✔ Does NOT access class (`cls`)  
✔ Acts like a normal function  
✔ Lives inside a class namespace  

---

## Mental Model

Static methods are:

```text
Namespaced Utility Functions
```

They are grouped logically inside a class but have:

👉 No automatic binding  
👉 No implicit arguments  

---

## Why Static Methods Exist

---

Without static methods:

```python
def add(a, b):
    return a + b
```

With static methods:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

✔ Better organization  
✔ Logical grouping  
✔ Cleaner APIs  

---

## Basic Syntax

---

```python
class ClassName:
    @staticmethod
    def method_name(parameters):
        # logic
```

✔ Uses `@staticmethod` decorator  
✔ No `self`  
✔ No `cls`

---

## Example 1 — Basic Static Method

---

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(10, 20))
```

**Output:**
```text
30
```

---

## Key Insight

✔ Called using class  
✔ No object required  

---

## Example 2 — Can Be Called via Instance

---

```python
class Demo:
    @staticmethod
    def greet():
        print("Hello!")

d = Demo()
d.greet()
```

**Output:**
```text
Hello!
```

---

## Why Does This Work?

Because static methods:

✔ Are NOT bound  
✔ Behave like functions  

Python simply finds method in class namespace.

---

## Static Method vs Instance Method

---

## Comparison

```python
class Example:
    def instance_method(self):
        print("Instance")

    @staticmethod
    def static_method():
        print("Static")
```

---

## Internal Transformation

Instance method call:

```python
obj.instance_method()
→ Example.instance_method(obj)
```

Static method call:

```python
obj.static_method()
→ Example.static_method()
```

✔ No object passed

---

## Static Method vs Class Method

---

| Feature | Static Method | Class Method |
|-------------|------------------|----------------|
| First Argument | None | `cls` |
| Access Class Data | ❌ | ✅ |
| Access Instance Data | ❌ | ❌ |
| Binding | None | Class-bound |
| Use Case | Utility Logic | Class Logic |

---

## Example Showing Difference

---

```python
class Test:
    x = 10

    @staticmethod
    def static_show():
        print(Test.x)

    @classmethod
    def class_show(cls):
        print(cls.x)
```

✔ Static method → Hardcoded class  
✔ Class method → Dynamic class  

---

## Deep Internal Behavior

---

Static methods use:

```python
staticmethod()
```

Which wraps function inside descriptor.

Equivalent to:

```python
method = staticmethod(function)
```

---

## Demonstration

```python
class Demo:
    def greet():
        print("Hello")

print(Demo.greet)
```

**Output:**
```text
<function Demo.greet>
```

✔ No bound method object

---

## Deadly Gotchas

---

## Gotcha #1 — Expecting Access to Instance

---

WRONG:

```python
class Test:
    def __init__(self):
        self.x = 10

    @staticmethod
    def show():
        print(self.x)  
```

✔ No `self`

---

## Gotcha #2 — Expecting Access to Class

---

WRONG:

```python
print(cls.x)  
```

✔ No `cls`

---

## Gotcha #3 — Hardcoding Class Names

---

```python
print(Test.x)
```

Works BUT:

Breaks inheritance flexibility

Better design → Use classmethod when class access needed.

---

## Gotcha #4 — Misusing Static Methods

---

Bad usage:

✔ Business logic dependent on object state  
✔ Logic needing class attributes  
✔ Overcomplicating design  

---

## When to Use Static Methods

---

✔ Utility/helper logic  
✔ Independent calculations  
✔ Logical grouping  
✔ Stateless operations  
✔ Validation helpers  
✔ Factory helpers (sometimes)

---

## When NOT to Use Static Methods

---

❌ Needs instance data → Use instance method  
❌ Needs class data → Use classmethod  
❌ Complex workflows → Use normal methods  

---

## Real-World Example

---

```python
class Validator:
    @staticmethod
    def is_valid_age(age):
        return 0 < age < 120

print(Validator.is_valid_age(25))
```

**Output:**
```text
True
```

✔ Clean utility logic

---

## Summary

✔ Static methods = Functions inside class  
✔ No automatic binding  
✔ No `self` / `cls`  
✔ Used for utilities  
✔ Callable via class or instance  
✔ Backed by descriptor protocol  
✔ Avoid misuse  

---

## Practice Tasks

1. Create utility static method  
2. Break code using `self` inside static method  
3. Convert staticmethod → classmethod  
4. Compare binding behaviors  
5. Use staticmethod manually  
6. Build validation helper class  
7. Predict outputs
