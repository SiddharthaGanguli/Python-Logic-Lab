import itertools
import unittest

from merge_sorted_lists import merge_sorted_lists


class MergeSortedListsTests(unittest.TestCase):
    def test_interleaved_lists_keep_duplicates(self):
        self.assertEqual(
            merge_sorted_lists([1, 3, 5], [2, 3, 6]), [1, 2, 3, 3, 5, 6]
        )

    def test_empty_inputs(self):
        self.assertEqual(merge_sorted_lists([], []), [])
        self.assertEqual(merge_sorted_lists([], [-2, 3]), [-2, 3])
        self.assertEqual(merge_sorted_lists([-2, 3], []), [-2, 3])

    def test_negative_numbers_and_remaining_tail(self):
        self.assertEqual(merge_sorted_lists([-8, -3], [-2, -1, 0]), [-8, -3, -2, -1, 0])
        self.assertEqual(merge_sorted_lists([1, 2, 3], [-1]), [-1, 1, 2, 3])

    def test_inputs_are_unchanged_and_output_is_new(self):
        left, right = [1, 3], [2, 4]
        result = merge_sorted_lists(left, right)
        self.assertIsNot(result, left)
        self.assertIsNot(result, right)
        result.append(99)
        self.assertEqual(left, [1, 3])
        self.assertEqual(right, [2, 4])

    def test_small_sorted_inputs_against_sorting_reference(self):
        inputs = [
            list(values)
            for size in range(5)
            for values in itertools.combinations_with_replacement((-2, 0, 3), size)
        ]
        for left in inputs:
            for right in inputs:
                self.assertEqual(merge_sorted_lists(left, right), sorted(left + right))


if __name__ == "__main__":
    unittest.main()
