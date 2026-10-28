import itertools
import unittest

from search_rotated import search_rotated


class SearchRotatedTests(unittest.TestCase):
    def test_rotated_example_and_missing_target(self):
        numbers = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(search_rotated(numbers, 0), 4)
        self.assertEqual(search_rotated(numbers, 3), -1)

    def test_empty_and_single_element_lists(self):
        self.assertEqual(search_rotated([], 2), -1)
        self.assertEqual(search_rotated([2], 2), 0)
        self.assertEqual(search_rotated([2], 3), -1)

    def test_two_elements_and_unrotated_list(self):
        self.assertEqual(search_rotated([2, 1], 2), 0)
        self.assertEqual(search_rotated([2, 1], 1), 1)
        self.assertEqual(search_rotated([-5, 0, 8], -5), 0)
        self.assertEqual(search_rotated([-5, 0, 8], 8), 2)

    def test_input_list_is_not_modified(self):
        numbers = [3, 8, -7, -2, 0]
        original = numbers.copy()
        self.assertEqual(search_rotated(numbers, -2), 3)
        self.assertEqual(numbers, original)

    def test_small_distinct_lists_at_every_rotation_match_linear_search(self):
        for length in range(1, 6):
            for values in itertools.combinations(range(-3, 4), length):
                for pivot in range(length):
                    numbers = list(values[pivot:] + values[:pivot])
                    for target in range(-4, 5):
                        expected = numbers.index(target) if target in numbers else -1
                        with self.subTest(numbers=numbers, target=target):
                            self.assertEqual(search_rotated(numbers, target), expected)


if __name__ == "__main__":
    unittest.main()
