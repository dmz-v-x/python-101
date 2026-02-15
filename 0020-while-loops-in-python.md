## While Loops in Python

A **`while` loop** in Python repeatedly executes a block of code **as long as a condition remains `True`**.  
The loop stops automatically when the condition becomes `False`.

`while` loops are most useful when:
- The **number of iterations is unknown**
- Execution depends on a **changing condition**
- You want to keep running until something happens (user input, event, state change)

```python
while condition:
    # code runs while condition is True
```

---

## Core Concepts Behind `while` Loops

| Concept | Meaning |
|------|--------|
| Condition | Expression evaluated as `True` or `False` |
| Loop body | Code executed repeatedly |
| Iteration | One cycle of execution |
| Exit condition | Condition that stops the loop |
| Infinite loop | Condition never becomes `False` |

---

## 1. Basic `while` Loop

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

**Output:**
```text
1
2
3
4
5
```

`count += 1` is critical — without it, the loop would run forever.

---

## 2. Infinite `while` Loop

An infinite loop runs **forever** unless explicitly stopped.

```python
while True:
    print("This loop will run forever")
    break
```

**Output:**
```text
This loop will run forever
```

`True` never becomes `False`, so you must use `break`.

---

## 3. `while` Loop with `else`

The `else` block executes **only if the loop ends normally** (not via `break`).

```python
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop has finished")
```

**Output:**
```text
0
1
2
Loop has finished
```

---

### `while-else` with `break`

```python
x = 0
while x < 3:
    if x == 1:
        break
    print(x)
    x += 1
else:
    print("Loop has finished")
```

**Output:**
```text
0
```

`else` does **not** run because the loop exited via `break`.

---

## 4. Using `break` in a `while` Loop

`break` immediately **terminates** the loop.

```python
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
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

## 5. Using `continue` in a `while` Loop

`continue` skips the **current iteration** and jumps back to the condition check.

```python
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

**Output:**
```text
1
2
4
5
```

`3` is skipped.

---

## 6. `while` Loop with User Input

Common real-world use case: keep asking until correct input.

```python
password = ""
while password != "secret":
    password = input("Enter the password: ")

print("Access granted!")
```

Loop continues until the correct password is entered.

---

## 7. Nested `while` Loops

A `while` loop inside another `while` loop.

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1
```

**Output:**
```text
i = 1, j = 1
i = 1, j = 2
i = 2, j = 1
i = 2, j = 2
i = 3, j = 1
i = 3, j = 2
```

---

## 8. Real-World Example: Sum Until User Quits

```python
total = 0

while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input == 'q':
        break

    total += int(user_input)

print("Total sum is:", total)
```

This pattern is extremely common in real applications.

---

## 9. Common Use Cases of `while` Loops

1. **Waiting for a condition**
   - User input
   - File availability
   - Network response

2. **Unknown number of iterations**
   - Reading data until EOF
   - Retrying until success

3. **Real-time monitoring**
   - Background services
   - Event listeners
   - Game loops

---

## Common Mistakes & Errors

| Mistake | Why It Happens |
|------|---------------|
| Infinite loop | Condition never changes |
| Forgetting increment | Counter not updated |
| Wrong exit condition | Loop never stops |
| Overusing `while` | `for` loop might be simpler |
| Nested infinite loops | Program becomes unresponsive |

---

## Comparison: `for` vs `while`

| Feature | `for` Loop | `while` Loop |
|------|-----------|-------------|
| Known iterations | Yes | No |
| Condition-based | No | Yes |
| Cleaner syntax | Yes | Depends |
| Risk of infinite loop | Low | High |

---

## Practice Tasks

1. Print numbers from 10 to 1 using a `while` loop.  
2. Ask the user to enter numbers until they enter `0`, then print the sum.  
3. Create a password checker with a maximum of 3 attempts.  
4. Print all even numbers between 1 and 50 using `while`.  
5. Use a nested `while` loop to print a multiplication table (1–5).  
