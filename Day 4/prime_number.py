"""Decide whether an integer is prime using trial division."""


def is_prime(number: int) -> bool:
    """Return whether number has exactly two positive divisors.

    Integers below 2 are not prime. Only odd candidate divisors are checked
    after handling 2, and the stopping condition uses integer arithmetic.
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor <= number // divisor:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


if __name__ == "__main__":
    for example in (-7, 1, 2, 29, 49):
        print(f"{example}: {is_prime(example)}")
