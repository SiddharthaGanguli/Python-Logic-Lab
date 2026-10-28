# Day 8 — Windows and dynamic programming

Practice keeping useful state as a window moves or a larger answer grows from
smaller subproblems. Try each question before opening its solution and tests.

## 1. Find the longest substring with distinct characters

Write `longest_distinct_substring(text)` to return the length of the longest
contiguous substring containing no repeated characters.

### Requirements

- Compare Unicode code points exactly, without case folding or normalization.
- Spaces and punctuation count as characters. Uppercase and lowercase letters differ.
- Return a length, not the substring itself. Empty input returns `0`.
- Use a sliding window rather than generating every possible substring.

### Examples

| Input | Expected output |
|---|---|
| `"abcabcbb"` | `3` |
| `"pwwkew"` | `3` |
| `"abba"` | `2` |
| `"aA a"` | `3` |
| `""` | `0` |

### Approach and complexity

Track the most recent index of each character. When a character repeats inside
the current window, move the left boundary beyond its previous occurrence. Never
move that boundary backward for a duplicate already outside the window. For `n`
characters and `u` distinct code points, expected time is O(n) and extra space is O(u).

[Solution](longest_distinct_substring.py) · [Tests](test_longest_distinct_substring.py)

## 2. Find the maximum sum of a fixed-size window

Write `maximum_window_sum(numbers, size)` to return the largest sum of exactly
`size` consecutive integers.

### Requirements

- `numbers` is a list of integers and `size` is an integer.
- Raise `ValueError` if `size <= 0` or `size > len(numbers)`; an empty list has no valid window.
- Negative values are allowed. A shorter or empty window is never a valid substitute.
- Leave the input unchanged and solve the problem in one linear scan.

### Examples

| Input | Expected output |
|---|---|
| `maximum_window_sum([2, 1, 5, 1, 3, 2], 3)` | `9` |
| `maximum_window_sum([-8, -3, -6, -2], 2)` | `-8` |
| `maximum_window_sum([-4, 3, 1], 1)` | `3` |
| `maximum_window_sum([-4, 3, 1], 3)` | `0` |
| `maximum_window_sum([], 1)` | raises `ValueError` |

### Approach and complexity

Sum the first window and use it to initialize the best result, including for
negative-only input. Each step subtracts the outgoing value and adds the incoming
value. For `n` numbers, time is O(n) and extra space is O(1).

[Solution](fixed_window_sum.py) · [Tests](test_fixed_window_sum.py)

## 3. Make an amount with the fewest coins

Write `minimum_coin_change(coins, amount)` to find the minimum number of coins
needed to make an exact amount. Each denomination may be used any number of times.

### Requirements

- `coins` contains integer denominations and `amount` is an integer.
- Reject any coin value `<= 0` or an amount `< 0` with `ValueError`.
- Validate denominations even when `amount == 0`. A valid zero amount returns `0`.
- Return `-1` when the amount cannot be formed. Duplicate denominations are allowed.
- An empty coin list is valid: it makes only amount zero. Do not modify the list.

### Examples

| Input | Expected output |
|---|---|
| `minimum_coin_change([1, 3, 4], 6)` | `2` |
| `minimum_coin_change([2, 4], 7)` | `-1` |
| `minimum_coin_change([2, 3, 3], 6)` | `2` |
| `minimum_coin_change([], 0)` | `0` |
| `minimum_coin_change([], 4)` | `-1` |
| `minimum_coin_change([0, 1], 0)` | raises `ValueError` |

### Approach and complexity

Store the fewest coins needed for every subtotal from zero through the target.
For a subtotal, try each denomination as its last coin. An unreachable marker
distinguishes impossible subtotals from valid counts. A largest-coin-first greedy
strategy fails for `[1, 3, 4]` and amount `6`: two threes beat four plus two ones.

For `k` denominations and amount `A`, a nonempty coin list takes O(k + A*k) time,
including validation, and O(A + 1) extra space. Empty coin lists return directly.

[Solution](minimum_coin_change.py) · [Tests](test_minimum_coin_change.py)

## 4. Find the longest strictly increasing subsequence

Write `lis_length(numbers)` to return the length of the longest strictly increasing
subsequence of a list of integers.

### Requirements

- A subsequence keeps the original index order but may skip elements; it need not be contiguous.
- Values must increase strictly. Equal values cannot extend the subsequence.
- Return `0` for empty input and leave the list unchanged.
- Implement the O(n²) dynamic-programming approach with a length for each ending index.

### Examples

| Input | Expected output |
|---|---|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | `4` |
| `[1, 4, 2, 3]` | `3` |
| `[1, 2, 2, 3]` | `3` |
| `[7, 7, 7]` | `1` |
| `[]` | `0` |

### Approach and complexity

Initialize every ending length to one. For each current index, consider earlier
indices with smaller values and extend the best eligible subsequence. The largest
ending length is the answer. For `n` values, time is O(n²) and extra space is O(n).

[Solution](longest_increasing_subsequence.py) · [Tests](test_longest_increasing_subsequence.py)
