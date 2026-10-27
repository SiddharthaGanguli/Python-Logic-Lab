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
