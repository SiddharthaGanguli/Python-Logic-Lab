import itertools
import unittest

from count_inversions import count_inversions


class CountInversionsTests(unittest.TestCase):
    def test_example_with_inversions_in_both_halves(self):
        self.assertEqual(count_inversions([2, 4, 1, 3, 5]), 3)
        self.assertEqual(count_inversions([5, 1, 4, 2, 3]), 6)

    def test_empty_singleton_and_sorted_lists(self):
        self.assertEqual(count_inversions([]), 0)
        self.assertEqual(count_inversions([8]), 0)
        self.assertEqual(count_inversions([-4, -1, 0, 2, 2]), 0)

    def test_duplicates_are_not_inversions(self):
        self.assertEqual(count_inversions([7, 7, 7]), 0)
        self.assertEqual(count_inversions([2, 1, 2, 1]), 3)

    def test_descending_list_matches_pair_count(self):
        size = 1000
        numbers = list(range(size, 0, -1))
        self.assertEqual(count_inversions(numbers), size * (size - 1) // 2)

    def test_input_list_is_not_modified(self):
        numbers = [9, -2, 4, 4, 0]
        original = numbers.copy()
        self.assertEqual(count_inversions(numbers), 6)
        self.assertEqual(numbers, original)

    def test_small_lists_match_brute_force_pair_count(self):
        for length in range(7):
            for values in itertools.product((-1, 0, 1), repeat=length):
                numbers = list(values)
                expected = sum(
                    numbers[first] > numbers[second]
                    for first in range(length)
                    for second in range(first + 1, length)
                )
                with self.subTest(numbers=numbers):
                    self.assertEqual(count_inversions(numbers), expected)


if __name__ == "__main__":
    unittest.main()
