## Interfaces in Python

Unlike languages like **Java / C#**, Python does **NOT** have a dedicated `interface` keyword.

👉 Instead, Python achieves interface-like behavior using:

```text
1. Abstract Base Classes (ABC)
2. Protocols (Structural Subtyping)
```

Python philosophy:

```text
"We care about behavior, not rigid types"
```

---

## Mental Model

An **interface** defines:

What an object MUST do  
NOT how it does it  

Think of it as a **contract / blueprint** 

---

## Why Interfaces Matter

---

Interfaces help with:

✔ Loose coupling  
✔ Scalable architecture  
✔ Plug-in systems  
✔ Clean API design  
✔ Enforcing consistency  
✔ Dependency inversion  

---

## Interface vs Abstract Class

---

| Concept | Purpose |
|----------|------------|
| Interface | Defines ONLY behavior |
| Abstract Class | Can define behavior + shared logic |

👉 Python blurs the line slightly.

---

## Method 1 — Using Abstract Base Classes (ABC)

---

Python’s traditional way to simulate interfaces.

---

## Basic Interface Example

---

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Cannot instantiate:

```python
p = PaymentProcessor()  # ERROR 
```

---

## Implementation

---

```python
class CreditCardProcessor(PaymentProcessor):

    def pay(self, amount):
        return f"Paid {amount} using Credit Card"
```

```python
processor = CreditCardProcessor()
print(processor.pay(100))
```

**Output:**

```text
Paid 100 using Credit Card
```

---

## Key Insight

ABC behaves like:

```text
Interface + Partial Implementation Capability
```

✔ Can contain logic  
✔ Can contain attributes  
✔ Can enforce methods  

---

## Method 2 — Protocols (Modern Python Interfaces)

---

Introduced via:

```python
from typing import Protocol
```

Major difference:

```text
Structural Typing ("Duck Typing with Rules")
```

---

## Structural vs Nominal Typing

---

| Typing Style | Meaning |
|---------------|------------|
| Nominal Typing | Must explicitly inherit |
| Structural Typing | Must match structure |

👉 Python Protocols = Structural Typing

---

## Protocol Example

---

```python
from typing import Protocol

class PaymentProcessor(Protocol):

    def pay(self, amount: float) -> str:
        ...
```

Now ANY class with `pay()` works 

---

## Implementation WITHOUT Inheritance 

---

```python
class UPIProcessor:

    def pay(self, amount: float) -> str:
        return f"Paid {amount} via UPI"
```

✔ No inheritance  
✔ Still valid interface match

---

## Usage

---

```python
def process_payment(processor: PaymentProcessor):
    print(processor.pay(500))
```

```python
upi = UPIProcessor()
process_payment(upi)
```

**Output:**

```text
Paid 500 via UPI
```

---

## What Just Happened? 

Protocol checks:

```text
Does object behave correctly?
NOT
Did object inherit correctly?
```

Pure Pythonic design

---

## Deadly Gotchas

---

## Gotcha #1 — ABC Requires Explicit Inheritance

---

```text
If you forget inheritance → No enforcement
```

---

## Gotcha #2 — Protocols Do NOT Enforce at Runtime

Protocols are mainly for:

✔ Type checking tools (mypy / Pyright)  
✔ Static analysis  

Python itself won’t stop bad objects.

---

## Gotcha #3 — Protocols ≠ Validation 

Matching method names ≠ Correct logic.

---

## Gotcha #4 — ABC vs Protocol Confusion 

---

| Feature | ABC | Protocol |
|------------|---------|-------------|
| Requires Inheritance | ✅ Yes | ❌ No |
| Runtime Enforcement | ✅ Yes | ❌ No |
| Structural Typing | ❌ No | ✅ Yes |
| Pythonic Flexibility | Medium | Maximum 🔥 |

---

## When To Use ABC vs Protocol

---

## Use ABC When:

✔ You want strict enforcement  
✔ Shared base logic needed  
✔ Runtime safety required  
✔ Framework design  

---

## Use Protocol When:

✔ Flexibility needed  
✔ Duck typing design  
✔ Static typing benefits  
✔ Plug-in architecture  
✔ Large decoupled systems  

---

## Real-World Example 

---

Imagine:

```text
Logging System
```

Any class with:

```python
log(message)
```

Should work.

Protocols shine here 

---

## Deep Design Insight

Python prefers:

```text
Behavioral Contracts
Over
Rigid Hierarchies
```

Interfaces in Python are:

✔ Lightweight  
✔ Flexible  
✔ Powerful  

---

## Best Practices 

---

✔ Keep interfaces minimal  
✔ Define behaviors only  
✔ Avoid unnecessary abstraction  
✔ Prefer Protocols for flexibility  
✔ Use ABC for strict frameworks  
✔ Don't over-engineer  

---

## Summary

✔ Python has no `interface` keyword  
✔ ABC simulates classical interfaces  
✔ Protocols enable structural typing  
✔ ABC = Strict / Runtime Enforcement  
✔ Protocol = Flexible / Static Typing  
✔ Interfaces = Contracts  
✔ Key for scalable design  

---

## Practice Tasks

1. Create interface using ABC  
2. Try instantiating ABC (observe error)  
3. Implement subclass  
4. Add shared logic in ABC  
5. Create Protocol interface  
6. Implement class WITHOUT inheritance  
7. Use Protocol in function typing  
8. Compare ABC vs Protocol behavior  
