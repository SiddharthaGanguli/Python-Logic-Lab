# Day 5 — Dictionaries, stacks, and structured data

Practice choosing a data structure that makes the next step simple. Try each
question before reading its solution. Inputs follow the documented types;
complexity assumes constant-cost arithmetic and hash operations unless noted.

## 1. Count repeated items

Write `count_frequencies(items)` to count the occurrences of each string in a list.

### Requirements

- Return a dictionary whose keys follow the order of first appearance.
- Treat uppercase and lowercase strings as different items; an empty string is valid.
- Return `{}` for an empty list, and preserve the input.
- Build the counts yourself without `collections.Counter`.

### Examples

| Input | Expected output |
|---|---|
| `["red", "blue", "red", "green", "blue"]` | `{"red": 2, "blue": 2, "green": 1}` |
| `["A", "a", "", ""]` | `{"A": 1, "a": 1, "": 2}` |
| `[]` | `{}` |

### Approach and complexity

Update a dictionary as each item arrives. Python dictionaries preserve insertion
order, so an existing key keeps its position when its count changes. Expected
O(n) time and O(k) output space for k distinct items, treating string hashing
as constant cost; hashing long strings also depends on their lengths. O(1)
auxiliary space beyond the result under this model.

[Solution](count_frequencies.py) · [Tests](test_count_frequencies.py)

## 2. Check balanced brackets

Write `has_balanced_brackets(text)` to check whether `()`, `[]`, and `{}` close in
the correct nesting order.

### Requirements

- Ignore all other characters; empty text is balanced.
- A closing bracket must match the most recent unclosed opening bracket.
- Reject unmatched opening or closing brackets and crossed pairs such as `([)]`.
- This is a text exercise, not a Python parser: brackets inside quotes still count.

### Examples

| Input | Expected output |
|---|---|
| `"{[()]}()[]"` | `True` |
| `"items[(2 + 3)]"` | `True` |
| `"([)]"` | `False` |
| `"("` | `False` |
| `""` | `True` |

### Approach and complexity

Push opening brackets onto a stack. For a closing bracket, pop and compare the
last opening bracket. At the end, the stack must be empty. O(n) time and O(n)
auxiliary space in the worst case.

[Solution](balanced_brackets.py) · [Tests](test_balanced_brackets.py)

## 3. Find a unique intersection

Write `unique_intersection(first, second)` to return each integer shared by two
lists exactly once, in the order it first appears in `first`.

### Requirements

- Inputs can be unsorted and contain duplicates or negative integers.
- Do not sort or mutate either input.
- Return a new list; if either input is empty or there are no matches, return `[]`.

### Examples

| First list | Second list | Expected output |
|---|---|---|
| `[3, 1, 3, 2, 4]` | `[2, 3, 3]` | `[3, 2]` |
| `[-1, 0, -1, 2, 0]` | `[0, -1, -1]` | `[-1, 0]` |
| `[1]` | `[2]` | `[]` |

### Approach and complexity

Build a membership set from `second` and track values already emitted. Walk
`first` in its original order. Expected O(n + m) time for the two input lengths,
O(m + k) auxiliary space, and O(k) output space for k shared distinct values.

[Solution](unique_intersection.py) · [Tests](test_unique_intersection.py)

## 4. Transpose a rectangular matrix

Write `transpose_matrix(matrix)` to return a new matrix with rows and columns swapped.

### Requirements

- The input is a list of integer lists; all rows must have equal lengths.
- Raise `ValueError` for unequal row lengths, including an empty row mixed with a nonempty row.
- Return `[]` for `[]` or for a rectangular matrix with zero columns, such as `[[], []]`.
- Preserve the input and create independent output rows.
- Use indexing and loops or comprehensions rather than `zip()` for the core solution.

### Examples

| Input | Expected output |
|---|---|
| `[[1, 2, 3], [4, 5, 6]]` | `[[1, 4], [2, 5], [3, 6]]` |
| `[[1], [2]]` | `[[1, 2]]` |
| `[[], []]` | `[]` |
| `[[1], [2, 3]]` | `ValueError` |

### Approach and complexity

Check row lengths, then collect each column into a new row. For r rows and c
columns, the work is O(r + r*c): validation still visits rows when c is zero.
The output occupies O(r*c) space, with O(1) auxiliary space beyond it.

[Solution](transpose_matrix.py) · [Tests](test_transpose_matrix.py)

## 5. Count subarrays with a target sum

Write `count_target_subarrays(numbers, target)` to count contiguous, nonempty
subarrays whose values add up to `target`.

### Requirements

- Inputs and target are integers; negative numbers and zeros are valid.
- Count overlapping matches separately, including matches starting at index zero.
- Return `0` for an empty list and preserve the input.
- Aim for a single traversal instead of checking every possible subarray.

### Examples

| Numbers | Target | Expected output |
|---|---|---:|
| `[1, 2, 1, 2]` | `3` | `3` |
| `[1, -1, 0]` | `0` | `3` |
| `[0, 0, 0]` | `0` | `6` |
| `[]` | `0` | `0` |

### Approach and complexity

Track the running prefix sum and how often each earlier sum occurred. A previous
sum equal to `current_sum - target` starts a matching subarray. Seed the counts
with `{0: 1}` to include matches beginning at the first element, and query before
recording the current sum so empty subarrays are excluded. Expected O(n) time
and O(n) auxiliary space under the stated arithmetic and hashing assumptions.

[Solution](count_target_subarrays.py) · [Tests](test_count_target_subarrays.py)
