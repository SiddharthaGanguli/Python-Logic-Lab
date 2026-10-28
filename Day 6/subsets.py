"""Enumerate subsets by extending a path through later input positions."""


def subsets(numbers: list[int]) -> list[list[int]]:
    """Return subsets in backtracking preorder without changing the input.

    Assume the input integers are distinct. Emit the empty subset first;
    within each subset, preserve input order. Each returned list is new.
    Time/output: O(n * 2**n) for n > 0. Auxiliary space/depth: O(n).
    """
    results: list[list[int]] = []
    current: list[int] = []

    def extend(start: int) -> None:
        results.append(current.copy())
        for index in range(start, len(numbers)):
            current.append(numbers[index])
            extend(index + 1)
            current.pop()

    extend(0)
    return results


if __name__ == "__main__":
    print(subsets([3, 1, 2]))
