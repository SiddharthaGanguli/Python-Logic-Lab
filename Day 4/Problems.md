# Day 4 — Number logic

Practice divisibility, repeated division, binary search, and sequences using
integer arithmetic. Inputs are integers unless stated otherwise. The operation
counts below use the usual unit-cost arithmetic model; Python's arbitrary-size
integers take more time and memory as their bit lengths grow.

## 1. Check whether a number is prime

Write `is_prime(number)` to return whether `number` has exactly two positive
divisors. Every integer below 2, including negative numbers, returns `False`.
Use trial division without converting the number to a floating-point square root.

| Input | Expected output |
|---|---|
| `-7` | `False` |
| `2` | `True` |
| `29` | `True` |
| `49` | `False` |

**Approach:** Handle 2 separately and reject the other even numbers. Check odd
divisors while `divisor <= number // divisor`. A composite number must have a
factor no larger than its square root; testing that boundary also catches squares.

**Complexity:** For positive `n`, O(sqrt(n)) arithmetic operations in the worst
case and a constant number of auxiliary integer variables. Trial division is
intended for practice with modest inputs, not cryptographic-size primality tests.

[Solution](prime_number.py) · [Tests](test_prime_number.py)
