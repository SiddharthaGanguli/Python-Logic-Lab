"""Search a rotated sorted list of distinct integers."""


def search_rotated(numbers: list[int], target: int) -> int:
    """Return target's index in numbers, or -1 when it is absent.

    numbers must be a rotation of a strictly ascending integer list. An
    unrotated or empty list is valid. Duplicates are outside this contract.
    The function does not modify the list or validate the rotation.
    """
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle

        if numbers[left] <= numbers[middle]:
            # The left half is sorted, so its endpoints decide membership.
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            # With distinct values, the right half must be sorted here.
            if numbers[middle] < target <= numbers[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


if __name__ == "__main__":
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))
