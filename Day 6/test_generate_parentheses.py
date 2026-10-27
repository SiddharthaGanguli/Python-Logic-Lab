import unittest

from generate_parentheses import generate_parentheses


def is_balanced(sequence):
    balance = 0
    for character in sequence:
        balance += 1 if character == "(" else -1
        if balance < 0:
            return False
    return balance == 0


class GenerateParenthesesTests(unittest.TestCase):
    def test_zero_pairs_has_one_empty_sequence(self):
        self.assertEqual(generate_parentheses(0), [""])

    def test_one_and_two_pairs(self):
        self.assertEqual(generate_parentheses(1), ["()"])
        self.assertEqual(generate_parentheses(2), ["(())", "()()"])

    def test_three_pairs_are_complete_and_ordered(self):
        self.assertEqual(
            generate_parentheses(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )

    def test_each_result_is_unique_balanced_and_has_expected_length(self):
        results = generate_parentheses(4)
        self.assertEqual(len(results), 14)
        self.assertEqual(results, sorted(results))
        self.assertEqual(len(results), len(set(results)))
        self.assertTrue(all(len(result) == 8 and is_balanced(result) for result in results))

    def test_negative_pairs_are_rejected(self):
        with self.assertRaises(ValueError):
            generate_parentheses(-1)


if __name__ == "__main__":
    unittest.main()
