## Instance & Class Variable

In Python, variables inside a class can belong to:

1. **The Object (Instance Variables)**  
2. **The Class (Class Variables)**

Understanding this difference is **CRITICAL for OOP mastery**.

---

## Mental Model (VERY IMPORTANT)

Think of:

- **Class Variable → Shared Memory**
- **Instance Variable → Personal Memory**

Example:

```text
Class = Blueprint
Object = Individual Entity
```

---

## 1. Instance Variables

Instance variables belong to:

👉 **Each individual object**

Defined using:

```python
self.variable
```

---

### Example: Instance Variables

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p1 = Person("Alice")
p2 = Person("Bob")

print(p1.name)
print(p2.name)
```

**Output:**
```text
Alice
Bob
```

✔ Each object stores its own data

---

## Memory Behavior

Each object has its own storage:

```python
print(p1.__dict__)
print(p2.__dict__)
```

Example Output:

```text
{'name': 'Alice'}
{'name': 'Bob'}
```

---

## 2. Class Variables

Class variables belong to:

**The class itself**

Defined directly inside class:

```python
class Person:
    species = "Human"
```

---

### Example: Class Variables

```python
class Person:
    species = "Human"
```

```python
p1 = Person()
p2 = Person()

print(p1.species)
print(p2.species)
```

✔ Shared across all objects

---

## Memory Model

```text
Class Variable → Single Memory Location
Instance Variable → Separate per object
```

---

## 3. Lookup Rule (EXTREMELY IMPORTANT)

When accessing:

```python
object.variable
```

Python searches:

```text
1. Instance namespace
2. Class namespace
3. Parent classes (inheritance)
```

---

### Example: Lookup Behavior

```python
class Demo:
    x = 10

d = Demo()
print(d.x)
```

✔ Found in class

---

### Now Add Instance Variable

```python
d.x = 99
print(d.x)
```

✔ Instance variable overrides class variable

---

## Shadowing Explained

Instance variables **shadow** class variables.

```text
Instance → Higher priority
```

---

## 4. Modifying Class Variables

---

### Via Class (Preferred)

```python
Demo.x = 50
```

✔ Affects all objects

---

### Via Instance (Dangerous)

```python
d.x = 50
```

Creates NEW instance variable

---

### Example

```python
class Demo:
    x = 10

d1 = Demo()
d2 = Demo()

d1.x = 99

print(d1.x)
print(d2.x)
```

**Output:**
```text
99
10
```

Only d1 changed

---

## 5. The Most Dangerous Pitfall 🚨🔥

### Mutable Class Variables Bug

---

### WRONG DESIGN

```python
class Person:
    hobbies = []
```

```python
p1 = Person()
p2 = Person()

p1.hobbies.append("Coding")

print(p2.hobbies)
```

**Output:**
```text
['Coding']
```

WHY?!

Because:

✔ Class variable shared  
✔ List is mutable  
✔ Mutation affects everyone

---

## Rule of Survival

**Never use mutable objects as class variables**

Avoid:

❌ list  
❌ dict  
❌ set  

---

### CORRECT DESIGN

```python
class Person:
    def __init__(self):
        self.hobbies = []
```

✔ Each object gets independent list

---

## 6. Instance vs Class Variable Comparison

| Feature | Instance Variable | Class Variable |
|----------|------------------|----------------|
| Belongs To | Object | Class |
| Shared? | ❌ No | ✅ Yes |
| Memory | Per object | Single copy |
| Defined Using | self.var | var |
| Lookup Priority | High | Lower |
| Mutation Impact | Isolated | Global |

---

## 7. When Should You Use Class Variables?

Use class variables for:

✔ Constants  
✔ Shared configuration  
✔ Metadata  
✔ Counters  
✔ Defaults

Example:

```python
class User:
    platform = "WebApp"
```

---

## 8. Real-World Use Case: Object Counter

```python
class Person:
    population = 0

    def __init__(self):
        Person.population += 1
```

```python
p1 = Person()
p2 = Person()

print(Person.population)
```

**Output:**
```text
2
```

✔ Shared state tracking

---

## 9. Inspecting Namespaces (Master Level Insight)

---

### Instance Namespace

```python
print(object.__dict__)
```

---

### Class Namespace

```python
print(Class.__dict__)
```

---

## 10. Common Beginner Mistakes 🚨

| Mistake | Result |
|----------|----------|
| Using mutable class variable | Shared bugs |
| Modifying class variable via instance | Shadowing confusion |
| Confusing lookup order | Unexpected values |
| Overwriting shared data accidentally | Hard-to-debug bugs |
| Treating class variables as instance variables | Logical errors |

---

## Best Practices

✔ Instance variables → Object-specific data  
✔ Class variables → Shared / constant data  
✔ Avoid mutable class variables  
✔ Modify shared data via class  
✔ Understand lookup order  
✔ Use class variables intentionally

---

## Summary

| Concept | Truth |
|----------|---------|
| Instance Variable | Per-object storage |
| Class Variable | Shared storage |
| Lookup Order | Instance → Class |
| Shadowing | Instance overrides class |
| Mutable Class Variables | 🚨 Dangerous |
| Best Design | Prefer instance variables for mutable data |

---

## Practice Tasks

1. Create class with both variable types  
2. Demonstrate lookup order  
3. Create shadowing example  
4. Trigger mutable class variable bug  
5. Build population counter  
6. Inspect namespaces  
7. Predict outputs before running  
