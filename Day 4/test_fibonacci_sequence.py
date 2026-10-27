import unittest

from fibonacci_sequence import fibonacci_sequence


class FibonacciSequenceTests(unittest.TestCase):
    def test_empty_and_short_sequences(self):
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])

    def test_first_ten_values(self):
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_rejects_negative_count(self):
        for count in (-1, -100):
            with self.subTest(count=count):
                with self.assertRaises(ValueError):
                    fibonacci_sequence(count)

    def test_known_value_beyond_fixed_width_integers(self):
        values = fibonacci_sequence(101)
        self.assertEqual(len(values), 101)
        self.assertEqual(values[100], 354224848179261915075)

    def test_cassini_identity_for_successive_values(self):
        values = fibonacci_sequence(50)
        for index in range(1, len(values) - 1):
            with self.subTest(index=index):
                self.assertEqual(
                    values[index - 1] * values[index + 1] - values[index] ** 2,
                    (-1) ** index,
                )

    def test_calls_return_independent_lists(self):
        values = fibonacci_sequence(3)
        values[0] = 999
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1])


if __name__ == "__main__":
    unittest.main()
