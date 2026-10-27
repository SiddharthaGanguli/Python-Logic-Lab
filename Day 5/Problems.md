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
