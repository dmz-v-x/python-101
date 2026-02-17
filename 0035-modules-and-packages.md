## Modules & Packages in Python

As Python programs grow larger, putting all code in a single file becomes:
- Hard to read
- Hard to maintain
- Hard to reuse

Python solves this using:
- **Modules** → single `.py` files
- **Packages** → collections of modules (folders)

Together, they help you write **clean, modular, reusable code**.

---

## Why Modules & Packages Exist

They help with:
- Code organization
- Reusability
- Maintainability
- Avoiding name conflicts
- Team collaboration

Think of them like:

```
📁 Project
 ├── 📄 auth.py        → module
 ├── 📄 utils.py       → module
 └── 📁 payments       → package
     ├── 📄 upi.py
     ├── 📄 cards.py
     └── 📄 netbanking.py
```

---

# 📄 Modules in Python

---

## 1. What is a Module?

A **module** is simply a **Python file** (`.py`) that contains:
- Variables
- Functions
- Classes
- Executable code

Example: `math_utils.py`

```python
def add(a, b):
    return a + b

PI = 3.14
```

---

## 2. Importing a Module

```python
import math_utils

print(math_utils.add(2, 3))
print(math_utils.PI)
```

---

## 3. Importing Specific Names

```python
from math_utils import add, PI

print(add(5, 6))
print(PI)
```

⚠️ Use carefully — names enter your namespace directly.

---

## 4. Import with Alias (`as`)

```python
import math_utils as mu

print(mu.add(10, 20))
```

Useful for:
- Long module names
- Avoiding name clashes

---

## 5. Import Everything (NOT Recommended)

```python
from math_utils import *
```

❌ Bad practice because:
- Pollutes namespace
- Hard to trace origins
- Can overwrite names silently

---

## 6. Built-in Modules

Python ships with many built-in modules.

Examples:
- `math`
- `sys`
- `os`
- `datetime`
- `random`

```python
import math

print(math.sqrt(16))
print(math.pi)
```

---

## 7. The `__name__ == "__main__"` Guard

When a file is:
- Run directly → `__name__ == "__main__"`
- Imported → `__name__` = module name

```python
def main():
    print("Running directly")

if __name__ == "__main__":
    main()
```

This prevents code from running unintentionally during imports.

---

# 📦 Packages in Python

---

## 8. What is a Package?

A **package** is a **directory** that contains:
- Multiple modules
- (Optionally) sub-packages

📁 Package structure:

```
📁 my_package
 ├── __init__.py
 ├── module1.py
 ├── module2.py
```

📌 `__init__.py` marks the folder as a package (required in older Python versions).

---

## 9. Importing from a Package

```python
from my_package import module1

module1.some_function()
```

---

## 10. Importing Specific Functions from a Package Module

```python
from my_package.module1 import some_function

some_function()
```

---

## 11. Nested Packages

```
📁 project
 └── 📁 services
     └── 📁 auth
         ├── __init__.py
         └── login.py
```

```python
from services.auth.login import authenticate
```

---

## 12. Absolute vs Relative Imports

---

### Absolute Import (Recommended)

```python
from services.auth.login import authenticate
```

✔ Clear  
✔ Explicit  
✔ Scalable  

---

### Relative Import (Inside Packages Only)

```python
from .login import authenticate
from ..utils import helper
```

⚠️ Only works inside packages  
❌ Cannot be used in top-level scripts

---

## 13. The `__init__.py` File

Controls what gets exposed when importing a package.

```python
# my_package/__init__.py
from .module1 import add
from .module2 import subtract
```

```python
from my_package import add
```

---

## 14. `__all__` in Modules & Packages

Controls wildcard imports.

```python
__all__ = ["add", "subtract"]
```

Used with:
```python
from module import *
```

---

## 15. How Python Finds Modules (Import System)

Python searches modules in this order:

1. Current directory
2. `PYTHONPATH`
3. Standard library
4. Site-packages

You can inspect it:

```python
import sys
print(sys.path)
```

---

## 16. Third-Party Packages (pip)

Install external packages using `pip`.

```bash
pip install requests
```

```python
import requests
response = requests.get("https://example.com")
```

Installed packages live in:
- `site-packages`

---

## 17. Virtual Environments (Important)

Virtual environments isolate dependencies.

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

Why use them?
- Avoid version conflicts
- Project-specific dependencies

---

## ⚠️ Common Import Mistakes

| Mistake | Why It Happens |
|------|---------------|
| `ModuleNotFoundError` | Wrong path |
| Circular imports | Modules importing each other |
| Shadowing modules | File named `math.py` |
| Using relative imports wrongly | Outside packages |
| Overusing `import *` | Namespace pollution |

---

## Best Practices

✅ Prefer absolute imports  
✅ One module = one responsibility  
✅ Use `__main__` guard  
✅ Avoid circular dependencies  
✅ Keep package structure clean  
❌ Don’t shadow standard library names  

---

## Summary

| Concept | Description |
|------|-------------|
| Module | Single `.py` file |
| Package | Folder of modules |
| Import | Load code from module |
| Alias | Rename imported module |
| Absolute import | Fully qualified path |
| Relative import | Package-internal only |
| `__init__.py` | Package initializer |

---

## Practice Tasks

1. Create a package with 3 modules and import functions across them.  
2. Demonstrate absolute vs relative imports.  
3. Break a circular import and fix it.  
4. Use `__name__ == "__main__"` correctly.  
5. Inspect `sys.path` and explain each entry.
