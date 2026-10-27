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

## 2. Find the greatest common divisor

Write `gcd(first, second)` using Euclid's algorithm. Accept positive, negative,
and zero inputs, and return a nonnegative result. Define `gcd(0, 0)` as `0`.
Do not use `math.gcd` in the solution.

| Input | Expected output |
|---|---|
| `48, 18` | `6` |
| `-24, 36` | `12` |
| `35, 64` | `1` |
| `0, -9` | `9` |
| `0, 0` | `0` |

**Approach:** Work with the magnitudes. Repeatedly replace the pair `(a, b)`
with `(b, a % b)` until the second value is zero. The first value is then the GCD.

**Complexity:** O(log(M + 1)) remainder operations, where `M` is the larger
input magnitude, and a constant number of auxiliary integer variables.

[Solution](greatest_common_divisor.py) · [Tests](test_greatest_common_divisor.py)
