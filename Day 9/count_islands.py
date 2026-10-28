"""Count connected land regions without changing a binary grid."""


def count_islands(grid: list[list[int]]) -> int:
    """Count groups of 1s connected horizontally or vertically.

    Reject ragged rows or values other than 0 and 1 with ValueError.
    Empty grids and zero-column grids have no islands. For r rows and c
    columns, O(r + r*c) time and O(r*c) auxiliary space; input is preserved.
    """
    if not grid:
        return 0
    columns = len(grid[0])
    if any(len(row) != columns for row in grid):
        raise ValueError("grid rows must have equal lengths")
    if any(cell not in (0, 1) for row in grid for cell in row):
        raise ValueError("grid cells must be 0 or 1")

    visited: set[tuple[int, int]] = set()
    islands = 0
    for row in range(len(grid)):
        for column in range(columns):
            if grid[row][column] == 0 or (row, column) in visited:
                continue
            islands += 1
            visited.add((row, column))
            pending = [(row, column)]
            while pending:
                current_row, current_column = pending.pop()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = (current_row + dr, current_column + dc)
                    nr, nc = neighbor
                    if (0 <= nr < len(grid) and 0 <= nc < columns
                            and grid[nr][nc] == 1 and neighbor not in visited):
                        visited.add(neighbor)
                        pending.append(neighbor)
    return islands


if __name__ == "__main__":
    print(count_islands([[1, 1, 0], [0, 1, 0], [1, 0, 1]]))
