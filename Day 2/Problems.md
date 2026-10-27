# Day 2 — Lists and searching

Practice index arithmetic, sorted traversal, lookup tables, and running totals. Each question includes a reference solution and tests; try the question before opening the solution.

## 1. Rotate a list to the right

Write `rotate_right(numbers, steps)` to return a new list with every element moved `steps` positions to the right. Elements that pass the end wrap around to the beginning.

### Requirements

- `numbers` is a list of integers and `steps` is an integer.
- Support zero steps and step counts larger than the list length.
- Return an empty list for empty input. Raise `ValueError` for negative steps, including when the input is empty.
- Leave the original list unchanged and always return a new list.

### Examples

| Input | Expected output |
|---|---|
| `rotate_right([1, 2, 3, 4, 5], 2)` | `[4, 5, 1, 2, 3]` |
| `rotate_right([2, 2, -1], 10)` | `[-1, 2, 2]` |
| `rotate_right([1, 2], 0)` | `[1, 2]` |
| `rotate_right([], 3)` | `[]` |

### Approach and complexity

Reduce the rotation with `steps % len(numbers)` after handling empty input. For each output index, use modular arithmetic to find the corresponding input index. This takes O(n) time and O(1) auxiliary space, excluding the O(n) returned list.

[Solution](rotate_list.py) · [Tests](test_rotate_list.py)

## 2. Merge two sorted lists

Write `merge_sorted_lists(left, right)` to combine two lists into a new sorted list without sorting the combined input.

### Requirements

- Both inputs contain integers in nondecreasing order; assume this precondition is satisfied.
- Keep all values, including duplicates from either input.
- Handle empty inputs and lists of different lengths.
- Do not modify either input. Do not call `sort()` or `sorted()` in the solution.

### Examples

| Input | Expected output |
|---|---|
| `merge_sorted_lists([1, 3, 5], [2, 3, 6])` | `[1, 2, 3, 3, 5, 6]` |
| `merge_sorted_lists([-8, -3], [-2, -1, 0])` | `[-8, -3, -2, -1, 0]` |
| `merge_sorted_lists([], [1, 2])` | `[1, 2]` |
| `merge_sorted_lists([], [])` | `[]` |

### Approach and complexity

Keep one index for each input. Append the smaller current value and advance its index. When one input is exhausted, append the remaining values from the other. For input lengths m and n, time is O(m + n) and auxiliary space is O(1), excluding the O(m + n) returned list.

[Solution](merge_sorted_lists.py) · [Tests](test_merge_sorted_lists.py)

## 3. Find the missing number

A list of length n contains distinct integers from 0 through n, inclusive, with exactly one value missing. Write `missing_number(numbers)` to return that value.

### Requirements

- The list can be in any order and must remain unchanged.
- Assume the values are distinct and within the stated range; input validation is not part of this exercise.
- Either endpoint, 0 or n, may be missing.
- For an empty list, the only missing value is 0.

### Examples

| Input | Expected output |
|---|---|
| `missing_number([3, 0, 1])` | `2` |
| `missing_number([1, 2, 3])` | `0` |
| `missing_number([2, 0, 1])` | `3` |
| `missing_number([])` | `0` |

### Approach and complexity

The sum of the complete range is `n * (n + 1) // 2`. Subtract each observed number; the remaining total is the missing value. Time is O(n), with O(1) auxiliary space under the usual unit-cost integer model.

[Solution](missing_number.py) · [Tests](test_missing_number.py)

## 4. Find two indices with a target sum

Write `two_sum(numbers, target)` to return the indices of two distinct elements whose values add up to `target`.

### Requirements

- Inputs are a list of integers and an integer target; negative numbers and duplicate values are allowed.
- Return a tuple `(first, second)` where `first < second`, or `None` if no pair exists.
- If several pairs exist, choose the smallest `second` index, then the smallest `first` index.
- Never use one element twice and do not modify the input.

### Examples

| Input | Expected output |
|---|---|
| `two_sum([2, 7, 11, 15], 9)` | `(0, 1)` |
| `two_sum([3, 3], 6)` | `(0, 1)` |
| `two_sum([1, 1, 4, 2, 3], 5)` | `(0, 2)` |
| `two_sum([1, 2, 3, 4], 5)` | `(1, 2)` |
| `two_sum([3], 6)` | `None` |

### Approach and complexity

Scan from left to right and store the earliest index of each previously seen value. Look up `target - number` before inserting the current number, so an element cannot pair with itself. Expected time is O(n) with O(n) auxiliary space for the dictionary.

[Solution](two_sum.py) · [Tests](test_two_sum.py)
