"""Find the largest sum among nonempty contiguous subarrays."""


def maximum_subarray_sum(numbers: list[int]) -> int | None:
    """Return the maximum contiguous sum, or None for an empty list.

    A chosen subarray must contain at least one element, so all-negative
    input returns its largest element rather than zero. Input is unchanged.
    Time: O(n). Auxiliary space: O(1).
    """
    if not numbers:
        return None

    ending_here = numbers[0]
    best = numbers[0]
    for index in range(1, len(numbers)):
        number = numbers[index]
        ending_here = max(number, ending_here + number)
        best = max(best, ending_here)
    return best


if __name__ == "__main__":
    print(maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
