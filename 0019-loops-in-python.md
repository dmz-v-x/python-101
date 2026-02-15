## Loops in Python

A **`for` loop** in Python is used to **iterate over a sequence** (also called an *iterable*), such as:

- Lists
- Tuples
- Strings
- Dictionaries
- Sets
- Ranges
- Any iterable object

For **each item** in the iterable, the `for` loop executes a block of code.

```python
for item in iterable:
    # code to execute
```

---

## Core Concepts Behind `for` Loops

| Term | Meaning |
|----|--------|
| `item` | Temporary variable holding current element |
| `iterable` | Object that can be looped over |
| Iteration | One complete pass over an element |
| Loop body | Code executed on each iteration |

---

## 1. Basic `for` Loop Example

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**
```text
apple
banana
cherry
```

---

## 2. Looping Through a List

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

**Output:**
```text
1
2
3
4
5
```

---

## 3. Looping Through a Tuple

```python
tuple_data = (10, 20, 30)
for item in tuple_data:
    print(item)
```

**Output:**
```text
10
20
30
```

---

## 4. Looping Through a String

Strings are iterable character by character.

```python
word = "Python"
for char in word:
    print(char)
```

**Output:**
```text
P
y
t
h
o
n
```

---

## 5. Looping Through a Dictionary

### Looping Through Keys (Default Behavior)

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
for key in my_dict:
    print(key)
```

**Output:**
```text
name
age
city
```

---

### Looping Through Values

```python
for value in my_dict.values():
    print(value)
```

**Output:**
```text
Alice
30
New York
```

---

### Looping Through Keys and Values

```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

**Output:**
```text
name: Alice
age: 30
city: New York
```

---

## 6. Looping Through a Set

Sets are **unordered**, so output order may vary.

```python
my_set = {10, 20, 30}
for item in my_set:
    print(item)
```

**Output (order may vary):**
```text
10
20
30
```

---

## 7. `for-else` Block

The `else` block runs **only if the loop finishes normally** (no `break`).

```python
numbers = [1, 2, 3]
for num in numbers:
    print(num)
else:
    print("Loop finished!")
```

**Output:**
```text
1
2
3
Loop finished!
```

---

### `for-else` with `break`

```python
numbers = [1, 2, 3]
for num in numbers:
    if num == 2:
        break
    print(num)
else:
    print("Loop finished!")
```

**Output:**
```text
1
```

`else` does **NOT** execute because the loop was broken.

---

## 8. `break` and `continue`

### `break` → Stops the loop immediately

```python
for num in range(5):
    if num == 3:
        break
    print(num)
```

**Output:**
```text
0
1
2
```

---

### `continue` → Skips current iteration

```python
for num in range(5):
    if num == 3:
        continue
    print(num)
```

**Output:**
```text
0
1
2
4
```

---

## 9. `range()` Function

### Basic `range(stop)`

```python
for i in range(5):
    print(i)
```

**Output:**
```text
0
1
2
3
4
```

---

### `range(start, stop, step)`

```python
for i in range(2, 10, 2):
    print(i)
```

**Output:**
```text
2
4
6
8
```

---

## 10. `enumerate()`

Provides **index and value** together.

```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
```

**Output:**
```text
0: Alice
1: Bob
2: Charlie
```

---

## 11. `zip()`

Iterates over **multiple iterables together**.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```

**Output:**
```text
Alice is 25 years old.
Bob is 30 years old.
Charlie is 35 years old.
```

Stops at the **shortest iterable**.

---

## 12. Looping in Sorted Order

```python
numbers = [5, 1, 4, 2, 3]
for num in sorted(numbers):
    print(num)
```

**Output:**
```text
1
2
3
4
5
```

---

## 13. Looping in Reverse Order

```python
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)
```

**Output:**
```text
5
4
3
2
1
```

---

## 14. Loop Fallback & `in` Keyword

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

if "apple" in fruits:
    print("Apple exists")
```

**Output:**
```text
apple
banana
cherry
Apple exists
```

---

## 15. Walrus Operator (`:=`) in Loops (Python 3.8+)

Allows assignment **inside conditions**.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if (square := num * num) > 10:
        print(square)
```

**Output:**
```text
16
25
```

---

## Common Mistakes & Errors

| Mistake | Why It Happens |
|------|---------------|
| Modifying list during iteration | Causes unexpected behavior |
| Assuming set order | Sets are unordered |
| Infinite loop with `range()` | Incorrect step |
| Forgetting `break` logic | Loop never stops |
| Overusing nested loops | Reduces readability |

---

## Summary

| Feature | Description |
|------|------------|
| `for` loop | Iterates over iterable |
| `range()` | Generates sequence |
| `enumerate()` | Index + value |
| `zip()` | Parallel iteration |
| `break` | Exit loop |
| `continue` | Skip iteration |
| `for-else` | Runs if no break |
| `sorted()` | Ordered looping |
| `reversed()` | Reverse looping |

---

## Practice Tasks

1. Print all even numbers from 1 to 20 using a `for` loop.  
2. Loop through a string and count vowels.  
3. Use `enumerate()` to print index and value of a list.  
4. Combine two lists using `zip()` and print pairs.  
5. Use `for-else` to check if a number exists in a list.  
6. Reverse a list using a loop and `reversed()`.
