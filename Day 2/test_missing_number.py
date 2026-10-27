import itertools
import unittest

from missing_number import missing_number


class MissingNumberTests(unittest.TestCase):
    def test_unsorted_example(self):
        self.assertEqual(missing_number([3, 0, 1]), 2)

    def test_missing_zero_and_missing_upper_endpoint(self):
        self.assertEqual(missing_number([1, 2, 3]), 0)
        self.assertEqual(missing_number([2, 0, 1]), 3)

    def test_empty_input_and_singletons(self):
        self.assertEqual(missing_number([]), 0)
        self.assertEqual(missing_number([0]), 1)
        self.assertEqual(missing_number([1]), 0)

    def test_input_is_unchanged(self):
        numbers = [4, 0, 1, 3]
        self.assertEqual(missing_number(numbers), 2)
        self.assertEqual(numbers, [4, 0, 1, 3])

    def test_every_missing_value_in_small_permutations(self):
        for size in range(6):
            for absent in range(size + 1):
                remaining = [value for value in range(size + 1) if value != absent]
                for values in itertools.permutations(remaining):
                    self.assertEqual(missing_number(list(values)), absent)


if __name__ == "__main__":
    unittest.main()
