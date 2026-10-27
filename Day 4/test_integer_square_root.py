import math
import unittest

from integer_square_root import integer_square_root


class IntegerSquareRootTests(unittest.TestCase):
    def test_small_examples(self):
        for number, expected in ((0, 0), (1, 1), (2, 1), (8, 2), (16, 4), (26, 5)):
            with self.subTest(number=number):
                self.assertEqual(integer_square_root(number), expected)

    def test_rejects_negative_numbers(self):
        for number in (-1, -100):
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    integer_square_root(number)

    def test_matches_math_isqrt_for_small_numbers(self):
        for number in range(1001):
            with self.subTest(number=number):
                self.assertEqual(integer_square_root(number), math.isqrt(number))

    def test_values_around_large_perfect_square(self):
        root = 10**200 + 123
        square = root * root
        self.assertEqual(integer_square_root(square - 1), root - 1)
        self.assertEqual(integer_square_root(square), root)
        self.assertEqual(integer_square_root(square + 1), root)

    def test_floor_property_for_large_nonsquare(self):
        number = 2**1000 + 987654321
        root = integer_square_root(number)
        self.assertLessEqual(root * root, number)
        self.assertGreater((root + 1) * (root + 1), number)
        self.assertEqual(root, math.isqrt(number))


if __name__ == "__main__":
    unittest.main()
