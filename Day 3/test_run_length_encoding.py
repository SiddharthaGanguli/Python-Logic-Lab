import itertools
import unittest

from run_length_encoding import encode_runs


class RunLengthEncodingTests(unittest.TestCase):
    def test_separate_runs_keep_their_order(self):
        self.assertEqual(encode_runs("aaabbcaa"), [("a", 3), ("b", 2), ("c", 1), ("a", 2)])

    def test_empty_single_character_and_one_long_run(self):
        self.assertEqual(encode_runs(""), [])
        self.assertEqual(encode_runs("x"), [("x", 1)])
        self.assertEqual(encode_runs("z" * 100), [("z", 100)])

    def test_digits_spaces_and_case_are_preserved(self):
        self.assertEqual(encode_runs("11122  Aaa"), [("1", 3), ("2", 2), (" ", 2), ("A", 1), ("a", 2)])

    def test_unicode_characters(self):
        self.assertEqual(encode_runs("🙂🙂🙃"), [("🙂", 2), ("🙃", 1)])

    def test_small_inputs_round_trip_into_maximal_runs(self):
        for length in range(8):
            for letters in itertools.product("ab", repeat=length):
                text = "".join(letters)
                runs = encode_runs(text)
                self.assertEqual("".join(char * count for char, count in runs), text)
                self.assertTrue(all(count > 0 for _, count in runs))
                self.assertTrue(all(left[0] != right[0] for left, right in zip(runs, runs[1:])))


if __name__ == "__main__":
    unittest.main()
