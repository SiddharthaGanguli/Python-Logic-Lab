import unittest

from subsets import subsets


class SubsetsTests(unittest.TestCase):
    def test_empty_input_has_one_empty_subset(self):
        self.assertEqual(subsets([]), [[]])

    def test_preorder_preserves_unsorted_input_order(self):
        self.assertEqual(
            subsets([3, 1, 2]),
            [[], [3], [3, 1], [3, 1, 2], [3, 2], [1], [1, 2], [2]],
        )

    def test_singleton_and_negative_values(self):
        self.assertEqual(subsets([-2]), [[], [-2]])
        self.assertEqual(subsets([-1, 0]), [[], [-1], [-1, 0], [0]])

    def test_input_and_output_lists_are_independent(self):
        numbers = [2, 1]
        results = subsets(numbers)
        self.assertEqual(numbers, [2, 1])
        self.assertEqual(len({id(result) for result in results}), len(results))
        results[1].append(99)
        self.assertEqual(results[2], [2, 1])
        self.assertEqual(numbers, [2, 1])
        self.assertEqual(subsets([2, 1]), [[], [2], [2, 1], [1]])

    def test_matches_bitmask_enumeration_in_index_tuple_order(self):
        for size in range(8):
            numbers = list(range(size, 0, -1))
            index_sets = sorted(
                tuple(index for index in range(size) if mask & (1 << index))
                for mask in range(1 << size)
            )
            expected = [[numbers[index] for index in indices] for indices in index_sets]
            results = subsets(numbers)
            with self.subTest(size=size):
                self.assertEqual(results, expected)
                self.assertEqual(len(results), 2**size)
                self.assertEqual(len(set(map(tuple, results))), len(results))


if __name__ == "__main__":
    unittest.main()
