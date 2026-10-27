import itertools
import unittest

from rotate_list import rotate_right


class RotateRightTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_large_step_count_and_duplicates(self):
        self.assertEqual(rotate_right([2, 2, -1], 10), [-1, 2, 2])

    def test_empty_singleton_and_full_rotation(self):
        self.assertEqual(rotate_right([], 4), [])
        self.assertEqual(rotate_right([7], 100), [7])
        self.assertEqual(rotate_right([1, 2, 3], 3), [1, 2, 3])

    def test_negative_steps_are_rejected_even_for_empty_input(self):
        for values in ([], [1, 2]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                rotate_right(values, -1)

    def test_result_is_independent_and_input_is_unchanged(self):
        for values in ([], [1, 2, 3]):
            for steps in (0, 2, 3):
                original = values.copy()
                result = rotate_right(values, steps)
                self.assertIsNot(result, values)
                result.append(99)
                self.assertEqual(values, original)

    def test_small_inputs_against_repeated_single_step_rotation(self):
        for size in range(5):
            for values in itertools.product((-1, 0, 1), repeat=size):
                for steps in range(9):
                    expected = list(values)
                    for _ in range(steps):
                        if expected:
                            expected.insert(0, expected.pop())
                    self.assertEqual(rotate_right(list(values), steps), expected)


if __name__ == "__main__":
    unittest.main()
