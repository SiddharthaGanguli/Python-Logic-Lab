"""Check a palindrome after case folding and alphanumeric filtering."""


def is_palindrome(text: str) -> bool:
    """Ignore case and non-alphanumeric characters; empty text is a palindrome.

    Case folding happens before Unicode alphanumeric filtering. No additional
    Unicode normalization is applied. The input string is not changed.
    """
    normalized = "".join(character for character in text.casefold() if character.isalnum())
    left = 0
    right = len(normalized) - 1

    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama!"))
