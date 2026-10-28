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

## 2. Search a rotated sorted list

Write `search_rotated(numbers, target)` to return the target's index, or `-1`
when it is absent. Adapt binary search so each step discards half the remaining
candidates, without slicing the input or finding the pivot by a linear scan.

### Requirements

- The input is a rotation of an ascending list of distinct integers.
- An unrotated list is also valid. Duplicates are outside this exercise's contract.
- Return `-1` for an empty list or missing target.
- Preserve the input list; assume its rotation and uniqueness are valid.

### Examples

| Input | Output |
|---|---|
| `[4, 5, 6, 7, 0, 1, 2], 0` | `4` |
| `[4, 5, 6, 7, 0, 1, 2], 3` | `-1` |
| `[2, 1], 1` | `1` |
| `[-5, 0, 8], -5` | `0` |
| `[], 2` | `-1` |

### Approach and complexity

Check the middle value first. With distinct elements, at least one half is sorted.
Use that half's endpoint values to decide whether it contains the target; keep
that half or discard it accordingly. Continue until a match is found or the
candidate interval is empty.

For `n` values, time is O(log(n + 1)) and auxiliary space is O(1). The algorithm
uses indices only and makes no copy. Empty input takes constant time.

[Solution](search_rotated.py) · [Tests](test_search_rotated.py)

## 3. Merge overlapping intervals

Write `merge_intervals(intervals)` to combine overlapping or touching closed
intervals. Return a new list of `(start, end)` tuples, sorted by start, covering
exactly the same points as the input.

### Requirements

- Input is a list of two-integer tuples `(start, end)` in any order.
- Raise `ValueError` if an interval has `start > end`.
- Closed intervals sharing an endpoint merge: `(1, 3)` and `(3, 5)` become `(1, 5)`.
- Point intervals such as `(2, 2)` are valid. An empty list returns `[]`.
- Keep gaps: `(1, 2)` and `(3, 4)` remain separate despite integer endpoints.
- Preserve the input and return new interval tuples.

### Examples

| Input | Output |
|---|---|
| `[(8, 10), (1, 3), (2, 6), (10, 12)]` | `[(1, 6), (8, 12)]` |
| `[(1, 3), (3, 5)]` | `[(1, 5)]` |
| `[(1, 8), (2, 3), (8, 8)]` | `[(1, 8)]` |
| `[(2, 2), (1, 1)]` | `[(1, 1), (2, 2)]` |
| `[(3, 1)]` | `ValueError` |

### Approach and complexity

Validate endpoints and sort a copy of the input. Track the current interval and
extend its end when the next start touches or overlaps it. When a gap appears,
emit the current interval and start another. Emit the final interval after the
scan.

For `n` intervals, sorting takes O(n log n) time and the scan takes O(n).
The sorted copy and sorting workspace use O(n) auxiliary space; the output uses
O(k) space for `k` merged intervals. Empty input returns in constant time.

[Solution](merge_intervals.py) · [Tests](test_merge_intervals.py)

## 4. Count inversions without changing the list

Write `count_inversions(numbers)` to count index pairs `(i, j)` satisfying
`i < j` and `numbers[i] > numbers[j]`. Use merge sort to avoid checking every
pair individually.

### Requirements

- Accept a list of integers, including negative and repeated values.
- Equal values are not inversions.
- Empty and single-element inputs return `0`.
- Preserve the original list and return the count as an integer.

### Examples

| Input | Output |
|---|---|
| `[2, 4, 1, 3, 5]` | `3` |
| `[3, 2, 1]` | `3` |
| `[2, 1, 2, 1]` | `3` |
| `[7, 7, 7]` | `0` |
| `[]` | `0` |

### Approach and complexity

Copy the list, recursively count each half's inversions, then merge the sorted
halves. When the next right-side value is smaller than the next left-side value,
it forms an inversion with every remaining left-side value. Add that remaining
count at once. Choosing the left value when values are equal prevents duplicates
from being counted.

For `n` values, time is O(n log n) for `n >= 2`. The working copy and reusable
merge buffer occupy O(n) space, and recursion adds O(log n) stack space. Overall
auxiliary space is O(n). Inputs of length zero or one take constant time.

[Solution](count_inversions.py) · [Tests](test_count_inversions.py)
