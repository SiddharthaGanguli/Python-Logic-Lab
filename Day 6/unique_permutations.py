"""Generate distinct permutations using remaining counts for each value."""


def unique_permutations(numbers: list[int]) -> list[list[int]]:
    """Return unique permutations in lexicographic order, preserving input.

    Repeated values are allowed; empty input returns [[]]. A count table
    avoids generating identical branches for different copies of a value.
    The working path, count table, and recursion use O(n) auxiliary space.
    """
    remaining: dict[int, int] = {}
    for number in numbers:
        remaining[number] = remaining.get(number, 0) + 1
    choices = sorted(remaining)
    results: list[list[int]] = []
    current: list[int] = []

    def build() -> None:
        if len(current) == len(numbers):
            results.append(current.copy())
            return
        for number in choices:
            if remaining[number] == 0:
                continue
            remaining[number] -= 1
            current.append(number)
            build()
            current.pop()
            remaining[number] += 1

    build()
    return results


if __name__ == "__main__":
    print(unique_permutations([2, 1, 1]))
