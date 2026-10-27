"""Find the missing value in a shuffled range from zero to n."""


def missing_number(numbers: list[int]) -> int:
    """Return the one missing value from 0 through len(numbers), inclusive.

    Input contains distinct integers in that range with exactly one missing.
    These preconditions are assumed rather than validated. Input is unchanged.
    Time: O(n). Auxiliary space: O(1) under the usual unit-cost integer model.
    """
    size = len(numbers)
    missing = size * (size + 1) // 2
    for number in numbers:
        missing -= number
    return missing


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))
