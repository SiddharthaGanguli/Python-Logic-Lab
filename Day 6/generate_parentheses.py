"""Generate every properly balanced sequence of a chosen number of parentheses."""


def generate_parentheses(pairs: int) -> list[str]:
    """Return balanced parentheses strings in lexicographic order.

    ``pairs`` must be nonnegative. The function has no side effects and can be
    safely imported by tests or other programs.
    """
    if pairs < 0:
        raise ValueError("pairs must be nonnegative")

    results: list[str] = []
    current: list[str] = []

    def build(opened: int, closed: int) -> None:
        if len(current) == pairs * 2:
            results.append("".join(current))
            return

        if opened < pairs:
            current.append("(")
            build(opened + 1, closed)
            current.pop()

        if closed < opened:
            current.append(")")
            build(opened, closed + 1)
            current.pop()

    build(0, 0)
    return results


if __name__ == "__main__":
    print(generate_parentheses(3))
