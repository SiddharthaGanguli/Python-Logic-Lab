import unittest
from itertools import product

from balanced_brackets import has_balanced_brackets


def reduced_brackets_are_empty(text):
    """Independent reference: repeatedly remove adjacent matched pairs."""
    remaining = "".join(character for character in text if character in "()[]{}")
    while True:
        reduced = remaining.replace("()", "").replace("[]", "").replace("{}", "")
        if reduced == remaining:
            return remaining == ""
        remaining = reduced


class BalancedBracketsTests(unittest.TestCase):
    def test_empty_and_plain_text(self):
        self.assertTrue(has_balanced_brackets(""))
        self.assertTrue(has_balanced_brackets("hello"))

    def test_nested_and_adjacent_groups(self):
        self.assertTrue(has_balanced_brackets("{[()]}()[]"))
        self.assertTrue(has_balanced_brackets("items[(2 + 3)]"))

    def test_crossed_pairs_are_invalid(self):
        self.assertFalse(has_balanced_brackets("([)]"))

    def test_unmatched_opening_or_closing(self):
        for text in ["(", ")", "][]", "{[()]", "())"]:
            with self.subTest(text=text):
                self.assertFalse(has_balanced_brackets(text))

    def test_brackets_inside_quotes_still_count(self):
        self.assertFalse(has_balanced_brackets('print("(")'))

    def test_matches_pair_reduction_on_short_inputs(self):
        for length in range(5):
            for characters in product("()[]{}", repeat=length):
                text = "".join(characters)
                with self.subTest(text=text):
                    self.assertEqual(has_balanced_brackets(text), reduced_brackets_are_empty(text))


if __name__ == "__main__":
    unittest.main()
