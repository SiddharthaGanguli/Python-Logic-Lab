"""Find the longest substring without repeating characters."""


def longest_distinct_substring(text: str) -> int:
    """Return the length of the longest contiguous run of unique code points.

    Matching is case-sensitive, with no filtering or Unicode normalization.
    Empty input returns zero. Expected time: O(n). Extra space: O(u), where
    u is the number of distinct code points in the input.
    """
    last_seen: dict[str, int] = {}
    left = 0
    longest = 0

    for right, character in enumerate(text):
        if character in last_seen:
            left = max(left, last_seen[character] + 1)
        last_seen[character] = right
        longest = max(longest, right - left + 1)
    return longest


if __name__ == "__main__":
    print(longest_distinct_substring("abcabcbb"))
