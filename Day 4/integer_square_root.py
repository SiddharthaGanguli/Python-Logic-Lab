"""Find a floor square root without using floating-point arithmetic."""


def integer_square_root(number: int) -> int:
    """Return the largest integer root such that root * root <= number.

    number must be a nonnegative integer. Negative values raise ValueError.
    """
    if number < 0:
        raise ValueError("number must be nonnegative")

    low, high = 0, number
    answer = 0
    while low <= high:
        middle = (low + high) // 2
        if middle * middle <= number:
            answer = middle
            low = middle + 1
        else:
            high = middle - 1
    return answer


if __name__ == "__main__":
    for example in (0, 1, 8, 16, 26):
        print(f"{example}: {integer_square_root(example)}")
