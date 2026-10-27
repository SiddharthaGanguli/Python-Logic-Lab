"""Validate the nesting of parentheses, square brackets, and braces."""


def has_balanced_brackets(text: str) -> bool:
    """Return whether every bracket closes in the correct order.

    Ignore all characters other than ()[]{}. Empty text is balanced.
    Use O(n) time and O(n) auxiliary space in the worst case.
    """
    matching_open = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in matching_open:
            if not stack or stack.pop() != matching_open[character]:
                return False
    return not stack


if __name__ == "__main__":
    print(has_balanced_brackets("items[(2 + 3)]"))
