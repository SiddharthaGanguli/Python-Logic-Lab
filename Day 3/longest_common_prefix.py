"""Find the prefix shared by every string in a list."""


def longest_common_prefix(words: list[str]) -> str:
    """Return the longest case-sensitive common prefix, or '' for an empty list.

    An empty member also produces ''. No whitespace stripping or Unicode
    normalization is performed, and the input list is not modified.
    """
    if not words:
        return ""

    first = words[0]
    prefix_length = len(first)
    for word in words:
        limit = min(prefix_length, len(word))
        index = 0
        while index < limit and first[index] == word[index]:
            index += 1
        prefix_length = index
        if prefix_length == 0:
            return ""
    return first[:prefix_length]


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
