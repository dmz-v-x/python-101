## next() in Python

`next()` is a built-in Python function used to:

✔ Retrieve the next item from an iterator  
✔ Manually control iteration  
✔ Work directly with generators & iterables  

Basic idea:

	next(iterator)

---

## Mental Model

Python iteration works like this:

	Iterable → Iterator → next() → Value

Key insight:

	for loop internally uses next()

---

## Basic Example

	numbers = [1, 2, 3]

	iterator = iter(numbers)

	print(next(iterator))
	print(next(iterator))
	print(next(iterator))

**Output:**

	1
	2
	3

✔ Each call moves forward.

---

## What Happened Internally?

	next(iterator) → iterator.__next__()

Yes.

`next()` simply calls:

	__next__()

Behind the scenes.

---

## StopIteration Exception

	print(next(iterator))   # After last value

ERROR:

	StopIteration

✔ Means no more values.

---

## Safer Version — Default Value

	next(iterator, default_value)

Example:

	numbers = [1, 2]

	iterator = iter(numbers)

	print(next(iterator))
	print(next(iterator))
	print(next(iterator, "No more items"))

**Output:**

	1
	2
	No more items

✔ Prevents crash.

---

## next() with Strings

	text = "ABC"

	iterator = iter(text)

	print(next(iterator))
	print(next(iterator))
	print(next(iterator))

**Output:**

	A
	B
	C

✔ Strings are iterable.

---

## next() with Generators

	def generator():
	    yield 10
	    yield 20

	gen = generator()

	print(next(gen))
	print(next(gen))

**Output:**

	10
	20

✔ next() resumes generator execution.

---

## next() vs for Loop

### for Loop (Automatic)

	for num in [1, 2, 3]:
	    print(num)

---

### next() (Manual Control)

	iterator = iter([1, 2, 3])

	print(next(iterator))
	print(next(iterator))

✔ Useful for fine-grained control.

---

## Custom Iterator

You can define your own iteration logic.

Example:

	class Counter:

	    def __init__(self, max):
	        self.max = max
	        self.current = 0

	    def __iter__(self):
	        return self

	    def __next__(self):

	        if self.current >= self.max:
	            raise StopIteration

	        self.current += 1
	        return self.current

	counter = Counter(3)

	print(next(counter))
	print(next(counter))
	print(next(counter))

**Output:**

	1
	2
	3

✔ Manual iteration design.

---

## Iterator Protocol

Any iterator must implement:

✔ __iter__()  
✔ __next__()  

Python relies on this contract.

---

## Deadly Gotchas

### Gotcha #1 — next() Requires Iterator

	next([1, 2, 3])   # ERROR

✔ Because list is not an iterator.

Correct usage:

	next(iter([1, 2, 3]))

---

### Gotcha #2 — StopIteration Crashes

Always handle exhaustion safely.

---

### Gotcha #3 — next() Consumes Values

Once consumed → Gone.

---

### Gotcha #4 — Multiple Iterators Are Independent

	iterable = [1, 2, 3]

	it1 = iter(iterable)
	it2 = iter(iterable)

✔ Separate state.

---

### Gotcha #5 — Iterator vs Indexing

Iterator ≠ Random access.

---

## Deep Insight

`next()` enables:

✔ Manual iteration control  
✔ Lazy evaluation mechanics  
✔ Generator execution stepping  
✔ Custom iteration design  
✔ Streaming logic  

Core of Python’s iteration engine.

---

## When To Use next()

✔ Manual iteration control  
✔ Working with generators  
✔ Custom iterators  
✔ Streaming pipelines  
✔ Look-ahead logic  

Rare in simple loops.

---

## Best Practices

✔ Use default value when unsure  
✔ Handle StopIteration safely  
✔ Prefer loops unless control needed  
✔ Avoid unnecessary manual iteration  

---

## Summary

✔ next() retrieves next value  
✔ Works on iterators only  
✔ Calls __next__() internally  
✔ StopIteration signals end  
✔ Supports default fallback  
✔ Critical for generators  
✔ Core of iteration protocol  

---

## Practice Tasks

1. Use next() with list iterator  
2. Trigger StopIteration  
3. Use default fallback  
4. Use next() with string  
5. Use next() with generator  
6. Build custom iterator  
7. Implement iterator protocol  
8. Compare loop vs next()  
