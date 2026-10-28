import itertools
import unittest

from edit_distance import edit_distance


def reference_distance(first, second):
    """Enumerate choices directly for tiny inputs, without a DP table."""
    if not first:
        return len(second)
    if not second:
        return len(first)
    if first[0] == second[0]:
        return reference_distance(first[1:], second[1:])
    return 1 + min(reference_distance(first[1:], second),
                   reference_distance(first, second[1:]),
                   reference_distance(first[1:], second[1:]))


class EditDistanceTests(unittest.TestCase):
    def test_examples_require_combinations_of_operations(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("flaw", "lawn"), 2)

    def test_empty_and_identical_strings(self):
        self.assertEqual(edit_distance("", ""), 0)
        self.assertEqual(edit_distance("abc", ""), 3)
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("same", "same"), 0)

    def test_each_operation_has_unit_cost(self):
        self.assertEqual(edit_distance("cat", "cart"), 1)
        self.assertEqual(edit_distance("cart", "cat"), 1)
        self.assertEqual(edit_distance("cat", "cut"), 1)

    def test_transposition_is_not_a_single_operation(self):
        self.assertEqual(edit_distance("ab", "ba"), 2)

    def test_case_and_unicode_code_points_are_significant(self):
        self.assertEqual(edit_distance("A", "a"), 1)
        self.assertEqual(edit_distance("🙂a", "🙂b"), 1)
        self.assertEqual(edit_distance("é", "e\u0301"), 2)

    def test_unequal_lengths_work_in_both_argument_orders(self):
        self.assertEqual(edit_distance("a", "abbbbb"), 5)
        self.assertEqual(edit_distance("abbbbb", "a"), 5)

    def test_small_inputs_match_recursive_edit_enumeration(self):
        samples = ["".join(values) for size in range(4)
                   for values in itertools.product("ab", repeat=size)]
        for first in samples:
            for second in samples:
                self.assertEqual(edit_distance(first, second),
                                 reference_distance(first, second), (first, second))


if __name__ == "__main__":
    unittest.main()
