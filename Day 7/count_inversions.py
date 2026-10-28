"""Count out-of-order index pairs while merging sorted halves."""


def count_inversions(numbers: list[int]) -> int:
    """Count pairs i < j for which numbers[i] > numbers[j].

    Equal values do not form inversions. Empty or single-element lists return
    zero. The input is preserved; merge sorting works on a separate copy.
    """
    values = numbers.copy()
    buffer = [0] * len(values)

    def sort_and_count(left: int, right: int) -> int:
        if right - left < 2:
            return 0

        middle = (left + right) // 2
        inversions = sort_and_count(left, middle) + sort_and_count(middle, right)
        first, second, destination = left, middle, left

        while first < middle and second < right:
            if values[first] <= values[second]:
                buffer[destination] = values[first]
                first += 1
            else:
                buffer[destination] = values[second]
                inversions += middle - first
                second += 1
            destination += 1

        while first < middle:
            buffer[destination] = values[first]
            first += 1
            destination += 1
        while second < right:
            buffer[destination] = values[second]
            second += 1
            destination += 1

        for index in range(left, right):
            values[index] = buffer[index]
        return inversions

    return sort_and_count(0, len(values))


if __name__ == "__main__":
    print(count_inversions([2, 4, 1, 3, 5]))
    print(count_inversions([3, 2, 1]))
