"""Compare character frequencies while ignoring case and whitespace."""


def are_anagrams(first: str, second: str) -> bool:
    """Return whether the case-folded, whitespace-free strings are anagrams.

    Punctuation and digits are significant. Unicode whitespace is ignored, but
    canonically equivalent Unicode spellings are not otherwise normalized.
    """
    first = "".join(character for character in first.casefold() if not character.isspace())
    second = "".join(character for character in second.casefold() if not character.isspace())
    if len(first) != len(second):
        return False

    counts: dict[str, int] = {}
    for character in first:
        counts[character] = counts.get(character, 0) + 1
    for character in second:
        if counts.get(character, 0) == 0:
            return False
        counts[character] -= 1
    return True


if __name__ == "__main__":
    print(are_anagrams("Dormitory", "Dirty room"))
