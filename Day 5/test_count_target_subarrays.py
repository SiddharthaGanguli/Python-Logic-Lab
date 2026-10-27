import unittest
from itertools import product

from count_target_subarrays import count_target_subarrays


def count_by_enumeration(numbers, target):
    return sum(
        sum(numbers[start:stop]) == target
        for start in range(len(numbers))
        for stop in range(start + 1, len(numbers) + 1)
    )


class CountTargetSubarraysTests(unittest.TestCase):
    def test_empty_input_excludes_empty_subarrays(self):
        self.assertEqual(count_target_subarrays([], 0), 0)

    def test_overlapping_matches(self):
        self.assertEqual(count_target_subarrays([1, 2, 1, 2], 3), 3)

    def test_negative_numbers_and_zero(self):
        self.assertEqual(count_target_subarrays([1, -1, 0], 0), 3)
        self.assertEqual(count_target_subarrays([-2, -1, 2], -3), 1)

    def test_all_zeros(self):
        self.assertEqual(count_target_subarrays([0] * 8, 0), 36)

    def test_no_match(self):
        self.assertEqual(count_target_subarrays([2, 4], 3), 0)

    def test_input_is_preserved(self):
        numbers = [1, -1, 0]
        count_target_subarrays(numbers, 0)
        self.assertEqual(numbers, [1, -1, 0])

    def test_matches_brute_force_on_small_arrays(self):
        for length in range(6):
            for values in product([-1, 0, 1], repeat=length):
                for target in range(-2, 3):
                    with self.subTest(values=values, target=target):
                        self.assertEqual(count_target_subarrays(list(values), target), count_by_enumeration(values, target))


if __name__ == "__main__":
    unittest.main()
