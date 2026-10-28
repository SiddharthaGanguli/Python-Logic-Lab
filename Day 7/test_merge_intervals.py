import itertools
import unittest

from merge_intervals import merge_intervals


def covered_half_steps(intervals):
    """Sample integer and half-integer positions for small integer endpoints."""
    return {
        point
        for start, end in intervals
        for point in range(2 * start, 2 * end + 1)
    }


class MergeIntervalsTests(unittest.TestCase):
    def test_unsorted_overlapping_and_touching_intervals(self):
        self.assertEqual(
            merge_intervals([(8, 10), (1, 3), (2, 6), (10, 12)]),
            [(1, 6), (8, 12)],
        )

    def test_nested_duplicate_and_zero_length_intervals(self):
        self.assertEqual(
            merge_intervals([(1, 8), (2, 3), (1, 8), (8, 8)]),
            [(1, 8)],
        )
        self.assertEqual(merge_intervals([(2, 2), (1, 1)]), [(1, 1), (2, 2)])

    def test_empty_and_disjoint_negative_intervals(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([(-2, -1), (-5, -3)]), [(-5, -3), (-2, -1)])

    def test_rejects_reversed_interval_without_mutating_input(self):
        intervals = [(5, 7), (3, 1), (0, 2)]
        original = intervals.copy()
        with self.assertRaises(ValueError):
            merge_intervals(intervals)
        self.assertEqual(intervals, original)

    def test_returns_new_tuples_and_preserves_input_order(self):
        intervals = [(5, 8), (1, 2)]
        original = intervals.copy()
        result = merge_intervals(intervals)
        self.assertEqual(intervals, original)
        self.assertIsNot(result, intervals)
        self.assertEqual(result, [(1, 2), (5, 8)])
        self.assertIsNot(result[0], intervals[1])
        self.assertIsNot(result[1], intervals[0])

    def test_small_interval_sets_preserve_coverage_and_have_no_mergeable_pairs(self):
        choices = [(start, end) for start in range(-2, 3) for end in range(start, 3)]
        for size in range(4):
            for values in itertools.combinations_with_replacement(choices, size):
                intervals = list(reversed(values))
                result = merge_intervals(intervals)
                with self.subTest(intervals=intervals):
                    self.assertEqual(covered_half_steps(result), covered_half_steps(intervals))
                    self.assertTrue(all(start <= end for start, end in result))
                    self.assertTrue(
                        all(left[1] < right[0] for left, right in zip(result, result[1:]))
                    )


if __name__ == "__main__":
    unittest.main()
