import unittest
from collections import Counter
from itertools import product

from count_frequencies import count_frequencies


class CountFrequenciesTests(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(count_frequencies([]), {})

    def test_repeated_items(self):
        self.assertEqual(
            count_frequencies(["red", "blue", "red", "green", "blue"]),
            {"red": 2, "blue": 2, "green": 1},
        )

    def test_case_and_empty_string_are_significant(self):
        self.assertEqual(count_frequencies(["A", "a", "", ""]), {"A": 1, "a": 1, "": 2})

    def test_first_appearance_order(self):
        self.assertEqual(list(count_frequencies(["b", "a", "b", "c"])), ["b", "a", "c"])

    def test_input_is_preserved(self):
        items = ["b", "a", "b"]
        count_frequencies(items)
        self.assertEqual(items, ["b", "a", "b"])

    def test_matches_counter_on_small_inputs(self):
        for length in range(5):
            for values in product(["a", "b", ""], repeat=length):
                with self.subTest(values=values):
                    self.assertEqual(count_frequencies(list(values)), dict(Counter(values)))


if __name__ == "__main__":
    unittest.main()
