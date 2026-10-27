import itertools
import unittest

from palindrome_text import is_palindrome


class PalindromeTextTests(unittest.TestCase):
    def test_sentence_ignores_case_spaces_and_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(is_palindrome("Python is fun"))

    def test_empty_normalized_text_and_single_character(self):
        for text in ("", "... \t!", "x"):
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_digits_participate_in_comparison(self):
        self.assertTrue(is_palindrome("1,2,3,2,1"))
        self.assertFalse(is_palindrome("1a2"))

    def test_unicode_case_folding_and_alphanumeric_filtering(self):
        self.assertTrue(is_palindrome("Àbà"))
        self.assertTrue(is_palindrome("ßaSS"))
        self.assertTrue(is_palindrome("İ"))
        self.assertFalse(is_palindrome("éaE"))

    def test_small_inputs_match_reversal_reference(self):
        for length in range(5):
            for letters in itertools.product("aB1!", repeat=length):
                text = "".join(letters)
                cleaned = "".join(filter(str.isalnum, text.casefold()))
                self.assertEqual(is_palindrome(text), cleaned == cleaned[::-1], text)


if __name__ == "__main__":
    unittest.main()
