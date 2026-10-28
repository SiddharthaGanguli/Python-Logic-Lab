# Python Logic Lab

Python practice built around clear problem statements, small functions, and
executable checks. Start with the question, trace an example by hand, and then
compare your approach with the reference solution.

## Practice collection

[Day 1](Day%201/Problems.md) contains the original list exercises: largest
number, second-largest number, moving zeros, and removing sorted duplicates.

Additional exercises: **30**. Each includes requirements, expected examples,
an explained solution, and a separate test file. Day labels organize topics;
they do not impose a daily schedule.

| Day | Topic | Question |
|---|---|---|
| 2 | Lists and searching | [Rotate a list to the right](Day%202/Problems.md#1-rotate-a-list-to-the-right) |
| 2 | Lists and searching | [Merge two sorted lists](Day%202/Problems.md#2-merge-two-sorted-lists) |
| 2 | Lists and searching | [Find the missing number](Day%202/Problems.md#3-find-the-missing-number) |
| 2 | Lists and searching | [Find two indices with a target sum](Day%202/Problems.md#4-find-two-indices-with-a-target-sum) |
| 2 | Lists and searching | [Find the maximum contiguous subarray sum](Day%202/Problems.md#5-find-the-maximum-contiguous-subarray-sum) |
| 3 | String reasoning | [Check a normalized palindrome](Day%203/Problems.md#1-check-a-normalized-palindrome) |
| 3 | String reasoning | [Compare words as anagrams](Day%203/Problems.md#2-compare-words-as-anagrams) |
| 3 | String reasoning | [Find the first unique character](Day%203/Problems.md#3-find-the-first-unique-character) |
| 3 | String reasoning | [Encode consecutive character runs](Day%203/Problems.md#4-encode-consecutive-character-runs) |
| 3 | String reasoning | [Find the longest common prefix](Day%203/Problems.md#5-find-the-longest-common-prefix) |
| 4 | Number logic | [Check whether a number is prime](Day%204/Problems.md#1-check-whether-a-number-is-prime) |
| 4 | Number logic | [Find the greatest common divisor](Day%204/Problems.md#2-find-the-greatest-common-divisor) |
| 4 | Number logic | [Convert a decimal integer to binary](Day%204/Problems.md#3-convert-a-decimal-integer-to-binary) |
| 4 | Number logic | [Find the integer square root](Day%204/Problems.md#4-find-the-integer-square-root) |
| 4 | Number logic | [Generate a Fibonacci sequence](Day%204/Problems.md#5-generate-a-fibonacci-sequence) |
| 5 | Dictionaries, stacks, and structured data | [Count repeated items](Day%205/Problems.md#1-count-repeated-items) |
| 5 | Dictionaries, stacks, and structured data | [Check balanced brackets](Day%205/Problems.md#2-check-balanced-brackets) |
| 5 | Dictionaries, stacks, and structured data | [Find a unique intersection](Day%205/Problems.md#3-find-a-unique-intersection) |
| 5 | Dictionaries, stacks, and structured data | [Transpose a rectangular matrix](Day%205/Problems.md#4-transpose-a-rectangular-matrix) |
| 5 | Dictionaries, stacks, and structured data | [Count subarrays with a target sum](Day%205/Problems.md#5-count-subarrays-with-a-target-sum) |
| 6 | Recursion and backtracking | [Generate balanced parentheses](Day%206/Problems.md#1-generate-balanced-parentheses) |
| 6 | Recursion and backtracking | [Generate every subset](Day%206/Problems.md#2-generate-every-subset) |
| 6 | Recursion and backtracking | [Generate unique permutations](Day%206/Problems.md#3-generate-unique-permutations) |
| 6 | Recursion and backtracking | [Build combinations with a target sum](Day%206/Problems.md#4-build-combinations-with-a-target-sum) |
| 6 | Recursion and backtracking | [Search for a word in a grid](Day%206/Problems.md#5-search-for-a-word-in-a-grid) |
| 7 | Searching and ordering | [Find a lower-bound insertion index](Day%207/Problems.md#1-find-a-lower-bound-insertion-index) |
| 7 | Searching and ordering | [Search a rotated sorted list](Day%207/Problems.md#2-search-a-rotated-sorted-list) |
| 7 | Searching and ordering | [Merge overlapping intervals](Day%207/Problems.md#3-merge-overlapping-intervals) |
| 7 | Searching and ordering | [Count inversions without changing the list](Day%207/Problems.md#4-count-inversions-without-changing-the-list) |
| 8 | Windows and dynamic programming | [Find the longest substring with distinct characters](Day%208/Problems.md#1-find-the-longest-substring-with-distinct-characters) |

## Run a solution

Use Python 3.10 or newer. The new exercises use only the standard library.
From the repository root:

```sh
python "Day 2/rotate_list.py"
```

Each solution has a runnable example and can also be imported without printing
or running its example automatically.

## Run the tests

Run each day's suite from the repository root:

```sh
python -B -m unittest discover -s "Day 2" -v
python -B -m unittest discover -s "Day 3" -v
python -B -m unittest discover -s "Day 4" -v
python -B -m unittest discover -s "Day 5" -v
python -B -m unittest discover -s "Day 6" -v
python -B -m unittest discover -s "Day 7" -v
python -B -m unittest discover -s "Day 8" -v
```

These suites cover the additional exercises listed above. Tests check boundary
cases, input preservation where required, and results against independent
reference implementations. Original Day 1 scripts are outside these suites.

## Working through a question

1. Read the input contract, including empty-input and error behavior.
2. Write down an expected result before running your code.
3. Compare your reasoning with the solution and its complexity notes.
4. Add a boundary case and run the relevant test file or day suite.

Unless a question says otherwise, inputs follow its documented types. Complexity
uses the standard unit-cost arithmetic and expected hash-table model; operations
on very large Python integers can cost more than a single machine operation.

## License

[Apache License 2.0](LICENSE)
