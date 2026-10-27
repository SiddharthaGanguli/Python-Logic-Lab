import itertools
import unittest

from two_sum import two_sum


def reference_pair(numbers, target):
    for second in range(len(numbers)):
        for first in range(second):
            if numbers[first] + numbers[second] == target:
                return first, second
    return None


class TwoSumTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))

    def test_duplicates_use_distinct_indices(self):
        self.assertEqual(two_sum([3, 3], 6), (0, 1))
        self.assertIsNone(two_sum([3], 6))

    def test_pair_selection_is_deterministic(self):
        self.assertEqual(two_sum([1, 1, 4, 2, 3], 5), (0, 2))
        self.assertEqual(two_sum([1, 2, 3, 4], 5), (1, 2))

    def test_negatives_zero_and_no_solution(self):
        self.assertEqual(two_sum([-4, 0, 4], 0), (0, 2))
        self.assertEqual(two_sum([0, 0], 0), (0, 1))
        self.assertIsNone(two_sum([], 0))
        self.assertIsNone(two_sum([1, 2, 3], 9))

    def test_input_is_unchanged(self):
        numbers = [4, -1, 2, 4]
        self.assertEqual(two_sum(numbers, 3), (0, 1))
        self.assertEqual(numbers, [4, -1, 2, 4])

    def test_small_inputs_against_pair_enumeration(self):
        for size in range(6):
            for values in itertools.product((-2, 0, 2), repeat=size):
                numbers = list(values)
                for target in range(-4, 5):
                    self.assertEqual(two_sum(numbers, target), reference_pair(numbers, target))


if __name__ == "__main__":
    unittest.main()
