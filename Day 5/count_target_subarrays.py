"""Count contiguous, nonempty subarrays with a chosen sum."""


def count_target_subarrays(numbers: list[int], target: int) -> int:
    """Count overlapping matches, including those with zeros or negatives.

    Preserve the input. Expected O(n) time and O(n) auxiliary space,
    under the usual constant-cost integer arithmetic/hash assumption.
    """
    prefix_counts = {0: 1}
    prefix_sum = 0
    matches = 0
    for number in numbers:
        prefix_sum += number
        matches += prefix_counts.get(prefix_sum - target, 0)
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
    return matches


if __name__ == "__main__":
    print(count_target_subarrays([1, -1, 0], 0))
