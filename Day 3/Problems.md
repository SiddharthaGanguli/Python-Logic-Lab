# Day 3 — String reasoning

Practice normalization, character counts, consecutive runs, and shared prefixes.
Each exercise defines exactly which characters matter before choosing an algorithm.

## 1. Check a normalized palindrome

Write `is_palindrome(text)` to determine whether a string reads the same from both
ends after normalization. Compare from both ends without reversing the cleaned text.

### Requirements

- Apply `str.casefold()` first, then retain only characters for which `str.isalnum()` is true.
- This includes Unicode letters and digits; spaces and punctuation are discarded.
- Return `True` when the normalized string is empty or contains one character.
- Apply no other Unicode normalization. Accept a string and leave it unchanged.

### Examples

| Input | Output |
|---|---|
| `"A man, a plan, a canal: Panama!"` | `True` |
| `"1a2"` | `False` |
| `"ßaSS"` | `True` |
| `"..."` | `True` |

### Approach and complexity

Build the normalized string, then move two indices inward. A mismatch ends the
comparison immediately. For an input of length `n`, normalization and comparison
take O(n) time and O(n) extra space, including the cleaned string.

[Solution](palindrome_text.py) · [Tests](test_palindrome_text.py)
