# Day 7 — Searching and ordering

Practice binary-search boundaries, rotated order, interval merging, and counting
out-of-order pairs. The search exercises assume their stated ordering contracts;
checking those contracts would itself require a linear scan. Complexity counts
below use constant-cost integer comparisons and arithmetic.

## 1. Find a lower-bound insertion index

Write `lower_bound(numbers, target)` to return the first index whose value is
greater than or equal to `target`. If every value is smaller, return the list's
length. Use binary search rather than `bisect` or a linear scan.

### Requirements

- Accept an ascending sorted list of integers and an integer target.
- Duplicate values are allowed; return the first qualifying index.
- The result for an empty list is `0`.
- Preserve the input list. Sortedness is assumed, not checked.

### Examples

| Input | Output |
|---|---|
| `[1, 3, 3, 7], 3` | `1` |
| `[1, 3, 3, 7], 5` | `3` |
| `[1, 3, 3, 7], 9` | `4` |
| `[-5, -2, 4], -8` | `0` |
| `[], 4` | `0` |

### Approach and complexity

Search the half-open interval `[left, right)`, starting at `[0, len(numbers))`.
Values before `left` are too small. When the middle value qualifies, keep it as
a possible boundary by moving `right` to the middle. Otherwise discard it and
the values before it. The two boundaries meet at the answer.

For `n` values, time is O(log(n + 1)) and auxiliary space is O(1); no list copy
is made. Empty input takes constant time.

[Solution](lower_bound.py) · [Tests](test_lower_bound.py)
