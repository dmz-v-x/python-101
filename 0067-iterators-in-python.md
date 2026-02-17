## Iterators in Python

An iterator is an object that:

✔ Produces values one at a time  
✔ Keeps track of iteration state  
✔ Implements special methods  

Core idea:

	Iterator = Stateful Value Producer

---

## Mental Model

Python iteration works like this:

	Iterable → Iterator → next() → Value

Very important distinction.

---

## Iterable vs Iterator

| Concept | Meaning |
|------------|--------------|
| Iterable | Object you can loop over |
| Iterator | Object that produces values |

Example:

	my_list = [1, 2, 3]

✔ List = Iterable  
❌ List ≠ Iterator  

---

## Creating an Iterator using `iter()`

	numbers = [1, 2, 3]

	iterator = iter(numbers)

	print(iterator)

**Output:**

	<list_iterator object at 0x...>

✔ Now we have an iterator.

---

## Retrieving Values using `next()`

	print(next(iterator))
	print(next(iterator))
	print(next(iterator))

**Output:**

	1
	2
	3

✔ Iterator advances each time.

---

## What Happens Internally?

	next(iterator) → iterator.__next__()

Python simply calls:

	__next__()

Behind the scenes.

---

## StopIteration Exception

	print(next(iterator))

ERROR:

	StopIteration

✔ Means no more values.

---

## Why Iterators Matter

✔ Memory efficient  
✔ Lazy evaluation  
✔ Used by loops  
✔ Used by generators  
✔ Used by files  
✔ Used by large datasets  

Core of Python efficiency.

---

## Iterator Protocol

Any iterator must implement:

✔ __iter__()  
✔ __next__()  

This is Python’s contract.

---

## Custom Iterator

Let’s build Python iteration manually.

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

✔ Manual iteration engine.

---

## Execution Flow Breakdown

	next(counter)
	→ Calls __next__()
	→ Returns value
	→ Saves state
	→ Advances pointer

Iterator remembers progress.

---

## Iterators vs Generators

| Feature | Iterator | Generator |
|------------|-------------|--------------|
| Implementation | Manual class | Function with yield |
| State Handling | Manual | Automatic |
| Complexity | Higher | Lower |
| Memory Efficient | Yes | Yes |

Generator = Shortcut Iterator

---

## Example — Generator as Iterator

	def generator():
	    yield 1
	    yield 2

✔ Generator automatically implements:

✔ __iter__()  
✔ __next__()  

---

## Where Iterators Are Used

✔ for loops  
✔ Generators  
✔ File objects  
✔ range()  
✔ map()  
✔ filter()  
✔ zip()  
✔ enumerate()  

Everywhere.

---

## Hidden Truth

`for` loop internally does:

	iterator = iter(iterable)

	while True:
	    try:
	        value = next(iterator)
	    except StopIteration:
	        break

Loop mechanics revealed.

---

## Deadly Gotchas

### Gotcha #1 — Iterable ≠ Iterator

	next([1, 2, 3])   # ERROR

✔ Must call iter() first.

---

### Gotcha #2 — Iterator Exhaustion

Once consumed → Gone forever.

---

### Gotcha #3 — No Random Access

Iterator ≠ Indexable.

---

### Gotcha #4 — Multiple Iterators Independent

Each iterator maintains its own state.

---

### Gotcha #5 — Infinite Iterators

Possible → Must control carefully.

---

### Gotcha #6 — Forgetting StopIteration

Custom iterator must raise StopIteration.

---

## Deep Insight

Iterators enable:

✔ Lazy evaluation  
✔ Streaming systems  
✔ Infinite sequences  
✔ Memory-safe iteration  
✔ Pipeline processing  
✔ Core Python internals  

Fundamental concept.

---

## When To Use Custom Iterators

✔ Complex iteration logic  
✔ Controlled state machines  
✔ Infinite sequences  
✔ Lazy pipelines  

Rare for simple tasks.

---

## Best Practices

✔ Prefer generators (simpler)  
✔ Use iter() properly  
✔ Handle exhaustion safely  
✔ Raise StopIteration correctly  
✔ Avoid unnecessary manual iterators  

---

## Summary

✔ Iterator = Stateful value producer  
✔ Created via iter()  
✔ Consumed via next()  
✔ Implements iterator protocol  
✔ StopIteration signals end  
✔ Core of Python loops  
✔ Generators = Iterator shortcut  

---

## Practice Tasks

1. Convert list to iterator  
2. Use next() manually  
3. Trigger StopIteration  
4. Use default fallback  
5. Build custom iterator  
6. Implement iterator protocol  
7. Create infinite iterator  
8. Compare generator vs iterator  
