## Handling Function Return

In Python, the **`return` statement** is used to:
- Send a value back from a function to the caller
- Stop the execution of the function immediately

A function can:
- Return **nothing**
- Return **one value**
- Return **multiple values**
- Exit **early** using `return`

Understanding function return behavior is **critical** for writing correct and predictable programs.

---

## Key Facts About `return`

| Rule | Explanation |
|----|------------|
| `return` ends a function | Code after `return` is never executed |
| Functions always return something | Even if you don’t write `return` |
| Multiple values are returned as a tuple | Python packs them automatically |
| `return` without value → `None` | Explicit or implicit |

---

## 1. Returning Nothing (Implicit `None`)

If a function does **not** have a `return` statement, Python automatically returns `None`.

```python
def greet():
    print("Hello!")

result = greet()
print(result)
```

**Output:**
```text
Hello!
None
```

`None` represents **absence of a value**.

---

### Explicitly Returning `None`

```python
def do_nothing():
    return

print(do_nothing())
```

**Output:**
```text
None
```

Both implicit and explicit returns behave the same.

---

## 2. Returning a Single Value

A function can return **one value** using `return`.

```python
def square(x):
    return x * x

result = square(5)
print(result)
```

**Output:**
```text
25
```

The returned value can be:
- Stored in a variable
- Passed to another function
- Printed directly

---

## 3. Returning Multiple Values

Python allows returning **multiple values** separated by commas.

```python
def calculate(a, b):
    return a + b, a - b, a * b

result = calculate(10, 5)
print(result)
```

**Output:**
```text
(15, 5, 50)
```

Internally, Python returns a **tuple**.

---

### Unpacking Multiple Return Values

```python
sum_, diff, product = calculate(10, 5)
print(sum_)
print(diff)
print(product)
```

**Output:**
```text
15
5
50
```

---

## 4. Returning Early from a Function

`return` immediately exits the function — even inside loops or conditionals.

```python
def check_positive(num):
    if num <= 0:
        return "Not positive"
    return "Positive number"

print(check_positive(-5))
print(check_positive(10))
```

**Output:**
```text
Not positive
Positive number
```

This is called an **early return**.

---

### Early Return Inside a Loop

```python
def find_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

print(find_even([1, 3, 5, 6, 7]))
```

**Output:**
```text
6
```

---

## 5. Using `_` to Store Unused Return Values

In Python, `_` is commonly used to indicate:
> “I don’t care about this value”

---

### Ignoring Returned Values

```python
def get_coordinates():
    return 10, 20, 30

x, _, z = get_coordinates()
print(x)
print(z)
```

**Output:**
```text
10
30
```

`_` is just a variable name by convention, but widely understood as **ignored value**.

---

### Using `_` When You Don’t Need the Return

```python
def log_message():
    print("Logged!")

_ = log_message()
```

**Output:**
```text
Logged!
```

---

## 6. Returning Different Types Conditionally

A function can return **different types**, but this should be used carefully.

```python
def divide(a, b):
    if b == 0:
        return None
    return a / b

print(divide(10, 2))
print(divide(10, 0))
```

**Output:**
```text
5.0
None
```

Caller must handle `None` safely.

---

## Common Mistakes & Errors

| Mistake | Why It Happens |
|------|---------------|
| Forgetting `return` | Function returns `None` |
| Code after `return` | Never executes |
| Expecting multiple values without unpacking | Returns tuple |
| Ignoring `None` checks | Causes runtime errors |
| Returning inconsistent types | Confusing behavior |

---

## Summary

| Scenario | Behavior |
|------|---------|
| No `return` | Returns `None` |
| `return value` | Returns one value |
| `return a, b` | Returns a tuple |
| Early `return` | Exits function immediately |
| `_` variable | Used to ignore values |

---

## Practice Tasks

1. Write a function that returns nothing and verify it returns `None`.  
2. Create a function that returns both the square and cube of a number.  
3. Write a function that stops execution early if input is invalid.  
4. Use `_` to ignore one value from a function returning three values.  
5. Modify a function to return `None` when an error occurs.
