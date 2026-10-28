"""Find the fewest unlimited coins needed to make an exact amount."""


def minimum_coin_change(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins, or -1 if the amount is unreachable.

    Inputs are integer denominations and an integer amount. Reject nonpositive
    denominations and negative amounts with ValueError, even for amount zero.
    Duplicate denominations are allowed. The input list is not modified.
    """
    if amount < 0:
        raise ValueError("amount must be nonnegative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin denominations must be positive")
    if amount == 0:
        return 0
    if not coins:
        return -1

    unreachable = amount + 1
    fewest = [unreachable] * (amount + 1)
    fewest[0] = 0
    for subtotal in range(1, amount + 1):
        for coin in coins:
            if coin <= subtotal:
                fewest[subtotal] = min(fewest[subtotal], fewest[subtotal - coin] + 1)

    return -1 if fewest[amount] == unreachable else fewest[amount]


if __name__ == "__main__":
    print(minimum_coin_change([1, 3, 4], 6))
