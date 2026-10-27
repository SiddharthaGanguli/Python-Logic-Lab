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
