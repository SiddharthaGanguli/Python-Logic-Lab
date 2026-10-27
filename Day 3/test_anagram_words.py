import itertools
import unittest

from anagram_words import are_anagrams


class AnagramWordsTests(unittest.TestCase):
    def test_case_and_whitespace_are_ignored(self):
        self.assertTrue(are_anagrams("Dormitory", "Dirty room"))
        self.assertTrue(are_anagrams("a\tb\nc", "C\u2003BA"))

    def test_repeated_characters_must_have_matching_counts(self):
        self.assertTrue(are_anagrams("aabb", "baba"))
        self.assertFalse(are_anagrams("aab", "abb"))
        self.assertFalse(are_anagrams("a", "aa"))

    def test_punctuation_and_digits_remain_significant(self):
        self.assertFalse(are_anagrams("ab!", "ba"))
        self.assertTrue(are_anagrams("a1!", "!1A"))

    def test_empty_and_whitespace_only_inputs(self):
        self.assertTrue(are_anagrams("", " \t\n"))
        self.assertFalse(are_anagrams("", "x"))

    def test_unicode_case_folding_without_canonical_normalization(self):
        self.assertTrue(are_anagrams("Straße", "strasse"))
        self.assertFalse(are_anagrams("é", "e\u0301"))

    def test_small_inputs_match_sorted_character_reference(self):
        samples = ["".join(chars) for size in range(3)
                   for chars in itertools.product("aB !", repeat=size)]
        for first in samples:
            for second in samples:
                # Sorting characters gives a separate frequency comparison.
                left = sorted(char for char in first.casefold() if not char.isspace())
                right = sorted(char for char in second.casefold() if not char.isspace())
                self.assertEqual(are_anagrams(first, second), left == right, (first, second))


if __name__ == "__main__":
    unittest.main()
