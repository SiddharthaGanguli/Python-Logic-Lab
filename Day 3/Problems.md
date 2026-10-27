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

## 4. Encode consecutive character runs

Write `encode_runs(text)` to represent each maximal run of consecutive equal
characters as a `(character, count)` tuple, in its original order.

### Requirements

- Return a list of tuples, rather than a string such as `"a3b2"`, so digit characters remain unambiguous.
- Count characters case-sensitively without filtering spaces, digits, or punctuation.
- Keep separate runs separate, even when the same character appears again later.
- Return an empty list for an empty string. Every returned count must be positive.

### Examples

| Input | Output |
|---|---|
| `"aaabbcaa"` | `[("a", 3), ("b", 2), ("c", 1), ("a", 2)]` |
| `"11122"` | `[("1", 3), ("2", 2)]` |
| `"Aa"` | `[("A", 1), ("a", 1)]` |
| `""` | `[]` |

### Approach and complexity

Track the current character and count. Emit a tuple when the character changes,
and emit the final run after the scan. For `n` characters and `r` runs, time is O(n).
The returned list takes O(r) space; auxiliary space excluding that output is O(1).

[Solution](run_length_encoding.py) · [Tests](test_run_length_encoding.py)

## 5. Find the longest common prefix

Write `longest_common_prefix(words)` to find the longest starting substring shared
by every string in a list.

### Requirements

- Compare characters exactly: case, whitespace, and Unicode code points are significant.
- Return `""` for an empty list, an empty member, or no shared starting character.
- For one string, return that complete string.
- Do not sort or modify the input list.

### Examples

| Input | Output |
|---|---|
| `["flower", "flow", "flight"]` | `"fl"` |
| `["carpet", "car", "cart"]` | `"car"` |
| `["Apple", "apple"]` | `""` |
| `["abc", ""]` | `""` |
| `[]` | `""` |

### Approach and complexity

Start with the first string's length and shorten the possible prefix while
comparing each string against the first. Stop when the prefix becomes empty. For
`k` strings containing `S` characters in total, time is O(k + S). Auxiliary space
is O(1); the returned prefix requires up to O(p) space for prefix length `p`.

[Solution](longest_common_prefix.py) · [Tests](test_longest_common_prefix.py)
