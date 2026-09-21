from pathlib import Path

readme = """# Day 1 — Python Problem Solving

**Date:** 20 September 2026  
**Focus:** Python fundamentals, list traversal, comparison logic, and in-place array/list manipulation.

## Overview

This document contains the problems solved or planned for **Day 1** of the Python problem-solving journey. The main goal is to strengthen fundamental programming skills without relying on built-in functions for the core logic wherever restrictions are specified.

## Problems

### 1. Find the Largest Number

Write a Python program to find the largest number in a list.

#### Requirements

- Do not use built-in functions such as `max()`, `sort()`, or `sorted()`.
- Traverse the list and determine the largest value using comparison logic.
- The solution should work with both positive and negative numbers.

#### Examples

| Input | Expected Output |
|---|---:|
| `[1, 2, 3, 5, 6, 8]` | `8` |
| `[-8, -4, -2, -12]` | `-2` |

> **Note:** The largest number in `[-8, -4, -2, -12]` is `-2`, not `-3`.

---

### 2. Find the Second Largest Number

Write a Python program to find the second-largest **distinct** number in a list.

#### Requirements

- The second-largest value must be distinct from the largest value.
- Duplicate values should not be counted multiple times.
- Return `None` when a second-largest distinct value does not exist.
- The solution should support positive and negative numbers.

#### Examples

| Input | Expected Output |
|---|---:|
| `[4, 5, 6, 7, 8, 2]` | `7` |
| `[6, 2, 3, 9, 9, 8]` | `8` |
| `[6, 6, 6, 6]` | `None` |
| `[-5, -8, -12, -5]` | `-5` |

---

### 3. Move Zeros

Write a Python program to move all zeros in a list to the end while preserving the relative order of the non-zero elements.

#### Requirements

- Move every `0` to the end of the list.
- Preserve the original order of all non-zero elements.
- Avoid unnecessary changes to the order of non-zero values.

#### Examples

| Input | Expected Output |
|---|---|
| `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` |
| `[1, 2, 3]` | `[1, 2, 3]` |
| `[0, 0, 0]` | `[0, 0, 0]` |
| `[4, 0, 5, 0, 2]` | `[4, 5, 2, 0, 0]` |

---

### 4. Remove Duplicates from a Sorted List

Write a Python program to remove duplicate values from a sorted list.

#### Requirements

- The input list is sorted.
- Keep only one occurrence of each value.
- Preserve the sorted order.
- Consider using a two-pointer approach.
- Clearly define whether the solution modifies the original list or returns a new list.

#### Examples

| Input | Expected Output |
|---|---|
| `[1, 1, 2, 2, 3, 4, 4]` | `[1, 2, 3, 4]` |
| `[1, 1, 1, 1]` | `[1]` |
| `[1, 2, 3, 4]` | `[1, 2, 3, 4]` |
| `[]` | `[]` |
| `[-3, -3, -2, -1, -1]` | `[-3, -2, -1]` |

---

## Learning Objectives

By completing these problems, I aim to practice:

- Iterating through lists using loops.
- Comparing values and maintaining variables.
- Handling positive, negative, and duplicate values.
- Working with edge cases such as empty lists and lists containing identical values.
- Using conditional statements effectively.
- Understanding time and space complexity.
- Applying two-pointer and in-place array manipulation techniques.
- Writing clean, readable, and maintainable Python code.

## Suggested Project Structure

```text
Day-1/
├── README.md
├── largest_number.py
├── second_largest.py
├── move_zeros.py
└── remove_duplicates_sorted_list.py