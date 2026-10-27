import unittest
from itertools import product

from unique_intersection import unique_intersection


class UniqueIntersectionTests(unittest.TestCase):
    def test_preserves_first_list_order(self):
        self.assertEqual(unique_intersection([3, 1, 3, 2, 4], [2, 3, 3]), [3, 2])

    def test_empty_and_disjoint_inputs(self):
        self.assertEqual(unique_intersection([], [1]), [])
        self.assertEqual(unique_intersection([1], []), [])
        self.assertEqual(unique_intersection([1], [2]), [])

    def test_duplicates_and_negative_values(self):
        self.assertEqual(unique_intersection([-1, 0, -1, 2, 0], [0, -1, -1]), [-1, 0])

    def test_inputs_are_preserved(self):
        first, second = [2, 1, 2], [1, 2]
        result = unique_intersection(first, second)
        self.assertEqual(first, [2, 1, 2])
        self.assertEqual(second, [1, 2])
        self.assertIsNot(result, first)
        self.assertIsNot(result, second)

    def test_matches_simple_reference(self):
        inputs = [list(values) for length in range(4) for values in product([-1, 0, 1], repeat=length)]
        for first in inputs:
            for second in inputs:
                expected = [value for index, value in enumerate(first) if value in second and value not in first[:index]]
                with self.subTest(first=first, second=second):
                    self.assertEqual(unique_intersection(first, second), expected)


if __name__ == "__main__":
    unittest.main()
