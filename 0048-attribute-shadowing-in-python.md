## Attribute Shadowing in Python

**Attribute Shadowing** occurs when:

👉 An **instance variable** has the **same name** as a **class variable**.

Result:

✔ Instance variable overrides class variable  
✔ Class variable remains unchanged  

---

## Critical Mental Model

Python attribute lookup order:

```text
1. Object Namespace (Highest Priority)
2. Class Namespace
3. Parent Classes
```

Instance namespace always wins.

---

## 1. Basic Example of Shadowing

---

### Class with Class Variable

```python
class Demo:
    value = 10
```

---

### Create Object

```python
d = Demo()
print(d.value)
```

**Output:**
```text
10
```

✔ Found in class namespace

---

## 2. Shadowing Happens Here

Assign same attribute via instance:

```python
d.value = 99
```

```python
print(d.value)
print(Demo.value)
```

**Output:**
```text
99
10
```

---

## What Just Happened?

Python created:

✔ NEW variable inside object namespace

```python
print(d.__dict__)
```

**Output:**
```text
{'value': 99}
```

✔ Class variable untouched

---

## Golden Rule

```text
Assignment via object NEVER modifies class variable
```

It creates a new instance variable instead.

---

## 3. Why Does Shadowing Exist?

Because Python lookup prioritizes:

👉 Instance → Class

This enables:

✔ Object-specific overrides  
✔ Flexible object behavior  
✔ Dynamic customization

---

## 4. Visualizing Shadowing

Before shadowing:

```text
Class Namespace → value = 10
Object Namespace → empty
```

After:

```text
Class Namespace → value = 10
Object Namespace → value = 99
```

Lookup:

```text
object.value → finds instance first → 99
```

---

## 5. Shadowing vs Mutation (VERY IMPORTANT)

Shadowing ≠ Mutation

---

### Shadowing → New Variable

```python
d.value = 99
```

---

### Mutation → Modify Existing Object

```python
Demo.value = 99
```

Affects all instances.

---

## 6. Dangerous Pitfall 🚨🔥

---

### Mutable Class Variable Nightmare

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

WHY?

Because:

✔ No shadowing happened  
✔ Lookup found class variable  
✔ Mutation modified shared object

---

## When Shadowing DOES Occur

```python
p1.hobbies = []
```

Now:

✔ Instance variable created  
✔ Shadowing activated

---

## 7. Shadowing Methods? Yes

Methods are class attributes.

---

### Example

```python
class Demo:
    def greet(self):
        print("Hello")
```

```python
d = Demo()
d.greet = "Not a method anymore"

print(d.greet)
```

Method shadowed!

---

## Why This is Dangerous

✔ Breaks object behavior  
✔ Confusing debugging  
✔ Silent logical errors

---

## 8. Shadowing Lookup Mechanics

```python
print(d.__dict__)     # Instance namespace
print(Demo.__dict__)  # Class namespace
```

---

## 9. Shadowing vs Overriding (Different Concepts)

| Concept | Meaning |
|-------------|-------------|
| Shadowing | Instance hides class attribute |
| Overriding | Child class redefines parent method |

---

## 10. Common Beginner Confusions

| Confusion | Reality |
|--------------|------------|
| Instance modified class variable | ❌ No |
| Shadowing deletes class variable | ❌ No |
| Shadowing = mutation | ❌ |
| Shadowing always bad | ❌ Sometimes intentional |
| Methods immune to shadowing | ❌ No |

---

## When Shadowing is Useful

✔ Temporary overrides  
✔ Object-specific behavior  
✔ Testing / mocking  
✔ Dynamic configurations  

Example:

```python
obj.timeout = 5
```

---

## When Shadowing Causes Bugs

✔ Accidental attribute naming  
✔ Mutable shared state  
✔ Method replacement  
✔ Debugging nightmares  

---

## Best Practices

✔ Avoid naming collisions  
✔ Use instance variables carefully  
✔ Never shadow methods unintentionally  
✔ Avoid mutable class variables  
✔ Understand lookup order  

---

## Summary

| Concept | Truth |
|-------------|------------|
| Shadowing | Instance overrides class lookup |
| Lookup Order | Instance → Class |
| Mutation | Changes shared object |
| Assignment via object | Creates instance variable |
| Class variable unchanged | ✅ Yes |
| Methods can be shadowed | 🚨 Yes |

---

## Practice Tasks

1. Create shadowing examples  
2. Print instance vs class namespaces  
3. Shadow a method intentionally  
4. Trigger mutable class variable bug  
5. Predict outputs before execution  
6. Compare mutation vs shadowing  
7. Create debugging scenario
