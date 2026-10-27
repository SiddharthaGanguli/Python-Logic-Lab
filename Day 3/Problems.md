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

## 2. Compare words as anagrams

Write `are_anagrams(first, second)` to check whether two strings contain the same
characters with the same frequencies after ignoring case and whitespace. Use
character counts rather than sorting the inputs.

### Requirements

- Case-fold each string and remove characters for which `str.isspace()` is true.
- Punctuation and digits remain significant: `"ab!"` and `"ba"` are not anagrams.
- Empty and whitespace-only strings are anagrams of each other.
- Apply no additional Unicode normalization; `"é"` and `"e\u0301"` remain different.
- Accept two strings and leave the original values unchanged.

### Examples

| First input | Second input | Output |
|---|---|---|
| `"Dormitory"` | `"Dirty room"` | `True` |
| `"aab"` | `"abb"` | `False` |
| `"ab!"` | `"ba"` | `False` |
| `"Straße"` | `"strasse"` | `True` |

### Approach and complexity

Compare normalized lengths, count characters in the first string, and consume
those counts while scanning the second. Equal lengths ensure successful consumption
uses every count. For input lengths `n` and `m`, expected time is O(n + m) and extra
space is O(n + m), including both normalized strings and the frequency dictionary.

[Solution](anagram_words.py) · [Tests](test_anagram_words.py)

## 3. Find the first unique character

Write `first_unique_character(text)` to return the first character appearing exactly
once in a string. Return the character itself, not its index.

### Requirements

- Matching is case-sensitive; `"a"` and `"A"` are different characters.
- Spaces, punctuation, and Unicode code points count like any other character.
- Return `None` for empty input or when every character repeats.
- Preserve original order when choosing between multiple unique characters.

### Examples

| Input | Output |
|---|---|
| `"swiss"` | `"w"` |
| `"aA"` | `"a"` |
| `"aa bb"` | `" "` |
| `"aabb"` | `None` |
| `""` | `None` |

### Approach and complexity

Count frequencies in one pass. Scan the original string again and return the first
character with count one. For `n` characters and `u` distinct characters, expected
time is O(n) and extra space is O(u).

[Solution](first_unique_character.py) · [Tests](test_first_unique_character.py)
