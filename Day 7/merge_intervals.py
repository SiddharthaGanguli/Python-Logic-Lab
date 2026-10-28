"""Combine overlapping or touching closed intervals."""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return sorted, merged closed intervals without changing the input.

    Each input tuple contains integer endpoints (start, end). A start greater
    than its end raises ValueError. Touching intervals share an endpoint and
    merge, so [(1, 3), (3, 5)] becomes [(1, 5)]. Empty input returns [].
    """
    for start, end in intervals:
        if start > end:
            raise ValueError("interval start must not exceed its end")
    if not intervals:
        return []

    ordered = sorted(intervals)
    merged: list[tuple[int, int]] = []
    current_start, current_end = ordered[0]
    for index in range(1, len(ordered)):
        start, end = ordered[index]
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    merged.append((current_start, current_end))
    return merged


if __name__ == "__main__":
    print(merge_intervals([(8, 10), (1, 3), (2, 6), (10, 12)]))
