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
