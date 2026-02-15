## Pure vs Impure Functions

In Python (and programming in general), functions can be classified based on **how they interact with data outside themselves**.

There are two important categories:

- **Pure functions**
- **Impure functions**

Understanding this distinction helps you write:
- More predictable code
- Easier-to-test functions
- Cleaner, bug-free programs

---

## What Is a Pure Function?

A **pure function** is a function that:

1. **Always returns the same output** for the same input  
2. **Does not cause side effects**

### Side effects include:
- Modifying global variables
- Changing mutable objects passed as arguments
- Printing to console
- Reading user input
- Writing to files or databases

---

## 1. Example of a Pure Function

```python
def add(a, b):
    return a + b
```

```python
print(add(2, 3))
print(add(2, 3))
```

**Output:**
```text
5
5
```

✅ Same input → same output  
✅ No external state used  
✅ No side effects  

---

## 2. Characteristics of Pure Functions

| Property | Description |
|-------|-------------|
| Deterministic | Same input → same output |
| No side effects | Does not modify outside state |
| Independent | Depends only on arguments |
| Easy to test | No setup or cleanup required |
| Safe to reuse | No hidden behavior |

---

## 3. Example of an Impure Function

An **impure function** either:
- Depends on external state  
- Modifies external state  
- Produces side effects  

```python
x = 10

def add_to_x(y):
    return x + y
```

```python
print(add_to_x(5))
```

**Output:**
```text
15
```

❌ Output depends on global variable `x`

---

## 4. Impure Function with Side Effects

### Modifying Global State

```python
count = 0

def increment():
    global count
    count += 1
```

```python
increment()
increment()
print(count)
```

**Output:**
```text
2
```

❌ Function modifies external state  
❌ Output depends on previous calls  

---

## 5. Impure Function Modifying Mutable Arguments

```python
def add_item(lst):
    lst.append(100)
```

```python
my_list = [1, 2, 3]
add_item(my_list)
print(my_list)
```

**Output:**
```text
[1, 2, 3, 100]
```

❌ Function mutates the input  
❌ Side effect introduced  

---

## 6. Impure Function with I/O

```python
def greet(name):
    print(f"Hello, {name}")
```

```python
greet("Alice")
```

**Output:**
```text
Hello, Alice
```

❌ Printing is a side effect  
❌ Output is not returned  

---

## 7. Making an Impure Function Pure

### ❌ Impure Version

```python
tax_rate = 0.1

def calculate_tax(price):
    return price * tax_rate
```

---

### ✅ Pure Version

```python
def calculate_tax(price, tax_rate):
    return price * tax_rate
```

All required data is passed explicitly.

---

## 8. Pure vs Impure — Side-by-Side

| Feature | Pure Function | Impure Function |
|------|--------------|----------------|
| Depends on global state | ❌ No | ✅ Yes |
| Has side effects | ❌ No | ✅ Yes |
| Predictable output | ✅ Yes | ❌ No |
| Easy to test | ✅ Yes | ❌ No |
| Debug friendly | ✅ Yes | ❌ No |

---

## 9. Why Pure Functions Matter

Pure functions provide:

- 🔁 **Referential transparency**  
- 🧪 **Easy unit testing**  
- 🔄 **Safe reuse**  
- 🧵 **Concurrency safety**  
- 📉 **Fewer bugs**

This is why **functional programming** emphasizes purity.

---

## 10. Are Lambdas Pure?

Lambda functions **can be pure or impure**.

### Pure Lambda

```python
square = lambda x: x * x
```

---

### Impure Lambda

```python
counter = 0
increment = lambda: globals().__setitem__('counter', counter + 1)
```

❌ Depends on and modifies external state.

---

## Common Misconceptions

| Misconception | Reality |
|--------------|--------|
| Pure functions are slow | They’re often faster |
| Python doesn’t support purity | Python supports it fully |
| Printing is harmless | It’s a side effect |
| Mutating inputs is okay | Breaks predictability |

---

## Best Practices

✅ Prefer pure functions whenever possible  
✅ Pass all required data explicitly  
✅ Avoid modifying arguments  
❌ Avoid `global` state  
❌ Avoid hidden dependencies  

---

## Summary

| Concept | Pure | Impure |
|------|------|-------|
| Deterministic | ✅ | ❌ |
| Side effects | ❌ | ✅ |
| External state | ❌ | ✅ |
| Testability | High | Low |
| Maintainability | High | Low |

---

## Practice Tasks

1. Write a pure function to convert Celsius to Fahrenheit.  
2. Convert an impure function into a pure one.  
3. Identify side effects in a given function.  
4. Write a function that mutates input and explain why it’s impure.  
5. Explain why pure functions are easier to debug.
