"""Build a binary representation by repeated division."""


def decimal_to_binary(number: int) -> str:
    """Return the base-two digits of a nonnegative integer.

    The result has no prefix or unnecessary leading zeroes. Zero becomes
    "0". Negative integers raise ValueError.
    """
    if number < 0:
        raise ValueError("number must be nonnegative")
    if number == 0:
        return "0"

    digits = []
    while number:
        number, remainder = divmod(number, 2)
        digits.append(str(remainder))
    digits.reverse()
    return "".join(digits)


if __name__ == "__main__":
    for example in (0, 1, 10, 42):
        print(f"{example}: {decimal_to_binary(example)}")
