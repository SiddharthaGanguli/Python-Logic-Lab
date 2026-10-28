"""Find the best sum among windows of exactly the requested size."""


def maximum_window_sum(numbers: list[int], size: int) -> int:
    """Return the largest sum of exactly size consecutive integers.

    Inputs are a list of integers and an integer size. Raise ValueError when
    size is outside 1 through len(numbers), inclusive. Do not modify numbers.
    Time: O(n). Extra space: O(1).
    """
    if size <= 0 or size > len(numbers):
        raise ValueError("size must be between 1 and the list length")

    window_sum = 0
    for index in range(size):
        window_sum += numbers[index]
    best = window_sum

    for right in range(size, len(numbers)):
        window_sum += numbers[right] - numbers[right - size]
        best = max(best, window_sum)
    return best


if __name__ == "__main__":
    print(maximum_window_sum([2, 1, 5, 1, 3, 2], 3))
