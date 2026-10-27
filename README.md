# Python Logic Lab

Python practice built around clear problem statements, small functions, and
executable checks. Start with the question, trace an example by hand, and then
compare your approach with the reference solution.

## Practice collection

[Day 1](Day%201/Problems.md) contains the original list exercises: largest
number, second-largest number, moving zeros, and removing sorted duplicates.

Additional exercises: **2**. Each includes requirements, expected examples,
an explained solution, and a separate test file. Day labels organize topics;
they do not impose a daily schedule.

| Day | Topic | Question |
|---|---|---|
| 2 | Lists and searching | [Rotate a list to the right](Day%202/Problems.md#1-rotate-a-list-to-the-right) |
| 2 | Lists and searching | [Merge two sorted lists](Day%202/Problems.md#2-merge-two-sorted-lists) |

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
