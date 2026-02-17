## Modify in Place in Python

**Modify in place** means changing the **contents of an existing object** **without creating a new object**.

- The object’s **identity (`id`) stays the same**
- Only the **internal state** changes

This behavior is possible **only for mutable objects**.

---

## Core Rule (Very Important)

> **Mutable objects** → can be modified in place  
> **Immutable objects** → cannot be modified in place (new object is created)

---

## Mutable vs Immutable (Quick Recap)

| Category | Examples | Modify In Place? |
|------|--------|------------------|
| Mutable | `list`, `dict`, `set` | ✅ Yes |
| Immutable | `int`, `str`, `tuple`, `float` | ❌ No |

---

## Why Modify In Place Matters

Understanding in-place modification helps you:
- Avoid unexpected side effects
- Write memory-efficient code
- Debug reference-sharing bugs
- Understand `+=`, `.append()`, `.sort()`, etc.

---

## 1. Modifying a List In Place

```python
my_list = [1, 2, 3]
print("Before:", my_list, id(my_list))

my_list.append(4)

print("After:", my_list, id(my_list))
```

**Output:**
```text
Before: [1, 2, 3] 139692510168832
After:  [1, 2, 3, 4] 139692510168832
```

✅ Same memory address  
✅ List modified in place  

---

## 2. In-Place Modification Using List Slicing

```python
my_list = [1, 2, 3, 4]
print("Before:", my_list, id(my_list))

my_list[1:3] = [20, 30]

print("After:", my_list, id(my_list))
```

**Output:**
```text
Before: [1, 2, 3, 4] 139692510170944
After:  [1, 20, 30, 4] 139692510170944
```

Slicing assignment modifies the list **in place**

---

## 3. Modifying a Dictionary In Place

```python
my_dict = {'a': 1, 'b': 2}
print("Before:", my_dict, id(my_dict))

my_dict['c'] = 3

print("After:", my_dict, id(my_dict))
```

**Output:**
```text
Before: {'a': 1, 'b': 2} 139692510188000
After:  {'a': 1, 'b': 2, 'c': 3} 139692510188000
```

✅ Same object  
✅ New key added in place  

---

## 4. `+=` on Lists vs Tuples (CRITICAL DIFFERENCE)

---

### `+=` with Lists (In Place)

```python
my_list = [1, 2, 3]
print("Before:", my_list, id(my_list))

my_list += [4, 5]

print("After:", my_list, id(my_list))
```

**Output:**
```text
Before: [1, 2, 3] 139692510174592
After:  [1, 2, 3, 4, 5] 139692510174592
```

✅ List modified in place

---

### `+=` with Tuples (NOT In Place)

```python
my_tuple = (1, 2, 3)
print("Before:", my_tuple, id(my_tuple))

my_tuple += (4, 5)

print("After:", my_tuple, id(my_tuple))
```

**Output:**
```text
Before: (1, 2, 3) 139692510155424
After:  (1, 2, 3, 4, 5) 139692510189056
```

❌ New tuple created  
❌ Memory address changes  

---

## 5. In-Place Modification of Nested Lists

```python
nested_list = [[1, 2, 3], [4, 5, 6]]
print("Before:", nested_list, id(nested_list))

nested_list[0].append(100)

print("After:", nested_list, id(nested_list))
```

**Output:**
```text
Before: [[1, 2, 3], [4, 5, 6]] 139692510190720
After:  [[1, 2, 3, 100], [4, 5, 6]] 139692510190720
```

Outer list unchanged  
Inner list modified in place  

---

## 6. `sort()` vs `sorted()` (In Place vs New Object)

```python
my_list = [3, 1, 2]
print("Before:", my_list, id(my_list))

my_list.sort()

print("After sort():", my_list, id(my_list))
```

**Output:**
```text
Before: [3, 1, 2] 139692510191040
After sort(): [1, 2, 3] 139692510191040
```

---

### `sorted()` Creates a New List

```python
sorted_list = sorted([3, 1, 2])
print("New sorted list:", sorted_list)
```

**Output:**
```text
[1, 2, 3]
```

---

## 7. In-Place Modification Using Loops

```python
my_list = [1, 2, 3, 4, 5]
print("Before:", my_list, id(my_list))

for i in range(len(my_list)):
    my_list[i] *= 2

print("After:", my_list, id(my_list))
```

**Output:**
```text
Before: [1, 2, 3, 4, 5] 139692510193056
After:  [2, 4, 6, 8, 10] 139692510193056
```

---

## 8. In-Place Modification with Sets

```python
my_set = {1, 2, 3}
print("Before:", my_set, id(my_set))

my_set.add(4)

print("After:", my_set, id(my_set))
```

**Output:**
```text
Before: {1, 2, 3} 139692510194368
After:  {1, 2, 3, 4} 139692510194368
```

---

## Common Pitfalls

| Pitfall | Why It Happens |
|------|---------------|
| Unexpected data changes | Shared references |
| Assuming `+=` always mutates | Depends on mutability |
| Modifying arguments in functions | Passed by reference |
| Confusing `sort()` and `sorted()` | One mutates, one doesn’t |
| Forgetting nested mutability | Inner objects may change |

---

## Best Practices

✅ Know which methods modify in place  
✅ Be cautious with shared references  
✅ Prefer immutability when possible  
✅ Use `sorted()` when original data must stay unchanged  
❌ Don’t assume memory behavior blindly  

---

## Summary

| Concept | Key Idea |
|------|--------|
| Modify in place | Same object, same `id` |
| Mutable types | Support in-place changes |
| Immutable types | Create new objects |
| `+=` | In place for mutable only |
| `sort()` | In place |
| `sorted()` | Returns new object |

---

## Practice Tasks

1. Show how modifying a list inside a function affects the caller.  
2. Demonstrate why `+=` behaves differently for lists and tuples.  
3. Convert an in-place algorithm to a non-mutating version.  
4. Identify which methods mutate objects in a given codebase.  
5. Debug a bug caused by unintended in-place modification.
