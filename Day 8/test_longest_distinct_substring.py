import itertools
import unittest

from longest_distinct_substring import longest_distinct_substring


def reference_length(text):
    longest = 0
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            candidate = text[start:end]
            if len(set(candidate)) == len(candidate):
                longest = max(longest, len(candidate))
    return longest


class LongestDistinctSubstringTests(unittest.TestCase):
    def test_repeated_characters_shrink_the_window(self):
        self.assertEqual(longest_distinct_substring("abcabcbb"), 3)
        self.assertEqual(longest_distinct_substring("pwwkew"), 3)

    def test_old_duplicates_cannot_move_the_left_boundary_backwards(self):
        self.assertEqual(longest_distinct_substring("abba"), 2)
        self.assertEqual(longest_distinct_substring("tmmzuxt"), 5)

    def test_empty_single_and_identical_characters(self):
        self.assertEqual(longest_distinct_substring(""), 0)
        self.assertEqual(longest_distinct_substring("x"), 1)
        self.assertEqual(longest_distinct_substring("zzzzz"), 1)

    def test_case_spaces_and_unicode_code_points_are_significant(self):
        self.assertEqual(longest_distinct_substring("aA a"), 3)
        self.assertEqual(longest_distinct_substring("🙂🙃🙂a"), 3)
        self.assertEqual(longest_distinct_substring("e\u0301"), 2)

    def test_small_inputs_match_substring_enumeration(self):
        for size in range(7):
            for characters in itertools.product("abc", repeat=size):
                text = "".join(characters)
                self.assertEqual(longest_distinct_substring(text), reference_length(text), text)


if __name__ == "__main__":
    unittest.main()
