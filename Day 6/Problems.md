# Day 6 — Recursion and backtracking

Backtracking builds a partial answer, checks whether it can still lead to a
solution, and removes its last choice before trying the next one. This question
uses that pattern to enumerate every valid arrangement without producing invalid
ones first.

## 1. Generate balanced parentheses

Write `generate_parentheses(pairs)` to return every properly balanced string
containing exactly `pairs` opening and `pairs` closing parentheses.

### Requirements

- Return the strings in lexicographic order, with `"("` considered before `")"`.
- Return `[""]` for zero pairs: the empty string is the one valid arrangement.
- Return a new list and do not print during import.
- Raise `ValueError` if `pairs` is negative.
- Generate candidates by backtracking; do not enumerate all `2 ** (2 * pairs)`
  strings and filter them afterward.

### Examples

| Input | Expected output |
|---|---|
| `0` | `[""]` |
| `1` | `["()"]` |
| `2` | `["(())", "()()"]` |
| `3` | `["((()))", "(()())", "(())()", "()(())", "()()()"]` |
| `-1` | `ValueError` |

### Approach and complexity

At every partial string, add an opening parenthesis only while fewer than
`pairs` have been used. Add a closing parenthesis only when it can close a
previous opening parenthesis. These rules ensure each completed string is valid,
and trying openings first produces lexicographic order.

There are `C(pairs)` valid strings, where `C` is the Catalan-number sequence.
Building and storing the output takes O(C(pairs) * pairs) time and output space,
because every result has `2 * pairs` characters. The mutable working path uses
O(pairs) auxiliary space.

[Solution](generate_parentheses.py) · [Tests](test_generate_parentheses.py)

## 2. Generate every subset

Write `subsets(numbers)` to return every subset of a list of distinct integers.

### Requirements

- Assume all input values are distinct; do not sort or modify the input.
- Keep the input order within each subset.
- Return results in backtracking preorder: emit the current subset first, then
  extend it using each later input index from left to right.
- The empty subset comes first; empty input returns `[[]]`.
- Return independent lists so changing one result cannot change another.

### Examples

| Input | Expected output |
|---|---|
| `[]` | `[[]]` |
| `[-2]` | `[[], [-2]]` |
| `[3, 1, 2]` | `[[], [3], [3, 1], [3, 1, 2], [3, 2], [1], [1, 2], [2]]` |

### Approach and complexity

Save a copy of the current path, choose a later input value, recurse from the
following index, and undo the choice. Each subset has a unique increasing
sequence of input indices, so no duplicate branch is needed.

For n values there are `2**n` subsets. Copying them takes O(n * 2**n) time and
output space for n > 0; empty input takes constant time and space. The working
path and recursion use O(n) auxiliary space, with at most n choices on a path.

[Solution](subsets.py) · [Tests](test_subsets.py)

## 3. Generate unique permutations

Write `unique_permutations(numbers)` to return every distinct rearrangement of
a list of integers, including lists that contain repeated values.

### Requirements

- Return each permutation once, with the result list in lexicographic order.
- Keep the original input unchanged, even if it is unsorted.
- Keep the same number of occurrences of every value in each result.
- Return `[[]]` for empty input and independent lists for all results.
- Avoid producing all repeated permutations and deduplicating them afterward.

### Examples

| Input | Expected output |
|---|---|
| `[2, 1, 1]` | `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]` |
| `[0, -1]` | `[[-1, 0], [0, -1]]` |
| `[4, 4]` | `[[4, 4]]` |
| `[]` | `[[]]` |

### Approach and complexity

Count each distinct value and consider those values in sorted order. Choose
only values with a positive remaining count, decrement the count while exploring
that choice, and restore it afterward. A full path becomes one permutation.

Let n be the input length, d the distinct-value count, P the number of unique
permutations, and V the number of visited partial paths. Building counts and
sorting choices takes O(n + d log d). Traversal and result copying take
O(d * V + n * P); for all-distinct inputs this is O(n * n!). Output space is
O(n * P) for nonempty input. Auxiliary space is O(n + d), and recursion depth
is at most n choices. Empty input takes constant time and space.

[Solution](unique_permutations.py) · [Tests](test_unique_permutations.py)

## 4. Build combinations with a target sum

Write `combination_sum(candidates, target)` to return every unique combination
of candidate values that sums to the target. A candidate may be reused.

### Requirements

- Candidates are positive integers and target is a nonnegative integer.
- Raise `ValueError` for any nonpositive candidate or negative target. Check
  candidates even when target is zero.
- Ignore duplicate candidate values and preserve the original input.
- Keep values inside each combination in nondecreasing order, and return the
  combinations in lexicographic order with no duplicates.
- Zero target returns `[[]]`; an unreachable positive target returns `[]`.

### Examples

| Candidates | Target | Expected output |
|---|---:|---|
| `[2, 3, 6, 7]` | `7` | `[[2, 2, 3], [7]]` |
| `[5, 3, 2, 2]` | `8` | `[[2, 2, 2, 2], [2, 3, 3], [3, 5]]` |
| `[2, 4]` | `3` | `[]` |
| `[]` | `0` | `[[]]` |
| `[0, 2]` | `0` | `ValueError` |

### Approach and complexity

Sort the distinct candidates. At each step, try values from the current index
onward; recurse from the chosen index again to allow reuse. Stop trying larger
values once a candidate exceeds the remaining target. Restricting future choices
to the same or later index prevents rearrangements of one combination.

For c supplied candidates and m distinct values, preprocessing takes expected
O(c + m log m) time. Let V be the number of explored partial combinations and L
the total number of integers in the returned combinations. The search takes
O(m * V + L) time, an output-sensitive bound that can grow exponentially.
For K results, output space is O(K + L). With nonempty candidates, at most
`target // min(candidates)` choices can fit on a path; call this D. Auxiliary
space is O(m + D), with at most D choices in the recursion. Empty candidates
need only a constant-size search.

[Solution](combination_sum.py) · [Tests](test_combination_sum.py)
