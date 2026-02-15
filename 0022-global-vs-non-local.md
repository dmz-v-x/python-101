## `global` vs `nonlocal`

In Python, **variables live in different scopes**.  
When working with functions, you may want to **modify variables defined outside the current function**.

Python provides two keywords for this purpose:

- `global`
- `nonlocal`

Although they look similar, they work in **very different scopes**.

---

## Python Variable Scope (LEGB Rule)

Python resolves variables using the **LEGB rule**:

| Scope | Meaning |
|-----|--------|
| **L**ocal | Inside the current function |
| **E**nclosing | Inside enclosing (outer) functions |
| **G**lobal | Defined at the top-level of the file |
| **B**uilt-in | Python built-ins (`len`, `print`, etc.) |

Understanding this rule is **essential** before using `global` or `nonlocal`.

---

## 1. What is `global`?

The `global` keyword allows a function to **modify a variable defined in the global (module-level) scope**.

Without `global`, assigning to a variable inside a function creates a **new local variable**.

---

### Without `global`

```python
x = 10

def change_x():
    x = 20  # creates a local variable
    print("Inside function:", x)

change_x()
print("Outside function:", x)
```

**Output:**
```text
Inside function: 20
Outside function: 10
```

The global variable was **not changed**.

---

### With `global`

```python
x = 10

def change_x():
    global x
    x = 20
    print("Inside function:", x)

change_x()
print("Outside function:", x)
```

**Output:**
```text
Inside function: 20
Outside function: 20
```

The function modified the **global variable**.

---

## 2. When to Use `global`

Use `global` when:
- The variable is defined **outside all functions**
- You want to **modify it inside a function**

Overusing `global` is discouraged because it:
- Makes code harder to debug
- Creates hidden dependencies
- Can cause unexpected side effects

---

## 3. What is `nonlocal`?

The `nonlocal` keyword is used inside **nested functions**.

It allows a function to modify a variable from its **enclosing (outer) function**, but **not the global scope**.

---

### Without `nonlocal`

```python
def outer():
    x = 10

    def inner():
        x = 20  # creates a new local variable
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
```

**Output:**
```text
Inner: 20
Outer: 10
```

The outer variable was **not changed**.

---

### With `nonlocal`

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
```

**Output:**
```text
Inner: 20
Outer: 20
```

The inner function modified the **enclosing function’s variable**.

---

## 4. Where `nonlocal` Works (and Doesn’t)

### Valid: Enclosing Scope

```python
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)

outer()
```

---

### Invalid: Global Scope

```python
x = 10

def outer():
    def inner():
        nonlocal x  # ❌ Error
        x = 20
```

**Error:**
```text
SyntaxError: no binding for nonlocal 'x' found
```

`nonlocal` **cannot access global variables**.

---

## 5. `global` vs `nonlocal` — Side-by-Side

| Feature | `global` | `nonlocal` |
|------|---------|-----------|
| Modifies variable in | Global scope | Enclosing function scope |
| Works in nested functions | ❌ No | ✅ Yes |
| Affects entire program | ✅ Yes | ❌ No |
| Can access module variables | ✅ Yes | ❌ No |
| Risk level | High | Medium |

---

## 6. Real-World Example: Counter with `nonlocal`

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())
print(c())
print(c())
```

**Output:**
```text
1
2
3
```

This is a **classic closure pattern** — safe and controlled.

---

## 7. Real-World Example: Configuration with `global`

```python
DEBUG = False

def enable_debug():
    global DEBUG
    DEBUG = True

enable_debug()
print(DEBUG)
```

**Output:**
```text
True
```

Used occasionally for application-wide flags.

---

## Common Mistakes & Errors

| Mistake | Why It Happens |
|------|---------------|
| Using `nonlocal` without enclosing scope | Variable doesn’t exist |
| Forgetting `global` | Creates a local variable |
| Overusing `global` | Makes code unpredictable |
| Confusing scopes | Not understanding LEGB |
| Using `global` in libraries | Causes side effects |

---

## Best Practices

✅ Prefer **return values** instead of modifying outer variables  
✅ Use `nonlocal` for **closures and stateful functions**  
❌ Avoid `global` unless absolutely necessary  
❌ Never mix `global` and `nonlocal` for the same variable  

---

## Summary

| Keyword | Purpose |
|------|---------|
| `global` | Modify global variables |
| `nonlocal` | Modify enclosing function variables |
| Scope affected | Entire module vs enclosing function |
| Typical use | Config flags | Closures, counters |

---

## Practice Tasks

1. Create a global counter and modify it using `global`.  
2. Create a nested function that updates a value using `nonlocal`.  
3. Try using `nonlocal` without an enclosing scope and observe the error.  
4. Convert a `global`-based program into a closure using `nonlocal`.  
5. Explain why closures are safer than globals in your own words.
