import bisect
import itertools
import unittest

from lower_bound import lower_bound


class LowerBoundTests(unittest.TestCase):
    def test_empty_and_single_element_lists(self):
        self.assertEqual(lower_bound([], 4), 0)
        self.assertEqual(lower_bound([4], 3), 0)
        self.assertEqual(lower_bound([4], 4), 0)
        self.assertEqual(lower_bound([4], 5), 1)

    def test_duplicate_values_return_the_first_boundary(self):
        self.assertEqual(lower_bound([1, 3, 3, 3, 7], 3), 1)
        self.assertEqual(lower_bound([5, 5, 5], 5), 0)
        self.assertEqual(lower_bound([5, 5, 5], 6), 3)

    def test_target_between_values_or_outside_the_list(self):
        numbers = [-8, -3, 0, 4]
        self.assertEqual(lower_bound(numbers, -9), 0)
        self.assertEqual(lower_bound(numbers, -2), 2)
        self.assertEqual(lower_bound(numbers, 9), 4)

    def test_input_list_is_not_modified(self):
        numbers = [-4, 0, 0, 6]
        original = numbers.copy()
        self.assertEqual(lower_bound(numbers, 0), 1)
        self.assertEqual(numbers, original)

    def test_small_sorted_lists_match_bisect_and_partition_contract(self):
        for length in range(6):
            for values in itertools.combinations_with_replacement(range(-2, 3), length):
                numbers = list(values)
                for target in range(-3, 4):
                    with self.subTest(numbers=numbers, target=target):
                        result = lower_bound(numbers, target)
                        self.assertEqual(result, bisect.bisect_left(numbers, target))
                        self.assertTrue(all(value < target for value in numbers[:result]))
                        self.assertTrue(all(value >= target for value in numbers[result:]))


if __name__ == "__main__":
    unittest.main()
