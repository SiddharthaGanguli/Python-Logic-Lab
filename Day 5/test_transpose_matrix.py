import unittest

from transpose_matrix import transpose_matrix


class TransposeMatrixTests(unittest.TestCase):
    def test_rectangular_matrix(self):
        self.assertEqual(transpose_matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_square_matrix(self):
        self.assertEqual(transpose_matrix([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_empty_shapes(self):
        self.assertEqual(transpose_matrix([]), [])
        self.assertEqual(transpose_matrix([[], []]), [])

    def test_single_row_and_column(self):
        self.assertEqual(transpose_matrix([[1, 2]]), [[1], [2]])
        self.assertEqual(transpose_matrix([[1], [2]]), [[1, 2]])

    def test_rejects_ragged_rows(self):
        for matrix in [[[1], [2, 3]], [[], [1]], [[1], []]]:
            with self.subTest(matrix=matrix):
                with self.assertRaises(ValueError):
                    transpose_matrix(matrix)

    def test_input_and_output_rows_are_independent(self):
        matrix = [[1, 2], [3, 4]]
        result = transpose_matrix(matrix)
        result[0][0] = 99
        self.assertEqual(matrix, [[1, 2], [3, 4]])
        self.assertEqual(result[1], [2, 4])

    def test_matches_zip_reference_for_varied_shapes(self):
        for rows in range(1, 5):
            for columns in range(5):
                matrix = [[row * columns + column for column in range(columns)] for row in range(rows)]
                with self.subTest(rows=rows, columns=columns):
                    self.assertEqual(transpose_matrix(matrix), [list(column) for column in zip(*matrix)])


if __name__ == "__main__":
    unittest.main()
