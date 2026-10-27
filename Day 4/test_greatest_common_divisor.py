import math
import unittest

from greatest_common_divisor import gcd


class GreatestCommonDivisorTests(unittest.TestCase):
    def test_common_factors_and_coprime_values(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(35, 64), 1)
        self.assertEqual(gcd(12, 12), 12)

    def test_zero_inputs(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, -9), 9)
        self.assertEqual(gcd(9, 0), 9)

    def test_negative_inputs(self):
        for first, second in ((-24, 36), (24, -36), (-24, -36)):
            with self.subTest(first=first, second=second):
                self.assertEqual(gcd(first, second), 12)

    def test_matches_math_gcd_across_small_integer_pairs(self):
        for first in range(-30, 31):
            for second in range(-30, 31):
                with self.subTest(first=first, second=second):
                    self.assertEqual(gcd(first, second), math.gcd(first, second))

    def test_large_integer_common_factor(self):
        factor = 10**150 + 7
        self.assertEqual(gcd(35 * factor, 64 * factor), factor)


if __name__ == "__main__":
    unittest.main()
