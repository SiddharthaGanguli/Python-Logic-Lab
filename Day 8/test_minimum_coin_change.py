from collections import deque
import unittest

from minimum_coin_change import minimum_coin_change


def reference_minimum(coins, amount):
    queue = deque([(0, 0)])
    seen = {0}
    while queue:
        subtotal, count = queue.popleft()
        if subtotal == amount:
            return count
        for coin in coins:
            following = subtotal + coin
            if following <= amount and following not in seen:
                seen.add(following)
                queue.append((following, count + 1))
    return -1


class MinimumCoinChangeTests(unittest.TestCase):
    def test_a_greedy_choice_can_miss_the_minimum(self):
        self.assertEqual(minimum_coin_change([1, 3, 4], 6), 2)

    def test_unreachable_amount_and_oversized_coins(self):
        self.assertEqual(minimum_coin_change([2, 4], 7), -1)
        self.assertEqual(minimum_coin_change([10], 3), -1)

    def test_zero_amount_and_empty_coin_list(self):
        self.assertEqual(minimum_coin_change([2, 5], 0), 0)
        self.assertEqual(minimum_coin_change([], 0), 0)
        self.assertEqual(minimum_coin_change([], 4), -1)

    def test_invalid_denominations_are_rejected_even_for_zero_amount(self):
        for coins in ([0], [-1], [2, 0], [1, -3]):
            for amount in (0, 4):
                with self.subTest(coins=coins, amount=amount), self.assertRaises(ValueError):
                    minimum_coin_change(coins, amount)

    def test_negative_amount_is_rejected_with_or_without_coins(self):
        for coins in ([], [1, 2]):
            with self.subTest(coins=coins), self.assertRaises(ValueError):
                minimum_coin_change(coins, -1)

    def test_duplicates_are_allowed_and_input_is_not_modified(self):
        coins = [4, 1, 3, 3]
        original = coins.copy()
        self.assertEqual(minimum_coin_change(coins, 6), 2)
        self.assertEqual(coins, original)

    def test_small_amounts_match_breadth_first_search(self):
        denominations = [[], [1], [2], [3], [1, 3], [2, 4], [2, 3, 3], [4, 7]]
        for coins in denominations:
            for amount in range(21):
                self.assertEqual(minimum_coin_change(coins, amount),
                                 reference_minimum(coins, amount), (coins, amount))


if __name__ == "__main__":
    unittest.main()
