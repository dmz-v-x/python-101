## `*args` vs `**kwargs`

Python functions can accept arguments in **multiple flexible ways**.  
Understanding how arguments are passed is crucial for writing **clean, reusable, and scalable functions**.

Python supports:
- Positional arguments
- Keyword arguments
- Default arguments
- Variable-length positional arguments (`*args`)
- Variable-length keyword arguments (`**kwargs`)

---

## Key Terminology

| Term | Meaning |
|----|--------|
| Parameter | Variable defined in function |
| Argument | Value passed to function |
| Positional argument | Matched by position |
| Keyword argument | Matched by parameter name |
| `*args` | Variable positional arguments |
| `**kwargs` | Variable keyword arguments |

---

## 1. Positional Arguments

Positional arguments are assigned **based on order**.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Alice")
```

**Output:**
```text
Hello, Alice
```

`"Alice"` is assigned to `name` because it’s the **first parameter**.

---

## 2. Keyword Arguments

Keyword arguments are passed using **parameter names**, so order does **not** matter.

```python
greet(name="Bob", greeting="Hi")
greet(greeting="Hola", name="Mike")
```

**Output:**
```text
Hi, Bob
Hola, Mike
```

---

### Empty Keyword Arguments

```python
greet(greeting="", name="")
```

**Output:**
```text
, 
```

Python allows empty values — validation is your responsibility.

---

## 3. Mixing Positional and Keyword Arguments

Positional arguments must come **before** keyword arguments.

```python
def introduction(first_name, last_name, age):
    print(f"Hi, I'm {first_name} {last_name}, and I'm {age} years old.")

introduction("John", last_name="Doe", age=28)
```

**Output:**
```text
Hi, I'm John Doe, and I'm 28 years old.
```

---

### Invalid Order

```python
# introduction(first_name="John", "Doe", age=28)
```

**Error:**
```text
SyntaxError: positional argument follows keyword argument
```

---

## 4. Keyword Arguments with All Parameters

```python
def info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

info(age=30, name="Charlie", city="San Francisco")
```

**Output:**
```text
Name: Charlie, Age: 30, City: San Francisco
```

Keyword arguments make function calls **self-documenting**.

---

## 5. Default Arguments + Positional Arguments

```python
def greeting(name, message="Howdy"):
    print(f"{message}, {name}!")

greeting("Alice")
greeting("Bob", message="Welcome")
greeting("Michelle")
```

**Output:**
```text
Howdy, Alice!
Welcome, Bob!
Howdy, Michelle!
```

Default parameters are used **only if not overridden**.

---

## 6. Variable-Length Positional Arguments (`*args`)

`*args` allows a function to accept **any number of positional arguments**.

```python
def sum_all(*args):
    print(args)

sum_all(1, 2, 3, 4)
```

**Output:**
```text
(1, 2, 3, 4)
```

Inside the function, `args` is a **tuple**.

---

### Practical Example

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
```

**Output:**
```text
15
```

---

## 7. Variable-Length Keyword Arguments (`**kwargs`)

`**kwargs` allows a function to accept **any number of keyword arguments**.

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
```

**Output:**
```text
name: Alice
age: 30
city: New York
```

Inside the function, `kwargs` is a **dictionary**.

---

## 8. Using `*args` and `**kwargs Together`

Order matters:

```python
def demo(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

demo(1, 2, 3, 4, x=10, y=20)
```

**Output:**
```text
1 2
(3, 4)
{'x': 10, 'y': 20}
```

---

### Correct Order Rule

```text
1. Positional parameters
2. *args
3. Keyword-only parameters (optional)
4. **kwargs
```

---

## 9. Why `*args` and `**kwargs` Are Powerful

✅ Build flexible APIs  
✅ Accept optional inputs  
✅ Forward arguments to other functions  
✅ Useful in decorators and frameworks  

---

## Common Mistakes & Errors

| Mistake | Reason |
|------|-------|
| Mixing order incorrectly | Positional after keyword |
| Forgetting `*` or `**` | Syntax error |
| Treating `args` as list | It’s a tuple |
| Treating `kwargs` as list | It’s a dictionary |
| Overusing `*args` | Reduces readability |

---

## Comparison Summary

| Feature | Positional | Keyword | `*args` | `**kwargs` |
|------|-----------|--------|--------|-----------|
| Order matters | ✅ | ❌ | ✅ | ❌ |
| Variable length | ❌ | ❌ | ✅ | ✅ |
| Data type inside | — | — | Tuple | Dictionary |
| Readability | Medium | High | Medium | High |

---

## Practice Tasks

1. Write a function that accepts any number of numbers and returns their average using `*args`.  
2. Create a function that prints user details using `**kwargs`.  
3. Mix positional, default, `*args`, and `**kwargs` in one function.  
4. Rewrite a function call using only keyword arguments.  
5. Explain why keyword arguments improve readability.
