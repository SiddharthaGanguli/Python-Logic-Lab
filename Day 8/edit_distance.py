"""Measure Levenshtein distance using only two dynamic-programming rows."""


def edit_distance(first: str, second: str) -> int:
    """Return the minimum unit-cost insertions, deletions, and substitutions.

    Compare Unicode code points case-sensitively, without normalization. A
    transposition is not a separate operation. Time: O(m*n) for nonempty
    strings; empty input is handled directly. Extra space: O(min(m, n) + 1).
    """
    if len(first) < len(second):
        first, second = second, first
    if not second:
        return len(first)

    previous = list(range(len(second) + 1))
    for row, first_character in enumerate(first, start=1):
        current = [row]
        for column, second_character in enumerate(second, start=1):
            deletion = previous[column] + 1
            insertion = current[column - 1] + 1
            substitution = previous[column - 1] + (first_character != second_character)
            current.append(min(deletion, insertion, substitution))
        previous = current
    return previous[-1]


if __name__ == "__main__":
    print(edit_distance("kitten", "sitting"))
