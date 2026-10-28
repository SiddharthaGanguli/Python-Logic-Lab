import itertools
import unittest

from fixed_window_sum import maximum_window_sum


class MaximumWindowSumTests(unittest.TestCase):
    def test_best_window_can_be_in_the_middle_or_at_an_end(self):
        self.assertEqual(maximum_window_sum([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(maximum_window_sum([5, 4, -9], 2), 9)
        self.assertEqual(maximum_window_sum([-9, 4, 5], 2), 9)

    def test_negative_inputs_still_require_a_full_window(self):
        self.assertEqual(maximum_window_sum([-8, -3, -6, -2], 2), -8)

    def test_size_one_full_length_and_zero_values(self):
        self.assertEqual(maximum_window_sum([-4, 3, 1], 1), 3)
        self.assertEqual(maximum_window_sum([-4, 3, 1], 3), 0)
        self.assertEqual(maximum_window_sum([0, 0, 0], 2), 0)

    def test_invalid_window_sizes_are_rejected(self):
        for numbers, size in (([], 1), ([], 0), ([1, 2], 0), ([1], -1), ([1], 2)):
            with self.subTest(numbers=numbers, size=size), self.assertRaises(ValueError):
                maximum_window_sum(numbers, size)

    def test_input_is_not_modified(self):
        numbers = [3, -1, 4, 2]
        original = numbers.copy()
        self.assertEqual(maximum_window_sum(numbers, 2), 6)
        self.assertEqual(numbers, original)

    def test_small_inputs_match_independently_summed_windows(self):
        for length in range(1, 7):
            for values in itertools.product((-2, 0, 3), repeat=length):
                numbers = list(values)
                for size in range(1, length + 1):
                    expected = max(sum(numbers[start:start + size])
                                   for start in range(length - size + 1))
                    self.assertEqual(maximum_window_sum(numbers, size), expected,
                                     (numbers, size))


if __name__ == "__main__":
    unittest.main()
