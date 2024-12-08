# Euclidean Algorithm

The **Euclidean Algorithm** is an efficient method for finding the **Greatest Common Divisor (GCD)** of two integers. The GCD is the largest number that divides both integers without leaving a remainder.

---

## How the Algorithm Works

1. Take two numbers, `a` and `b`, where \( a > b \).
2. Compute the remainder of \( a \div b \), denoted as \( r \).
3. Replace \( a \) with \( b \) and \( b \) with \( r \).
4. Repeat the process until \( b = 0 \).
5. When \( b = 0 \), the value of `a` is the GCD of the original two numbers.

---

## Example: GCD of 56 and 98

1. \( 98 \div 56 = 1 \) remainder \( 42 \). Replace \( a = 56 \), \( b = 42 \).
2. \( 56 \div 42 = 1 \) remainder \( 14 \). Replace \( a = 42 \), \( b = 14 \).
3. \( 42 \div 14 = 3 \) remainder \( 0 \). Stop, as \( b = 0 \).

**Result**: The GCD of 56 and 98 is **14**.

---

## Python Implementation

Here's how you can implement the Euclidean Algorithm in Python:

```python
def gcd(a, b):
    """
    Computes the Greatest Common Divisor (GCD) of two integers using the Euclidean Algorithm.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The GCD of a and b
    """
    while b != 0:  # Continue until the remainder becomes 0
        a, b = b, a % b  # Update a to b and b to the remainder
    return a  # When b is 0, a is the GCD

# Example usage:
num1 = 56
num2 = 98
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
```
