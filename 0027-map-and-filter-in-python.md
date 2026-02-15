## `map` and `filter` in Python

`map()` and `filter()` are **built-in higher-order functions** in Python.  
They are commonly used to **process collections** (like lists, tuples, etc.) in a **clean, functional style**.

- `map()` → **Transforms** each element
- `filter()` → **Selects** elements based on a condition

They are often used together with **lambda functions**.

---

## What Are Higher-Order Functions?

A **higher-order function** is a function that:
- Takes another function as an argument, or
- Returns a function

Both `map()` and `filter()` accept a **function** as their first argument.

---

## 1. `map()` Function

### What `map()` Does

`map()` applies a function to **each element** of an iterable and returns a **map object** (iterator).

### Syntax

```python
map(function, iterable)
```

---

## 2. Basic Example of `map()`

```python
numbers = [1, 2, 3, 4]

def square(x):
    return x * x

result = map(square, numbers)
print(list(result))
```

**Output:**
```text
[1, 4, 9, 16]
```

Each element is passed to `square()`  
Result is collected into a new list

---

## 3. `map()` with Lambda Function

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)
```

**Output:**
```text
[1, 4, 9, 16]
```

✅ Shorter  
✅ Cleaner  
✅ Commonly used in real-world code

---

## 4. `map()` with Multiple Iterables

`map()` can work with **multiple iterables** in parallel.

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))
print(result)
```

**Output:**
```text
[5, 7, 9]
```

Stops at the **shortest iterable**

---

## 5. `map()` vs Loop

### Using `for` Loop

```python
result = []
for num in numbers:
    result.append(num * 2)
```

---

### Using `map()`

```python
result = list(map(lambda x: x * 2, numbers))
```

✅ Less code  
✅ More declarative  
❌ May be less readable for beginners

---

## 6. `filter()` Function

### What `filter()` Does

`filter()` selects elements from an iterable **based on a condition**.

### Syntax

```python
filter(function, iterable)
```

- Function must return `True` or `False`

---

## 7. Basic Example of `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)
print(list(result))
```

**Output:**
```text
[2, 4, 6]
```

---

## 8. `filter()` with Lambda Function

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

## 9. `filter()` vs Loop

### Using `for` Loop

```python
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
```

---

### Using `filter()`

```python
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

✅ Cleaner intent  
❌ Logic hidden inside lambda

---

## 10. Combining `map()` and `filter()`

You can chain them together.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers))
)

print(result)
```

**Output:**
```text
[4, 16, 36]
```

🔹 Step-by-step:
1. `filter()` → `[2, 4, 6]`
2. `map()` → `[4, 16, 36]`

---

## 11. `map()` & `filter()` Return Type

Both return **iterators**, not lists.

```python
result = map(lambda x: x * 2, [1, 2, 3])
print(result)
```

**Output:**
```text
<map object at 0x...>
```

You must convert them:

```python
list(result)
```

---

## 12. `map()` / `filter()` vs List Comprehension

### List Comprehension (Often Preferred)

```python
squares = [x * x for x in numbers if x % 2 == 0]
```

---

### Equivalent with `map()` + `filter()`

```python
squares = list(map(lambda x: x * x,
                   filter(lambda x: x % 2 == 0, numbers)))
```

✅ List comprehensions are usually **more readable**

---

## Common Mistakes & Errors

| Mistake | Reason |
|------|-------|
| Forgetting to convert to list | Returns iterator |
| Writing complex lambdas | Hurts readability |
| Expecting `filter()` to modify list | It returns new iterable |
| Overusing `map()` | List comprehensions are clearer |
| Mixing side effects | Breaks functional style |

---

## When to Use What?

| Scenario | Best Choice |
|------|-------------|
| Simple transformation | `map()` |
| Simple filtering | `filter()` |
| Readability | List comprehension |
| Functional pipelines | `map()` + `filter()` |
| Complex logic | Normal loops |

---

## Summary

| Function | Purpose |
|------|---------|
| `map()` | Transform each element |
| `filter()` | Select elements conditionally |
| Input | Function + iterable |
| Output | Iterator |
| Common Pair | Lambda functions |

---

## Practice Tasks

1. Use `map()` to convert a list of Celsius temperatures to Fahrenheit.  
2. Use `filter()` to remove empty strings from a list.  
3. Combine `map()` and `filter()` to square only odd numbers.  
4. Rewrite a `map()` example using list comprehension.  
5. Explain when `filter()` is better than a `for` loop.
