## Generators in Python

A **generator** is a special type of function that:

✔ Produces values **one at a time**  
✔ Does **NOT store everything in memory**  
✔ Uses the `yield` keyword  

```text
Generators = Lazy Iteration
```

---

## Mental Model

Normal function:

```python
return → Ends function
```

Generator function:

```python
yield → Pauses function
```

✔ Remembers state  
✔ Resumes later

---

## Why Generators Matter

---

✔ Memory efficient  
✔ Faster for large data  
✔ Lazy evaluation  
✔ Infinite sequences  
✔ Streaming data  
✔ Used heavily in real systems  

---

## Normal Function vs Generator

---

## Normal Function

```python
def get_numbers():
    return [1, 2, 3]
```

✔ Creates FULL list in memory

---

## Generator Function

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
```

✔ Produces values one-by-one

---

## Using a Generator

---

```python
gen = get_numbers()

print(gen)
```

**Output:**

```text
<generator object get_numbers at 0x...>
```

✔ It’s NOT executed yet 

---

## Consuming Generator Values

---

```python
print(next(gen))
print(next(gen))
print(next(gen))
```

**Output:**

```text
1
2
3
```

✔ Each `next()` resumes execution.

---

## What Happened Internally?

---

```text
yield → Pause → Save State → Resume
```

Python keeps:

✔ Local variables  
✔ Execution position  
✔ Internal context  

---

## Generator with Loop

---

```python
def count_up_to(n):

    i = 1
    while i <= n:
        yield i
        i += 1
```

---

```python
gen = count_up_to(3)

for num in gen:
    print(num)
```

**Output:**

```text
1
2
3
```

✔ Clean & elegant.

---

## Generator vs List (Memory Insight) 

---

## List Version

```python
numbers = [x for x in range(1000000)]
```

✔ Stores EVERYTHING

---

## Generator Version

```python
numbers = (x for x in range(1000000))
```

✔ Produces on demand

---

## Generator Expression

---

```python
gen = (x * 2 for x in range(5))

for num in gen:
    print(num)
```

**Output:**

```text
0
2
4
6
8
```

✔ Like list comprehension but lazy.

---

## Real-World Example

---

Reading HUGE file 

```python
def read_large_file():

    with open("huge.txt") as f:
        for line in f:
            yield line
```

✔ Processes line-by-line  
✔ No memory explosion

---

## Infinite Generator

---

```python
def infinite_counter():

    i = 1
    while True:
        yield i
        i += 1
```

✔ Runs forever ⚠️

---

## Deadly Gotchas

---

## Gotcha #1 — Generator Exhaustion 

---

```python
gen = get_numbers()

list(gen)
list(gen)   # EMPTY 
```

✔ Generators run ONLY once.

---

## Gotcha #2 — Cannot Index Generators 

---

```python
gen[0]   # ERROR 
```

✔ No random access.

---

## Gotcha #3 — Forgetting Lazy Nature

Generator does NOTHING until:

✔ `next()`  
✔ Loop  
✔ `list()`  

---

## Gotcha #4 — yield vs return

---

```python
return → Ends
yield → Pauses
```

Big difference

---

## Gotcha #5 — Debugging Confusion

Generators hide flow.

✔ Harder to trace logic.

---

## Deep Insight

Generators enable:

✔ Lazy pipelines  
✔ Streaming systems  
✔ Data processing chains  
✔ Memory-safe iteration  
✔ Functional composition  

---

## yield vs yield from 

---

## ✅ yield from Example

```python
def generator1():
    yield 1
    yield 2

def generator2():
    yield from generator1()
    yield 3
```

---

```python
for x in generator2():
    print(x)
```

**Output:**

```text
1
2
3
```

✔ Delegates iteration

---

## When To Use Generators

---

Large datasets  
File processing  
Infinite sequences  
Streaming APIs  
Pipelines  
Memory-critical apps  

Tiny lists.

---

## Best Practices

---

✔ Use for large data  
✔ Avoid unnecessary conversion  
✔ Remember exhaustion  
✔ Keep logic simple  
✔ Prefer generator expressions  

---

## Summary

✔ Generators = Lazy evaluation 
✔ Use `yield` keyword  
✔ Memory efficient  
✔ State preserved between yields  
✔ Can create infinite sequences  
✔ Generator expressions available  
✔ Exhaustible  

---

## Practice Tasks

1. Create simple generator  
2. Use next() manually  
3. Build generator with loop  
4. Create generator expression  
5. Create infinite generator  
6. Demonstrate exhaustion  
7. Use yield from  
8. Simulate file reader 
