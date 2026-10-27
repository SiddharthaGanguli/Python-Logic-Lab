import itertools
import unittest

from longest_common_prefix import longest_common_prefix


class LongestCommonPrefixTests(unittest.TestCase):
    def test_shared_prefix_and_no_shared_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_empty_list_and_empty_member(self):
        self.assertEqual(longest_common_prefix([]), "")
        self.assertEqual(longest_common_prefix(["abc", ""]), "")

    def test_single_word_and_word_that_is_entire_prefix(self):
        self.assertEqual(longest_common_prefix(["solo"]), "solo")
        self.assertEqual(longest_common_prefix(["carpet", "car", "cart"]), "car")

    def test_case_whitespace_and_unicode_are_literal(self):
        self.assertEqual(longest_common_prefix(["Apple", "apple"]), "")
        self.assertEqual(longest_common_prefix(["  one", "  two"]), "  ")
        self.assertEqual(longest_common_prefix(["école", "écran"]), "éc")

    def test_input_list_is_not_modified(self):
        words = ["prefix", "present", "prevent"]
        original = words.copy()
        self.assertEqual(longest_common_prefix(words), "pre")
        self.assertEqual(words, original)

    def test_small_inputs_match_prefix_enumeration_reference(self):
        choices = ["", "a", "b", "aa", "ab", "ba"]
        for count in range(4):
            for values in itertools.product(choices, repeat=count):
                words = list(values)
                candidates = [""] if not words else [words[0][:size] for size in range(len(words[0]) + 1)]
                expected = max((prefix for prefix in candidates if all(word.startswith(prefix) for word in words)), key=len)
                self.assertEqual(longest_common_prefix(words), expected, words)


if __name__ == "__main__":
    unittest.main()
