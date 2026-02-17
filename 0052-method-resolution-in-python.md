## Method Resolution Order

**Method Resolution Order (MRO)** defines:

👉 The order in which Python searches for methods and attributes.

Whenever you call:

```python
obj.method()
```

Python follows a **strict lookup sequence**.

---

## Mental Model

Think of MRO as:

```text
Search Path for Methods
```

Python asks:

```text
Where should I look FIRST?
If not found → Where NEXT?
```

---

## Why MRO Exists

---

Simple inheritance is easy.

Multiple inheritance = Potential chaos

Example problem:

👉 Two parent classes define SAME method.

Which one should Python call?

✔ MRO solves this deterministically.

---

## Single Inheritance (Easy Case)

---

```python
class Parent:
    def greet(self):
        print("From Parent")

class Child(Parent):
    pass

c = Child()
c.greet()
```

**Output:**
```text
From Parent
```

---

## Lookup Order

```text
1. Child Instance
2. Child Class
3. Parent Class
```

---

## Multiple Inheritance

---

```python
class A:
    def greet(self):
        print("From A")

class B:
    def greet(self):
        print("From B")

class C(A, B):
    pass

c = C()
c.greet()
```

**Output:**
```text
From A
```

---

## Why From A?

Because inheritance order:

```python
class C(A, B)
```

Means:

👉 Search A first → Then B

---

## How to See MRO

---

Python exposes MRO using:

```python
ClassName.__mro__
```

OR

```python
ClassName.mro()
```

---

## Example

```python
print(C.__mro__)
```

**Output:**
```text
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

✔ Exact search order

---

## The Diamond Problem 😈🔥

---

Classic multiple inheritance scenario.

---

## Structure

```text
        A
       / \
      B   C
       \ /
        D
```

---

## Example

```python
class A:
    def greet(self):
        print("From A")

class B(A):
    def greet(self):
        print("From B")

class C(A):
    def greet(self):
        print("From C")

class D(B, C):
    pass

d = D()
d.greet()
```

**Output:**
```text
From B
```

---

## But WHY?

Let's inspect MRO.

---

```python
print(D.__mro__)
```

**Output:**
```text
(D, B, C, A, object)
```

✔ Python follows this EXACT order.

---

## Python Uses C3 Linearization (VERY IMPORTANT)

---

Python computes MRO using:

```text
C3 Linearization Algorithm
```

Ensures:

✔ No ambiguity  
✔ Consistent ordering  
✔ Parent precedence respected  
✔ Monotonicity maintained  

---

## Simplified Rules

Python guarantees:

1. Child before parents
2. Left-to-right inheritance priority
3. No duplicate class visits
4. Logical consistency  

---

## `super()` and MRO

---

CRITICAL INSIGHT

👉 `super()` follows MRO.

NOT direct parent.

---

## Example

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

---

## Mind-Blowing Truth

Even though:

```python
class D(B, C)
```

Execution becomes:

```text
A → C → B → D
```

✔ Because MRO chain

---

## Deadly Gotchas

---

## Gotcha #1 — Hardcoding Parent Calls

---

BAD:

```python
A.greet(self)
```

✔ Breaks MRO

✔ Skips chain

ALWAYS USE:

```python
super()
```

---

## Gotcha #2 — Unexpected Execution Order

---

Multiple inheritance ≠ Tree

It becomes:

```text
Linearized Chain
```

✔ Must inspect MRO

---

## Gotcha #3 — Duplicate Method Calls

Improper design:

✔ May call same logic twice

✔ Happens if `super()` not used cooperatively

---

## Gotcha #4 — Conflicting Hierarchies 

Illegal inheritance:

```python
class X(A, B)
class Y(B, A)  #Conflict
```

✔ Python throws MRO error

---

**Error Example:**
```text
TypeError: Cannot create a consistent method resolution order
```

---

## Best Practices

---

✔ Use `super()` ALWAYS  
✔ Write cooperative classes  
✔ Avoid direct parent calls  
✔ Inspect MRO when debugging  
✔ Design clean hierarchies  
✔ Avoid overly complex inheritance  

---

## Summary

✔ MRO = Method lookup order  
✔ Critical for multiple inheritance  
✔ Python uses C3 Linearization  
✔ `super()` respects MRO  
✔ Hardcoded calls break chain ❌  
✔ Diamond problem solved automatically 🔥  

---

## Practice Tasks

1. Print MRO of complex hierarchy  
2. Create diamond inheritance  
3. Predict method execution order  
4. Break MRO intentionally  
5. Fix using `super()`  
6. Add class attributes + test lookup  
7. Build 4-level inheritance chain  
