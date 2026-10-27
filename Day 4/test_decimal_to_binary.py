import unittest

from decimal_to_binary import decimal_to_binary


class DecimalToBinaryTests(unittest.TestCase):
    def test_zero_and_small_examples(self):
        for number, expected in ((0, "0"), (1, "1"), (2, "10"), (10, "1010"), (42, "101010")):
            with self.subTest(number=number):
                self.assertEqual(decimal_to_binary(number), expected)

    def test_rejects_negative_numbers(self):
        for number in (-1, -10, -(10**100)):
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    decimal_to_binary(number)

    def test_matches_builtin_for_small_numbers(self):
        for number in range(513):
            with self.subTest(number=number):
                self.assertEqual(decimal_to_binary(number), bin(number)[2:])

    def test_powers_of_two_and_adjacent_values(self):
        for exponent in (1, 8, 32, 127):
            with self.subTest(exponent=exponent):
                self.assertEqual(decimal_to_binary(2**exponent), "1" + "0" * exponent)
                self.assertEqual(decimal_to_binary(2**exponent - 1), "1" * exponent)

    def test_large_integer_round_trip(self):
        number = 2**1024 + 2**511 + 1
        result = decimal_to_binary(number)
        self.assertEqual(len(result), 1025)
        self.assertEqual(int(result, 2), number)
        self.assertEqual(result, bin(number)[2:])


if __name__ == "__main__":
    unittest.main()
