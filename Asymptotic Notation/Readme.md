# Asymptotic Notation

**Asymptotic Notation** is a mathematical tool used to describe the behavior of algorithms as the input size grows. It provides a way to compare the efficiency of algorithms in terms of time or space complexity, focusing on the growth trend rather than precise measurements.

---

## Why Use Asymptotic Notation?

1. To **analyze algorithm performance** independently of hardware or programming language.
2. To understand how the running time or memory usage grows as the input size increases.

---

## Types of Asymptotic Notation

### 1. Big-O Notation (\(O\))

- Describes the **upper bound** of an algorithm's growth rate.
- Indicates the **worst-case performance**.
- Example: If an algorithm's complexity is \(O(n^2)\), its running time will grow at most quadratically with the input size \(n\).

**Formal Definition:**
`f(n) ∈ O(g(n))` if there exist constants `c > 0` and `n₀ > 0` such that:
`f(n) ≤ c * g(n) for all n ≥ n₀`

---

### 2. Omega Notation (\(\Omega\))

- Describes the **lower bound** of an algorithm's growth rate.
- Indicates the **best-case performance**.
- Example: If an algorithm's complexity is \(\Omega(n)\), its running time will grow at least linearly with \(n\).

**Formal Definition:**
`f(n) ∈ Ω(g(n))` if there exist constants `c > 0` and `n₀ > 0` such that:
`f(n) ≥ c * g(n) for all n ≥ n₀`

---

### 3. Theta Notation (\(\Theta\))

- Describes the **tight bound** of an algorithm's growth rate.
- Indicates both the **upper and lower bounds**.
- Example: If an algorithm's complexity is \(\Theta(n^2)\), its running time grows exactly quadratically with \(n\).

**Formal Definition:**
`f(n) ∈ Θ(g(n))` if there exist constants `c₁ > 0`, `c₂ > 0`, and `n₀ > 0` such that:
`c₁ * g(n) ≤ f(n) ≤ c₂ * g(n) for all n ≥ n₀`

---

## Common Complexity Classes

| Complexity            | Notation        | Example Use Case                 |
| --------------------- | --------------- | -------------------------------- |
| **Constant Time**     | \(O(1)\)        | Accessing an array element       |
| **Logarithmic Time**  | \(O(\log n)\)   | Binary search                    |
| **Linear Time**       | \(O(n)\)        | Iterating through an array       |
| **Linearithmic Time** | \(O(n \log n)\) | Merge Sort                       |
| **Quadratic Time**    | \(O(n^2)\)      | Nested loops (e.g., Bubble Sort) |
| **Exponential Time**  | \(O(2^n)\)      | Tower of Hanoi                   |

---

## Visual Representation

The following table compares the growth rates of common complexity classes for increasing input sizes:

| Input Size (\(n\)) | \(O(1)\) | \(O(\log n)\) | \(O(n)\) | \(O(n \log n)\) | \(O(n^2)\) |
| ------------------ | -------- | ------------- | -------- | --------------- | ---------- |
| 1                  | 1        | 0             | 1        | 0               | 1          |
| 10                 | 1        | 1             | 10       | 10              | 100        |
| 100                | 1        | 2             | 100      | 200             | 10,000     |
| 1,000              | 1        | 3             | 1,000    | 3,000           | 1,000,000  |

---

## Importance of Asymptotic Notation

1. **Scalability**: Helps identify how algorithms perform as the input grows.
2. **Comparison**: Enables fair comparisons of different algorithms regardless of implementation details.
3. **Optimization**: Guides developers to choose algorithms that are best suited for their needs.

---

## Example: Analyzing Algorithm Complexity

### Code Example: Linear Time (\(O(n)\))

```python
def linear_search(arr, target):
    """
    Performs a linear search on the array.

    Args:
        arr (list): The array to search.
        target: The target element to find.

    Returns:
        int: The index of the target element, or -1 if not found.
    """
    for i in range(len(arr)):  # Loop runs 'n' times
        if arr[i] == target:
            return i
    return -1
```
