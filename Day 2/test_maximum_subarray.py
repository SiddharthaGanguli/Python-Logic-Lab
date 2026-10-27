import itertools
import unittest

from maximum_subarray import maximum_subarray_sum


def reference_maximum(numbers):
    if not numbers:
        return None
    return max(
        sum(numbers[start:end])
        for start in range(len(numbers))
        for end in range(start + 1, len(numbers) + 1)
    )


class MaximumSubarrayTests(unittest.TestCase):
    def test_best_sum_can_be_in_the_middle(self):
        self.assertEqual(maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_all_negative_input_uses_a_nonempty_subarray(self):
        self.assertEqual(maximum_subarray_sum([-8, -3, -6, -2, -5]), -2)

    def test_empty_singleton_zeros_and_all_positive(self):
        self.assertIsNone(maximum_subarray_sum([]))
        self.assertEqual(maximum_subarray_sum([-4]), -4)
        self.assertEqual(maximum_subarray_sum([0, 0]), 0)
        self.assertEqual(maximum_subarray_sum([1, 2, 3]), 6)

    def test_input_is_unchanged(self):
        numbers = [2, -1, 3]
        self.assertEqual(maximum_subarray_sum(numbers), 4)
        self.assertEqual(numbers, [2, -1, 3])

    def test_small_inputs_against_all_contiguous_subarrays(self):
        for size in range(7):
            for values in itertools.product((-2, 0, 3), repeat=size):
                numbers = list(values)
                self.assertEqual(maximum_subarray_sum(numbers), reference_maximum(numbers))


if __name__ == "__main__":
    unittest.main()
