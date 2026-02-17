## Magic Methods in Python

Magic methods (also called dunder methods) are special methods in Python.

They follow this naming pattern:

	Double underscores → __method__

Examples:

	__init__
	__str__
	__repr__
	__add__
	__len__

These methods define how objects behave.

---

## Mental Model

Magic methods are Python’s hidden hooks into object behavior.

When you write:

	obj + other

Python internally calls:

	obj.__add__(other)

Operators and built-ins are powered by magic methods.

---

## Why Magic Methods Matter

✔ Customize object behavior  
✔ Operator overloading  
✔ Clean syntax  
✔ Pythonic APIs  
✔ Built-in type simulation  
✔ Deep language integration  

Core of Python OOP.

---

## Key Truth

Everything in Python works via magic methods.

	Operators → Magic Methods
	Functions → Magic Methods
	Built-ins → Magic Methods

---

## Object Initialization — `__init__`

	class Person:

	    def __init__(self, name):
	        self.name = name

✔ Called when object is created.

	p = Person("Alice")

Internally:

	Person.__init__(p, "Alice")

---

## String Representation — `__str__`

Controls:

	print(object)

Example:

	class Person:

	    def __init__(self, name):
	        self.name = name

	    def __str__(self):
	        return f"Person: {self.name}"

	p = Person("Alice")
	print(p)

**Output:**

	Person: Alice

---

## Developer Representation — `__repr__`

Used for debugging.

	repr(object)

Example:

	def __repr__(self):
	    return f"Person('{self.name}')"

✔ Should be unambiguous.

---

## Arithmetic Operators

| Operator | Magic Method |
|-------------|----------------|
| + | __add__ |
| - | __sub__ |
| * | __mul__ |
| / | __truediv__ |

Example:

	class Number:

	    def __init__(self, value):
	        self.value = value

	    def __add__(self, other):
	        return Number(self.value + other.value)

	n1 = Number(10)
	n2 = Number(20)

	print((n1 + n2).value)

**Output:**

	30

---

## Comparison Operators

| Operator | Magic Method |
|-------------|----------------|
| == | __eq__ |
| < | __lt__ |
| > | __gt__ |

Example:

	def __eq__(self, other):
	    return self.value == other.value

✔ Enables object comparisons.

---

## Length Behavior — `__len__`

Controls:

	len(object)

Example:

	class Collection:

	    def __init__(self, items):
	        self.items = items

	    def __len__(self):
	        return len(self.items)

	c = Collection([1, 2, 3])
	print(len(c))

**Output:**

	3

---

## Container Behavior

| Behavior | Magic Method |
|-------------|----------------|
| Indexing | __getitem__ |
| Assignment | __setitem__ |
| Membership | __contains__ |

Example:

	def __getitem__(self, index):
	    return self.items[index]

✔ Enables:

	obj[0]

---

## Callable Objects — `__call__`

Allows objects to behave like functions.

Example:

	class Greeter:

	    def __call__(self):
	        print("Hello!")

	g = Greeter()
	g()

**Output:**

	Hello!

---

## Context Managers

| Method | Purpose |
|-------------|------------|
| __enter__ | Setup |
| __exit__ | Cleanup |

Example:

	class FileManager:

	    def __enter__(self):
	        print("Opening resource")
	        return self

	    def __exit__(self, exc_type, exc_value, traceback):
	        print("Closing resource")

	with FileManager():
	    print("Using resource")

**Output:**

	Opening resource
	Using resource
	Closing resource

---

## Deadly Gotchas

### Gotcha #1 — Magic Methods Not Called Directly

Avoid:

	obj.__add__(other)

✔ Use operators instead.

---

### Gotcha #2 — Returning Wrong Type

	return self.value + other.value   # Bad

✔ Usually return an object.

---

### Gotcha #3 — Missing Type Safety

Always validate `other`.

	if not isinstance(other, ClassName):
	    return NotImplemented

---

### Gotcha #4 — `__str__` vs `__repr__`

| Method | Purpose |
|------------|------------|
| __str__ | User-friendly |
| __repr__ | Developer/debug |

---

### Gotcha #5 — Infinite Recursion

Incorrect calls inside magic methods can cause crashes.

---

### Gotcha #6 — NotImplemented Usage

Returning `NotImplemented` allows Python fallback logic.

---

## Deep Insight

Magic methods define:

✔ Object identity  
✔ Operator behavior  
✔ Container behavior  
✔ Callable behavior  
✔ Debugging display  
✔ Context management  

They form Python’s object protocol engine.

---

## Best Practices

✔ Keep behavior intuitive  
✔ Return correct types  
✔ Use type checks  
✔ Use NotImplemented properly  
✔ Implement __repr__ for debugging  
✔ Avoid overengineering  

---

## Summary

✔ Magic methods = Dunder methods  
✔ Control object behavior  
✔ Operators call magic methods  
✔ Built-ins rely on magic methods  
✔ Enable Pythonic APIs  
✔ Extremely powerful  

---

## Practice Tasks

1. Implement __str__  
2. Implement __repr__  
3. Overload + operator  
4. Overload comparison operator  
5. Implement __len__  
6. Implement __getitem__  
7. Implement callable object (__call__)  
8. Build context manager  
