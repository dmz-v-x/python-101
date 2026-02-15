## Lambda Functions in Python

A **lambda function** in Python is a **small, anonymous function** defined using the `lambda` keyword.

- It has **no name**
- It can take **any number of arguments**
- It can contain **only one expression**
- It **returns the result automatically**

Lambda functions are often used when a function is needed **for a short time** and **simple logic**.

---

##  What is a Lambda Function?

### Normal Function
```python
def square(x):
    return x * x
```

### Equivalent Lambda Function
```python
square = lambda x: x * x
```

Both produce the same result.

---

## Syntax of Lambda Function

```python
lambda arguments: expression
```

- `lambda` → keyword
- `arguments` → inputs (like parameters)
- `expression` → single expression whose result is returned

⚠️ **No `return` keyword** is used — it’s implicit.

---

## 1. Simple Lambda Function

```python
square = lambda x: x * x
print(square(5))
```

**Output:**
```text
25
```

---

## 2. Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(3, 4))
```

**Output:**
```text
7
```

---

## 3. Lambda with No Arguments

```python
say_hello = lambda: "Hello!"
print(say_hello())
```

**Output:**
```text
Hello!
```

---

 ## 4. Lambda with Conditional Logic (Ternary)

Since lambdas allow **only one expression**, conditional logic must be written using a **ternary expression**.

```python
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(10))
print(is_even(7))
```

**Output:**
```text
Even
Odd
```

---

## 5. Lambda vs Normal Function

### Normal Function
```python
def multiply(a, b):
    return a * b
```

### Lambda Function
```python
multiply = lambda a, b: a * b
```

✅ Use lambda when:
- Logic is simple
- Function is short-lived

❌ Avoid lambda when:
- Logic is complex
- Multiple statements are required

---

## 6. Lambda with Built-in Functions

Lambda functions shine when used with **higher-order functions**.

---

### `map()` + Lambda

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)
```

**Output:**
```text
[1, 4, 9, 16]
```

---

### `filter()` + Lambda

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```

**Output:**
```text
[2, 4, 6]
```

---

### `sorted()` + Lambda

```python
points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)
```

**Output:**
```text
[(5, 0), (3, 1), (1, 2)]
```

---

## 7. Lambda Inside Functions

```python
def apply_function(func, value):
    return func(value)

print(apply_function(lambda x: x * 2, 10))
```

**Output:**
```text
20
```

---

##️ 8. Lambda and `*args`

```python
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4))
```

**Output:**
```text
10
```

---

## 9. What Lambda Functions CANNOT Do

❌ Cannot contain multiple expressions  
❌ Cannot have statements like `print`, `for`, `while`, `try`  
❌ Cannot have assignments (`=`)  
❌ Hard to debug when overused  

---

## Common Mistakes & Errors

| Mistake | Why It Happens |
|------|---------------|
| Writing complex logic | Lambda allows only one expression |
| Overusing lambdas | Reduces readability |
| Using for long functions | Lambdas are meant to be short |
| Expecting statements | Lambdas support expressions only |
| Debugging difficulty | No function name |

---

## When to Use Lambda vs `def`

| Scenario | Use |
|------|----|
| One-line simple logic | Lambda |
| Reusable logic | `def` |
| Passed as argument | Lambda |
| Complex logic | `def` |
| Debugging needed | `def` |

---

## Summary

| Feature | Lambda Function |
|------|----------------|
| Name | Anonymous |
| Lines | Single line |
| Return | Implicit |
| Statements | ❌ Not allowed |
| Best use | Short-lived functions |

---

## Practice Tasks

1. Create a lambda to check if a number is positive or negative.  
2. Use `map()` with lambda to convert a list of temperatures from °C to °F.  
3. Sort a list of dictionaries by a specific key using lambda.  
4. Rewrite a small `def` function as a lambda.  
5. Explain why lambda should not replace all functions.
