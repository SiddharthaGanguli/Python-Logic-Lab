"""Find the length of a strictly increasing, possibly noncontiguous subsequence."""


def lis_length(numbers: list[int]) -> int:
    """Return the longest strictly increasing subsequence length; [] gives zero.

    A subsequence keeps original index order but may skip elements. Equal
    values cannot extend it. Input is unchanged. Time: O(n squared).
    Extra space: O(n) for the best length ending at each index.
    """
    if not numbers:
        return 0

    ending_at = [1] * len(numbers)
    for current in range(len(numbers)):
        for previous in range(current):
            if numbers[previous] < numbers[current]:
                ending_at[current] = max(ending_at[current], ending_at[previous] + 1)
    return max(ending_at)


if __name__ == "__main__":
    print(lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
