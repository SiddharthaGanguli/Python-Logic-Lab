"""Find the first character that appears exactly once."""


def first_unique_character(text: str) -> str | None:
    """Return the earliest unique character, or None if there is none.

    Matching is case-sensitive. Spaces, punctuation, and Unicode code points
    count as ordinary characters; no filtering or normalization is performed.
    """
    counts: dict[str, int] = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    for character in text:
        if counts[character] == 1:
            return character
    return None


if __name__ == "__main__":
    print(first_unique_character("swiss"))
