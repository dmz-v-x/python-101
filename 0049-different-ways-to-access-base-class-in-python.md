## Different ways to access base class in Python

When working with **inheritance**, a child class often needs to:

✔ Reuse base class logic  
✔ Extend behavior  
✔ Access parent attributes/methods  

Python provides **three primary ways** to access base class members.

---

## Mental Model First

Inheritance means:

Child class automatically receives base class features.

But HOW we access them matters.

---

## 1. Direct Access via Instance (Implicit Lookup)

---

## Example

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()
```

**Output:**
```text
Hello from Parent
```

---

## What Happened Internally?

Python lookup order:

```text
1. Child Instance Namespace
2. Child Class Namespace
3. Parent Class Namespace FOUND
```

✔ Works automatically  
✔ No special syntax needed  

---

## When This Works Best

✔ No overriding required  
✔ Simple reuse  
✔ Default inheritance behavior  

---

## 2. Using `super()` (Recommended)

---

## What is `super()`?

`super()` gives controlled access to base class.

👉 Clean  
👉 Safe  
👉 Maintains inheritance chain  

---

## Example

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()
```

**Output:**
```text
Hello from Parent
Hello from Child
```

---

## Why `super()` is Powerful

✔ Avoids hardcoding class names  
✔ Supports multiple inheritance  
✔ Prevents fragile code  
✔ Maintains Method Resolution Order (MRO)

---

## Bad Practice (Avoid)

```python
Parent.greet(self)
```

Problem:

❌ Breaks MRO  
❌ Dangerous in multiple inheritance  

---

## Best Use Cases

✔ Method extension  
✔ Constructor chaining  
✔ Cooperative inheritance  

---

## 3. Accessing via Base Class Name (Explicit Call)

---

## Example

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        Parent.greet(self)
        print("Hello from Child")

c = Child()
c.greet()
```

**Output:**
```text
Hello from Parent
Hello from Child
```

---

## What This Actually Does

✔ Directly jumps to Parent  
✔ Ignores MRO chain 

---

## Why This is Risky

Works fine in **single inheritance**, BUT:

❌ Breaks multiple inheritance logic  
❌ Skips cooperative calls  
❌ Creates maintenance issues  

---

## When It’s Acceptable

✔ Rare edge cases  
✔ Legacy code  
✔ Very controlled designs  

---

## Comparing All Three Methods

| Method | How it Works | Safe? | Recommended? |
|------------|------------------|------------|----------------|
| Direct Instance Access | Automatic lookup | ✅ Yes | ✅ Yes |
| `super()` | Controlled parent access | ✅🔥 Best | ✅✅✅ |
| Base Class Name | Hardcoded parent call | ⚠️ Risky | ❌ Avoid |

---

## Deep Insight: Why `super()` Wins 🔥

Because Python supports:

✔ Multiple inheritance  
✔ Complex class hierarchies  
✔ Dynamic resolution  

Only `super()` respects:

👉 MRO (Method Resolution Order)

---

## Example Showing Why `super()` Matters

---

## Multiple Inheritance Scenario

```python
class A:
    def greet(self):
        print("From A")

class B(A):
    def greet(self):
        super().greet()
        print("From B")

class C(A):
    def greet(self):
        super().greet()
        print("From C")

class D(B, C):
    def greet(self):
        super().greet()
        print("From D")

d = D()
d.greet()
```

**Output:**
```text
From A
From C
From B
From D
```

✔ Perfect chain  
✔ No duplication  
✔ MRO respected  

---

## Common Errors & Pitfalls

| Mistake | Problem |
|--------------|-------------|
| Forgetting `self` in explicit call | TypeError |
| Using base class name in multiple inheritance | Breaks MRO |
| Not using `super()` in constructors | Incomplete initialization |
| Assuming direct access always safe | Hidden bugs |

---

## Best Practices

✔ Prefer `super()`  
✔ Avoid hardcoded parent calls  
✔ Understand lookup order  
✔ Respect MRO  
✔ Write cooperative classes  

---

## Summary

| Concept | Truth |
|-------------|------------|
| Direct Access | Uses lookup chain |
| `super()` | Clean & safe parent access 🔥 |
| Base Class Name | Hardcoded & fragile |
| Multiple Inheritance | Only `super()` behaves correctly |
| Professional Code | Uses `super()` |

---

## Practice Tasks

1. Extend parent method using `super()`  
2. Chain constructors properly  
3. Print MRO using:

```python
print(ClassName.__mro__)
```

4. Break inheritance intentionally using base class name  
5. Predict lookup behavior  
6. Create diamond inheritance  
7. Debug shadowing vs inheritance  
