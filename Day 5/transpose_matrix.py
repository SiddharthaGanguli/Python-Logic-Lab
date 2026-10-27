"""Turn the rows of a rectangular matrix into columns."""


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Return a new transposed matrix; reject rows with unequal lengths.

    Empty input or a rectangular matrix with zero columns returns [].
    For r rows and c columns: O(r + r*c) time, O(r*c) output space,
    and O(1) auxiliary space apart from the output and loop variables.
    """
    if not matrix:
        return []
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError("matrix rows must have equal lengths")
    return [[row[column] for row in matrix] for column in range(columns)]


if __name__ == "__main__":
    print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
