import itertools
import unittest

from combination_sum import combination_sum


def combinations_by_counts(candidates, target):
    """Reference: enumerate multiplicities, rather than extending a path."""
    choices = sorted(set(candidates))
    results = []
    for counts in itertools.product(*(range(target // value + 1) for value in choices)):
        if sum(value * count for value, count in zip(choices, counts)) == target:
            results.append([value for value, count in zip(choices, counts) for _ in range(count)])
    return sorted(results)


class CombinationSumTests(unittest.TestCase):
    def test_example_uses_candidates_repeatedly(self):
        self.assertEqual(combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_candidates_are_deduplicated_and_results_are_lexicographic(self):
        self.assertEqual(
            combination_sum([5, 3, 2, 2], 8),
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        )

    def test_zero_target_has_one_empty_combination(self):
        self.assertEqual(combination_sum([], 0), [[]])
        self.assertEqual(combination_sum([2, 3], 0), [[]])

    def test_empty_candidates_and_unreachable_target(self):
        self.assertEqual(combination_sum([], 3), [])
        self.assertEqual(combination_sum([2, 4], 3), [])
        self.assertEqual(combination_sum([6, 7], 4), [])

    def test_rejects_negative_target(self):
        with self.assertRaises(ValueError):
            combination_sum([1, 2], -1)

    def test_rejects_nonpositive_candidates_even_when_target_is_zero(self):
        for candidates in ([0], [-1], [2, 0], [1, -3]):
            for target in (0, 4):
                with self.subTest(candidates=candidates, target=target), self.assertRaises(ValueError):
                    combination_sum(candidates, target)

    def test_input_and_output_lists_are_independent(self):
        candidates = [3, 2, 2]
        results = combination_sum(candidates, 6)
        self.assertEqual(results, [[2, 2, 2], [3, 3]])
        results[0].append(99)
        self.assertEqual(results[1], [3, 3])
        self.assertEqual(candidates, [3, 2, 2])

    def test_matches_exhaustive_multiplicity_reference(self):
        for size in range(4):
            for candidates in itertools.product((1, 2, 4), repeat=size):
                for target in range(9):
                    self.assertEqual(
                        combination_sum(list(candidates), target),
                        combinations_by_counts(candidates, target),
                    )


if __name__ == "__main__":
    unittest.main()
