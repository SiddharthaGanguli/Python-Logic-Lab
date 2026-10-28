"""Find an insertion boundary in a sorted list with binary search."""


def lower_bound(numbers: list[int], target: int) -> int:
    """Return the first index whose value is >= target, or len(numbers).

    numbers must already be sorted in ascending order; duplicates are allowed.
    The function does not modify the list or validate its sortedness.
    """
    left, right = 0, len(numbers)
    while left < right:
        middle = (left + right) // 2
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


if __name__ == "__main__":
    print(lower_bound([1, 3, 3, 7], 3))
    print(lower_bound([1, 3, 3, 7], 5))
