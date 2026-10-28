import itertools
import unittest

from longest_increasing_subsequence import lis_length


def reference_length(numbers):
    longest = 0
    for length in range(len(numbers) + 1):
        for indices in itertools.combinations(range(len(numbers)), length):
            values = [numbers[index] for index in indices]
            if all(left < right for left, right in zip(values, values[1:])):
                longest = max(longest, length)
    return longest


class LongestIncreasingSubsequenceTests(unittest.TestCase):
    def test_subsequence_can_skip_elements(self):
        self.assertEqual(lis_length([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lis_length([1, 4, 2, 3]), 3)

    def test_equal_values_do_not_extend_the_subsequence(self):
        self.assertEqual(lis_length([7, 7, 7]), 1)
        self.assertEqual(lis_length([1, 2, 2, 3]), 3)

    def test_empty_singleton_and_decreasing_inputs(self):
        self.assertEqual(lis_length([]), 0)
        self.assertEqual(lis_length([-4]), 1)
        self.assertEqual(lis_length([5, 4, 3, 2]), 1)

    def test_negative_values_and_already_increasing_inputs(self):
        self.assertEqual(lis_length([-3, -1, -2, 0]), 3)
        self.assertEqual(lis_length([-2, 0, 3, 9]), 4)

    def test_input_is_not_modified(self):
        numbers = [3, 1, 2]
        original = numbers.copy()
        self.assertEqual(lis_length(numbers), 2)
        self.assertEqual(numbers, original)

    def test_small_inputs_match_subsequence_enumeration(self):
        for size in range(7):
            for values in itertools.product((-1, 0, 1), repeat=size):
                numbers = list(values)
                self.assertEqual(lis_length(numbers), reference_length(numbers), numbers)


if __name__ == "__main__":
    unittest.main()
