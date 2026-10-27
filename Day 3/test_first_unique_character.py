import itertools
import unittest

from first_unique_character import first_unique_character


class FirstUniqueCharacterTests(unittest.TestCase):
    def test_returns_the_earliest_unique_character(self):
        self.assertEqual(first_unique_character("swiss"), "w")
        self.assertEqual(first_unique_character("abac"), "b")

    def test_no_unique_character(self):
        self.assertIsNone(first_unique_character(""))
        self.assertIsNone(first_unique_character("aabbcc"))

    def test_case_and_whitespace_are_significant(self):
        self.assertEqual(first_unique_character("aA"), "a")
        self.assertEqual(first_unique_character("aa bb"), " ")

    def test_unicode_characters_and_single_character(self):
        self.assertEqual(first_unique_character("🙂🙃🙂"), "🙃")
        self.assertEqual(first_unique_character("z"), "z")

    def test_small_inputs_match_counting_reference(self):
        for length in range(7):
            for letters in itertools.product("abc", repeat=length):
                text = "".join(letters)
                expected = next((char for char in text if text.count(char) == 1), None)
                self.assertEqual(first_unique_character(text), expected, text)


if __name__ == "__main__":
    unittest.main()
