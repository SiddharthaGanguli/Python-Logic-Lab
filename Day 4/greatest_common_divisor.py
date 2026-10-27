"""Find the greatest common divisor with Euclid's algorithm."""


def gcd(first: int, second: int) -> int:
    """Return the nonnegative greatest common divisor of two integers.

    Negative inputs are treated by magnitude. gcd(0, 0) is defined as 0.
    """
    first, second = abs(first), abs(second)
    while second:
        first, second = second, first % second
    return first


if __name__ == "__main__":
    print(gcd(48, 18))
    print(gcd(-24, 36))
    print(gcd(0, 0))
