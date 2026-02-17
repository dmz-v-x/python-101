## Scopes in Python

**Scope** in Python refers to the **region of a program where a variable name is recognized and accessible**.

Python decides **which variable value to use** based on **where the variable is defined** and **where it is accessed**.

To resolve variable names, Python follows the **LEGB Rule**:

```
Local → Enclosing → Global → Built-in
```

---

## Why Scope Matters

Understanding scope helps you:
- Avoid `NameError` and unexpected values
- Control variable lifetime
- Write safe nested functions
- Understand closures
- Debug tricky bugs involving shared names

---

## Types of Scope in Python

| Scope Type | Description |
|-----------|-------------|
| Local | Inside a function |
| Enclosing (Nonlocal) | Inside outer function (nested functions) |
| Global | Top-level of a module |
| Built-in | Python’s predefined names |

---

## The LEGB Rule (Very Important)

When Python encounters a variable name, it searches in this order:

1. **Local** – inside the current function  
2. **Enclosing** – inside outer (nested) functions  
3. **Global** – at the module level  
4. **Built-in** – Python’s built-in namespace  

First match wins 🏆

---

## 1. Local Scope

Variables declared **inside a function** belong to the **local scope**.

```python
def my_function():
    x = 10  # Local variable
    print("Inside function, x =", x)

my_function()
```

**Output:**
```text
Inside function, x = 10
```

---

### Accessing Local Variable Outside Function ❌

```python
print(x)
```

**Error:**
```text
NameError: name 'x' is not defined
```

Local variables exist **only inside the function**

---

## 2. Global Scope

Variables declared **outside all functions** are in the **global scope**.

```python
x = 10  # Global variable

def my_function():
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)
```

**Output:**
```text
Inside function, x = 10
Outside function, x = 10
```

Global variables are **readable inside functions**

---

## 3. Modifying Global Variables (`global`)

By default, you **cannot modify** a global variable inside a function.

```python
x = 10

def my_function():
    x = 20  # Creates a new local variable

my_function()
print(x)
```

**Output:**
```text
10
```

---

### Using `global` Keyword

```python
x = 10

def my_function():
    global x
    x = 20
    print("Inside function, x =", x)

my_function()
print("Outside function, x =", x)
```

**Output:**
```text
Inside function, x = 20
Outside function, x = 20
```

🔹 `global` tells Python:  
👉 “Use the variable from global scope”

⚠️ Use sparingly — global state can cause bugs.

---

## 4. Enclosing Scope (Nonlocal)

Enclosing scope appears in **nested functions**.

```python
def outer_function():
    x = 5  # Enclosing variable

    def inner_function():
        print("Inside inner_function, x =", x)

    inner_function()

outer_function()
```

**Output:**
```text
Inside inner_function, x = 5
```

---

## 5. Modifying Enclosing Variables (`nonlocal`)

Without `nonlocal`, assignment creates a new local variable.

```python
def outer_function():
    x = 5

    def inner_function():
        x = 10  # Local to inner_function

    inner_function()
    print(x)

outer_function()
```

**Output:**
```text
5
```

---

### Using `nonlocal`

```python
def outer_function():
    x = 5

    def inner_function():
        nonlocal x
        x = 10
        print("Inside inner_function, x =", x)

    inner_function()
    print("Inside outer_function, after inner_function, x =", x)

outer_function()
```

**Output:**
```text
Inside inner_function, x = 10
Inside outer_function, after inner_function, x = 10
```

`nonlocal` allows modification of **enclosing scope variables**

---

## 6. Built-in Scope

Built-in scope contains Python’s **predefined names**.

Examples:
- `print`
- `len`
- `range`
- `input`
- `int`

```python
print(len("Python"))
```

---

### Shadowing Built-ins (Dangerous ⚠️)

```python
len = 5
print(len("hello"))
```

**Error:**
```text
TypeError: 'int' object is not callable
```

❌ Avoid overriding built-in names.

---

## 7. Scope Lookup Example (LEGB in Action)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

**Output:**
```text
local
```

Python finds `x` in **Local scope first**

---

## Common Scope Pitfalls

| Mistake | Why It Happens |
|------|---------------|
| `NameError` | Variable not in scope |
| Unexpected values | Shadowing variables |
| Global mutation bugs | Overusing `global` |
| Closure confusion | Enclosing scope misunderstanding |
| Built-in override | Shadowing built-ins |

---

## Best Practices

✅ Prefer local variables  
✅ Avoid `global` when possible  
✅ Use `nonlocal` intentionally  
✅ Keep scopes small and clear  
❌ Don’t shadow built-ins  

---

## Summary

| Scope | Accessible Where |
|------|------------------|
| Local | Inside the function |
| Enclosing | Inside nested functions |
| Global | Entire module |
| Built-in | Everywhere |

| Keyword | Purpose |
|------|--------|
| `global` | Modify global variable |
| `nonlocal` | Modify enclosing variable |

---

## Practice Tasks

1. Write a nested function and modify an outer variable using `nonlocal`.  
2. Demonstrate LEGB lookup using same variable name in all scopes.  
3. Show how shadowing a built-in causes errors.  
4. Rewrite a `global` example without using `global`.  
5. Explain why Python forbids modifying globals by default.
