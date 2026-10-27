"""Combine two sorted lists using a pair of moving indices."""


def merge_sorted_lists(left: list[int], right: list[int]) -> list[int]:
    """Merge nondecreasing integer lists into a new nondecreasing list.

    Keep duplicate values. Inputs must already be sorted; this is not checked.
    Neither input is modified. Time: O(m + n). Auxiliary space: O(1),
    excluding the O(m + n) result.
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    print(merge_sorted_lists([1, 3, 5], [2, 3, 6]))
