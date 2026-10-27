"""Count string occurrences while keeping the order of first appearance."""


def count_frequencies(items: list[str]) -> dict[str, int]:
    """Return case-sensitive counts without changing the input list.

    Expected O(n) time and O(k) output space for k distinct strings,
    treating dictionary operations and string hashing as constant cost.
    """
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


if __name__ == "__main__":
    print(count_frequencies(["red", "blue", "red", "green", "blue"]))
