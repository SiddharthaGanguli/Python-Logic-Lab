"""Find common values in the order they first occur in the first list."""


def unique_intersection(first: list[int], second: list[int]) -> list[int]:
    """Return each shared integer once, without modifying either input.

    Expected O(n + m) time, O(m + k) auxiliary space, and O(k) output
    space, assuming constant-cost integer hashing and set operations.
    """
    available = set(second)
    seen: set[int] = set()
    result: list[int] = []
    for value in first:
        if value in available and value not in seen:
            result.append(value)
            seen.add(value)
    return result


if __name__ == "__main__":
    print(unique_intersection([3, 1, 3, 2, 4], [2, 3, 3]))
