"""Represent consecutive character runs without ambiguous digit encoding."""


def encode_runs(text: str) -> list[tuple[str, int]]:
    """Return (character, count) pairs for consecutive runs; empty input gives [].

    Characters are case-sensitive Unicode code points. Spaces and digits are
    retained, and repeated characters in separate runs are not combined.
    """
    if not text:
        return []

    runs: list[tuple[str, int]] = []
    previous = text[0]
    count = 1
    for index in range(1, len(text)):
        character = text[index]
        if character == previous:
            count += 1
        else:
            runs.append((previous, count))
            previous = character
            count = 1
    runs.append((previous, count))
    return runs


if __name__ == "__main__":
    print(encode_runs("aaabbcaa"))
