## Decorators in Python

A **decorator** is a function that:

✔ Takes another function as input  
✔ Adds extra behavior  
✔ Returns a new function  

```text
Decorators = Function Enhancement
```

---

## Mental Model

Decorator = Wrapper

```text
Original Function → Wrapped → Enhanced Function
```

Example idea:

```text
Before Execution → Extra Logic → After Execution
```

---

## Why Decorators Matter

---

✔ Code reuse  
✔ Clean architecture  
✔ Logging  
✔ Authentication  
✔ Validation  
✔ Performance tracking  
✔ Framework design  

Used EVERYWHERE

---

## Functions Are Objects

Python allows:

✔ Passing functions  
✔ Returning functions  
✔ Storing functions  

Decorator builds on this

---

## Basic Function Wrapper

---

```python
def decorator_function(original_function):

    def wrapper():
        print("Extra behavior before function")
        original_function()
        print("Extra behavior after function")

    return wrapper
```

---

```python
def greet():
    print("Hello!")
```

---

```python
decorated_greet = decorator_function(greet)
decorated_greet()
```

**Output:**

```text
Extra behavior before function
Hello!
Extra behavior after function
```

Core decorator concept.

---

## Using @ Syntax (Real Python Way)

---

```python
@decorator_function
def greet():
    print("Hello!")
```

✔ Equivalent to:

```python
greet = decorator_function(greet)
```

---

## What Happened Internally?

---

```text
@decorator → Automatic Wrapping
```

Python rewires function

---

## Decorator with Arguments

---

Problem:

Wrapper must accept arguments.

---

## Correct Version

```python
def decorator_function(original_function):

    def wrapper(*args, **kwargs):
        print("Before execution")
        result = original_function(*args, **kwargs)
        print("After execution")
        return result

    return wrapper
```

---

```python
@decorator_function
def greet(name):
    print(f"Hello, {name}!")
```

---

```python
greet("Alice")
```

**Output:**

```text
Before execution
Hello, Alice!
After execution
```

✔ Flexible decorator

---

## Decorators Return Values

---

```python
@decorator_function
def add(a, b):
    return a + b
```

```python
print(add(2, 3))
```

**Output:**

```text
Before execution
After execution
5
```

✔ Return preserved.

---

## Real-World Example — Logging

---

```python
def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called")
        return func(*args, **kwargs)

    return wrapper
```

---

```python
@logger
def multiply(a, b):
    return a * b
```

---

```python
print(multiply(3, 4))
```

**Output:**

```text
Function multiply called
12
```

---

## Decorators with Parameters 

Decorator factory.

---

## Example

```python
def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

---

```python
@repeat(3)
def greet():
    print("Hello!")
```

---

```python
greet()
```

**Output:**

```text
Hello!
Hello!
Hello!
```

 Advanced decorator mastery.

---

## Decorators + Closures

Decorator works because:

✔ Wrapper remembers original function  
✔ Closure retains context  

---

## Deadly Gotchas

---

## Gotcha #1 — Losing Function Metadata

---

```python
print(greet.__name__)
```

Shows wrapper name.

---

## Fix → functools.wraps

```python
from functools import wraps

def decorator_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

✔ Preserves metadata

---

## Gotcha #2 — Forgetting Return

---

```python
def wrapper():
    func()
```

Return lost.

✔ Always return result

---

## Gotcha #3 — Overusing Decorators

Too many decorators = Confusing code

---

## Gotcha #4 — Execution Order 

---

```python
@A
@B
def func():
```

Equivalent:

```text
func = A(B(func))
```

Order matters.

---

## Gotcha #5 — Mutable State Bugs 

Decorators holding shared mutable data → Dangerous.

---

## Deep Design Insight 

Decorators enable:

✔ Aspect-Oriented Programming  
✔ Cross-cutting concerns  
✔ Clean architecture layers  
✔ Middleware design  
✔ Framework internals  

Core of Python ecosystem

---

## When To Use Decorators

---

Logging  
Validation  
Authentication  
Timing  
Caching  
Rate limiting  
Access control  
Instrumentation  

Avoid for trivial logic.

---

## Best Practices

---

✔ Use wraps()  
✔ Preserve return values  
✔ Keep decorators simple  
✔ Avoid hidden side effects  
✔ Name clearly  
✔ Avoid decorator abuse  

---

## Summary

✔ Decorators = Function wrappers 
✔ Use @ syntax  
✔ Accept args via *args, **kwargs  
✔ Can return values  
✔ Can accept parameters  
✔ Powered by closures   
✔ Metadata issues → wraps()  
✔ Order matters  

---

## Practice Tasks

1. Create simple decorator  
2. Add before/after logic  
3. Decorator with arguments  
4. Decorator returning values  
5. Logging decorator  
6. Decorator with parameters  
7. Stack multiple decorators  
8. Fix metadata using wraps  
