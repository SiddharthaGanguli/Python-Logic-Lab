import itertools
import unittest
from collections import Counter

from unique_permutations import unique_permutations


class UniquePermutationsTests(unittest.TestCase):
    def test_duplicates_are_emitted_once_in_sorted_order(self):
        self.assertEqual(
            unique_permutations([2, 1, 1]),
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
        )

    def test_empty_singleton_and_identical_values(self):
        self.assertEqual(unique_permutations([]), [[]])
        self.assertEqual(unique_permutations([-2]), [[-2]])
        self.assertEqual(unique_permutations([4, 4, 4]), [[4, 4, 4]])

    def test_negatives_and_zero(self):
        self.assertEqual(unique_permutations([0, -1]), [[-1, 0], [0, -1]])

    def test_output_preserves_counts_and_lists_are_independent(self):
        numbers = [2, -1, 2, 0]
        results = unique_permutations(numbers)
        self.assertTrue(all(Counter(result) == Counter(numbers) for result in results))
        self.assertEqual(len(results), 12)
        self.assertEqual(len({id(result) for result in results}), len(results))
        self.assertEqual(numbers, [2, -1, 2, 0])
        saved_second = results[1].copy()
        results[0].append(99)
        self.assertEqual(results[1], saved_second)
        self.assertEqual(numbers, [2, -1, 2, 0])

    def test_matches_deduplicated_itertools_permutations(self):
        for size in range(6):
            for values in itertools.product((-1, 0, 1), repeat=size):
                expected = [list(result) for result in sorted(set(itertools.permutations(values)))]
                self.assertEqual(unique_permutations(list(values)), expected)


if __name__ == "__main__":
    unittest.main()
