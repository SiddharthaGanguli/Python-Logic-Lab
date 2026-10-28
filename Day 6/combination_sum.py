"""Build target-sum combinations with unlimited reuse of positive values."""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Return sorted unique combinations whose sum is target.

    Candidates must be positive integers; target must be nonnegative.
    Reject nonpositive candidates or a negative target with ValueError,
    including invalid candidates when target is zero. Leave inputs unchanged.
    Deduplicate candidates, and permit each remaining value any number of times.
    """
    if target < 0:
        raise ValueError("target must be nonnegative")
    if any(candidate <= 0 for candidate in candidates):
        raise ValueError("candidates must be positive")

    choices = sorted(set(candidates))
    results: list[list[int]] = []
    current: list[int] = []

    def build(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(current.copy())
            return
        for index in range(start, len(choices)):
            candidate = choices[index]
            if candidate > remaining:
                break
            current.append(candidate)
            build(index, remaining - candidate)
            current.pop()

    build(0, target)
    return results


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))
