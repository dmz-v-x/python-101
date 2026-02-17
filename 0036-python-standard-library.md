## Python Standard Library

The **Python Standard Library** is a **collection of built-in modules and packages** that come **pre-installed with Python**.

👉 You **do NOT need to install anything** to use it.  
👉 It provides ready-made solutions for common programming tasks.

Python follows the philosophy:

> **“Batteries Included”**

Meaning:  
Python already gives you tools for most real-world problems.

---

## Why the Standard Library Exists

The standard library helps you:

- Avoid reinventing the wheel
- Write less code
- Build reliable applications
- Follow best practices
- Work efficiently without third-party packages

---

## What Can You Do with the Standard Library?

You can handle:

- Files & directories
- Dates & time
- Math & statistics
- OS interaction
- Networking & internet
- Data formats (JSON, CSV)
- Compression
- Multithreading & multiprocessing
- Debugging & testing
- Security & encryption

All **without installing anything**.

---

## High-Level Categories of the Standard Library

Below are the **most important categories**, explained one by one.

---

## 1. Math & Numbers

Modules for mathematical operations.

### Common Modules
- `math`
- `random`
- `statistics`
- `decimal`
- `fractions`

### Example

```python
import math

print(math.sqrt(16))
print(math.pi)
```

---

## 2. Date & Time

Used for working with dates, times, and timestamps.

### Common Modules
- `datetime`
- `time`
- `calendar`

### Example

```python
from datetime import datetime

now = datetime.now()
print(now)
```

---

## 3. File & Directory Handling

Used to work with files and folders.

### Common Modules
- `os`
- `pathlib`
- `shutil`
- `glob`

### Example

```python
import os

print(os.getcwd())
```

---

## 4. Data Formats & Serialization

Used for reading/writing structured data.

### Common Modules
- `json`
- `csv`
- `pickle`
- `configparser`

### Example

```python
import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)
```

---

## 5. Networking & Internet

Used to interact with the web and networks.

### Common Modules
- `urllib`
- `http`
- `socket`
- `email`

### Example

```python
from urllib.request import urlopen

response = urlopen("https://example.com")
print(response.status)
```

---

## 6. Concurrency & Parallelism

Used to run tasks concurrently.

### Common Modules
- `threading`
- `multiprocessing`
- `concurrent.futures`
- `asyncio`

### Example

```python
import threading

def task():
    print("Task running")

t = threading.Thread(target=task)
t.start()
```

---

## 7. Testing & Debugging

Used to test and debug Python code.

### Common Modules
- `unittest`
- `doctest`
- `logging`
- `traceback`
- `pdb`

### Example

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is a log message")
```

---

## 8. Security & Cryptography

Used for hashing and secure data handling.

### Common Modules
- `hashlib`
- `secrets`
- `hmac`
- `ssl`

### Example

```python
import hashlib

hash_value = hashlib.sha256(b"password").hexdigest()
print(hash_value)
```

---

## 9. System & Interpreter Interaction

Used to interact with Python runtime and system.

### Common Modules
- `sys`
- `argparse`
- `platform`
- `subprocess`

### Example

```python
import sys

print(sys.version)
```

---

## 10. Functional Programming Utilities

Tools inspired by functional programming.

### Common Modules
- `functools`
- `itertools`
- `operator`

### Example

```python
import itertools

for item in itertools.count(5, 2):
    print(item)
    if item > 10:
        break
```

---

## 11. Data Structures

Specialized data containers.

### Common Modules
- `collections`
- `heapq`
- `array`
- `bisect`

### Example

```python
from collections import Counter

counts = Counter("banana")
print(counts)
```

---

## 12. Development & Packaging Tools

Used to build and distribute Python projects.

### Common Modules
- `venv`
- `distutils`
- `importlib`
- `pkgutil`

---

##  How to Explore the Standard Library Yourself

### Use `help()`

```python
help(os)
```

### Official Documentation
👉 https://docs.python.org/3/library/

---

## Common Mistakes

| Mistake | Why It’s Wrong |
|------|---------------|
| Rewriting built-in functionality | Library already exists |
| Not reading docs | Miss powerful features |
| Using third-party libs unnecessarily | Stdlib is enough |
| Shadowing module names | Causes import errors |

---

## Best Practices

✅ Prefer standard library first  
✅ Learn commonly used modules deeply  
✅ Combine modules effectively  
✅ Read official documentation  
❌ Don’t install libraries blindly  

---

## Summary

| Concept | Meaning |
|------|--------|
| Standard Library | Built-in Python modules |
| Batteries Included | Ready-to-use tools |
| No installation | Comes with Python |
| Reliable | Well-tested |
| Essential | Used in all real projects |

---

## Practice Tasks

1. Write a script using `os` and `pathlib` together.  
2. Serialize and deserialize data using `json`.  
3. Hash a password using `hashlib`.  
4. Create logs using `logging`.  
5. Explore `itertools` and explain one function.
