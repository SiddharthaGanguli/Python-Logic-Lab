import unittest

from prime_number import is_prime


class PrimeNumberTests(unittest.TestCase):
    def test_integers_below_two_are_not_prime(self):
        for number in (-100, -1, 0, 1):
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))

    def test_small_primes(self):
        for number in (2, 3, 5, 7, 29, 97):
            with self.subTest(number=number):
                self.assertTrue(is_prime(number))

    def test_composites_and_perfect_squares(self):
        for number in (4, 9, 15, 25, 49, 121, 1009 * 1009):
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))

    def test_matches_full_divisor_search_for_small_integers(self):
        for number in range(-5, 251):
            expected = number >= 2 and all(
                number % divisor != 0 for divisor in range(2, number)
            )
            with self.subTest(number=number):
                self.assertEqual(is_prime(number), expected)

    def test_larger_known_prime(self):
        self.assertTrue(is_prime(1_000_003))

    def test_large_composites_do_not_need_float_conversion(self):
        self.assertFalse(is_prime(10**400))
        self.assertFalse(is_prime(10**400 + 2))


if __name__ == "__main__":
    unittest.main()
