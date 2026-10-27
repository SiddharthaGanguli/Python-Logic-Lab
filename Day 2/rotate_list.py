"""Rotate a list to the right without changing the original list."""


def rotate_right(numbers: list[int], steps: int) -> list[int]:
    """Return a new list rotated right by a nonnegative number of steps.

    Empty input produces a new empty list. Negative steps raise ValueError.
    Time: O(n). Auxiliary space: O(1), excluding the O(n) result.
    """
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    if not numbers:
        return []

    size = len(numbers)
    shift = steps % size
    return [numbers[(index - shift) % size] for index in range(size)]


if __name__ == "__main__":
    print(rotate_right([1, 2, 3, 4, 5], 2))
