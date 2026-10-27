"""Generate Fibonacci values with two running state variables."""


def fibonacci_sequence(count: int) -> list[int]:
    """Return count Fibonacci values, starting at 0, 1.

    Zero requests an empty list. A negative count raises ValueError.
    """
    if count < 0:
        raise ValueError("count must be nonnegative")

    values = []
    current, following = 0, 1
    for _ in range(count):
        values.append(current)
        current, following = following, current + following
    return values


if __name__ == "__main__":
    print(fibonacci_sequence(10))
