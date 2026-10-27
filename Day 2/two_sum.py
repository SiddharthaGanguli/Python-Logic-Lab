"""Find indices of two distinct elements whose sum equals a target."""


def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return a pair of indices, or None when no pair exists.

    Prefer the smallest second index, then the smallest first index. Search
    left to right and retain the earliest index for each value. The input is
    unchanged. Expected time: O(n). Auxiliary space: O(n).
    """
    first_index = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in first_index:
            return first_index[complement], index
        if number not in first_index:
            first_index[number] = index
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
