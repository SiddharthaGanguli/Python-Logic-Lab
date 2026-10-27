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

## 3. Convert a decimal integer to binary

Write `decimal_to_binary(number)` to return a nonnegative integer's binary digits
as a string. Do not use `bin()`, `format()`, or binary format specifiers in the
solution. The result has no `0b` prefix and no extra leading zeroes. Return `"0"`
for zero and raise `ValueError` for a negative integer.

| Input | Expected output |
|---|---|
| `0` | `"0"` |
| `1` | `"1"` |
| `10` | `"1010"` |
| `42` | `"101010"` |
| `-1` | `ValueError` |

**Approach:** Repeatedly divide by 2 and collect the remainders. They arrive
least-significant digit first, so reverse them before joining them into a string.

**Complexity:** O(b) division steps and character work, where `b` is the number
of output bits. The digit list uses O(b) auxiliary space and the result uses O(b)
characters. Big-integer division itself is not a constant-time machine operation.

[Solution](decimal_to_binary.py) · [Tests](test_decimal_to_binary.py)

## 4. Find the integer square root

Write `integer_square_root(number)` to return the largest integer `r` satisfying
`r * r <= number`. Use binary search and integer arithmetic, without `sqrt()` or
`math.isqrt()` in the solution. Accept zero and positive integers; raise
`ValueError` for negative integers.

| Input | Expected output |
|---|---|
| `0` | `0` |
| `1` | `1` |
| `8` | `2` |
| `16` | `4` |
| `26` | `5` |
| `-1` | `ValueError` |

**Approach:** Search the integer interval from 0 to `number`. If the middle
value's square fits, record it and search larger candidates; otherwise search
smaller candidates. The saved candidate is the floor square root when the search
interval becomes empty.

**Complexity:** O(log(n + 1)) search iterations for positive `n`, with a constant
number of auxiliary integer variables. Zero takes constant time. The arithmetic
and storage costs of very large integers depend on their bit lengths.

[Solution](integer_square_root.py) · [Tests](test_integer_square_root.py)

## 5. Generate a Fibonacci sequence

Write `fibonacci_sequence(count)` to return the first `count` Fibonacci values
as a new list, starting at `0, 1`. Each later value is the sum of the previous two.
Return an empty list for zero and raise `ValueError` for a negative count. Use an
iterative solution rather than recursive recomputation.

| Input | Expected output |
|---|---|
| `0` | `[]` |
| `1` | `[0]` |
| `2` | `[0, 1]` |
| `7` | `[0, 1, 1, 2, 3, 5, 8]` |
| `-1` | `ValueError` |

**Approach:** Keep the current and next values. Append the current value, then
advance both variables together. A loop makes the requested sequence length
explicit and avoids recalculating earlier values.

**Complexity:** O(count) additions and O(count) output integer slots, plus a
constant number of working integer variables. Fibonacci integers grow in size:
the returned values collectively occupy O(count squared) bits for large counts.

[Solution](fibonacci_sequence.py) · [Tests](test_fibonacci_sequence.py)
