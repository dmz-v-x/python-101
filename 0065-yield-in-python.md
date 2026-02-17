## Yield in python

`yield` is a special keyword used inside functions.

Instead of:

	return → Ends function

We use:

	yield → Pauses function

	yield = Pause + Save State + Resume Later

---

## Mental Model

**Normal function:**

✔ Runs completely  
✔ Returns value  
✔ Execution ends  

**Generator function:**

✔ Runs until `yield`  
✔ Pauses execution  
✔ Remembers state  
✔ Resumes later  

---

## Basic Example

	def simple_generator():
	    yield 1
	    yield 2
	    yield 3

	gen = simple_generator()
	print(gen)

**Output:**

	<generator object simple_generator at 0x...>

✔ Function is not executed yet.

---

## Execution Flow with `yield`

	print(next(gen))

**Output:**

	1

✔ Function starts  
✔ Stops at first `yield`

---

	print(next(gen))

**Output:**

	2

✔ Execution resumes from previous pause point.

---

## What Does `yield` Actually Do?

When Python sees:

	yield value

It:

✔ Produces a value  
✔ Pauses execution  
✔ Saves variables  
✔ Saves instruction pointer  
✔ Waits for `next()`

---

## Visual Execution Breakdown

	def demo():
	    print("Start")
	    yield 1
	    print("Middle")
	    yield 2
	    print("End")

	gen = demo()

	next(gen)
	next(gen)
	next(gen)

**Output:**

	Start
	Middle
	End

---

## `yield` vs `return`

| Feature | return | yield |
|----------|------------|------------|
| Ends Function | Yes | No |
| Pauses Function | No | Yes |
| Saves State | No | Yes |
| Multiple Values | No | Yes |

---

## Yield Inside Loops

	def count_up_to(n):

	    i = 1
	    while i <= n:
	        yield i
	        i += 1

✔ Produces values lazily.

---

## Yielding Computed Values

	def squares(n):
	    for i in range(n):
	        yield i * i

	for num in squares(5):
	    print(num)

**Output:**

	0
	1
	4
	9
	16

---

## Yield & Memory Efficiency

**List version (memory heavy):**

	[x*x for x in range(1000000)]

✔ Stores everything in memory.

---

**Yield version (memory efficient):**

	def squares():
	    for x in range(1000000):
	        yield x * x

✔ Produces values one at a time.

---

## Yielding Infinite Values

	def infinite():

	    i = 1
	    while True:
	        yield i
	        i += 1

✔ Can run forever.

---

## `yield from`

Delegates iteration to another generator.

	def gen1():
	    yield 1
	    yield 2

	def gen2():
	    yield from gen1()
	    yield 3

**Output:**

	1
	2
	3

✔ Clean generator chaining.

---

## Deadly Gotchas

### Gotcha #1 — Function Becomes Generator

Even one `yield` changes behavior.

	def func():
	    yield 1

✔ Function now returns a generator.

---

### Gotcha #2 — `return` Ends Generator

	return value

✔ Immediately stops generator.

---

### Gotcha #3 — Generator Exhaustion

Generators run only once.

	gen = squares(3)

	for x in gen:
	    print(x)

	for x in gen:
	    print(x)

✔ Second loop prints nothing.

---

### Gotcha #4 — No Random Access

	gen[0] → Error

✔ Generators are not indexable.

---

### Gotcha #5 — Debugging Confusion

Execution flow is non-linear.

✔ Can confuse beginners.

---

## Deep Insight

`yield` enables:

✔ Lazy evaluation  
✔ Streaming systems  
✔ Pipelines  
✔ Infinite sequences  
✔ Memory-safe iteration  
✔ Advanced coroutine patterns  

Core of Python efficiency.

---

## When To Use `yield`

✔ Large datasets  
✔ File processing  
✔ Infinite sequences  
✔ Streaming data  
✔ Pipelines  
✔ Performance-critical applications  

Avoid for tiny collections.

---

## Best Practices

✔ Keep generator logic simple  
✔ Avoid unnecessary conversions  
✔ Remember generator exhaustion  
✔ Use `yield` for lazy computation  

---

## Summary

✔ `yield` pauses execution  
✔ Saves function state  
✔ Resumes later  
✔ Enables generators  
✔ Memory efficient  
✔ Supports infinite sequences  
✔ `yield from` for delegation  

---

## Practice Tasks

1. Create a simple generator  
2. Use `next()` manually  
3. Add print statements and observe flow  
4. Use `yield` inside loops  
5. Create an infinite generator  
6. Demonstrate generator exhaustion  
7. Use `yield from`  
8. Build a lazy computation generator  
