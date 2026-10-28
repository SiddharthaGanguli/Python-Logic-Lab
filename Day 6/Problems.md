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
