"""Search for a word along non-repeating orthogonal paths in a grid."""


def word_exists(board: list[list[str]], word: str) -> bool:
    """Return whether word can be traced without reusing a board cell.

    Board must be rectangular with single-character strings in every cell.
    Invalid row structure or cells raise ValueError, even for an empty word.
    Empty words exist in every valid board. Never modify the input board.
    """
    if not isinstance(board, list) or any(not isinstance(row, list) for row in board):
        raise ValueError("board must be a list of lists")
    columns = len(board[0]) if board else 0
    for row in board:
        if len(row) != columns:
            raise ValueError("board rows must have equal lengths")
        if any(not isinstance(cell, str) or len(cell) != 1 for cell in row):
            raise ValueError("board cells must be single-character strings")

    if word == "":
        return True
    rows = len(board)
    if not rows or not columns or len(word) > rows * columns:
        return False

    used: set[tuple[int, int]] = set()

    def search(row: int, column: int, index: int) -> bool:
        if board[row][column] != word[index]:
            return False
        if index == len(word) - 1:
            return True

        used.add((row, column))
        for row_step, column_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row = row + row_step
            next_column = column + column_step
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and (next_row, next_column) not in used
                and search(next_row, next_column, index + 1)
            ):
                used.remove((row, column))
                return True
        used.remove((row, column))
        return False

    return any(search(row, column, 0) for row in range(rows) for column in range(columns))


if __name__ == "__main__":
    grid = [list("ABCE"), list("SFCS"), list("ADEE")]
    print(word_exists(grid, "ABCCED"))
