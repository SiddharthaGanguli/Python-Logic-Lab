import copy
from itertools import product
import unittest

from count_islands import count_islands


def count_with_disjoint_sets(grid):
    cells = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 1}
    parents = {cell: cell for cell in cells}

    def root(cell):
        while parents[cell] != cell:
            cell = parents[cell]
        return cell

    for row, column in cells:
        for neighbor in ((row + 1, column), (row, column + 1)):
            if neighbor in cells:
                parents[root(neighbor)] = root((row, column))
    return len({root(cell) for cell in cells})


class CountIslandsTests(unittest.TestCase):
    def test_separate_regions(self):
        self.assertEqual(count_islands([[1, 1, 0], [0, 1, 0], [1, 0, 1]]), 3)

    def test_diagonals_do_not_connect(self):
        self.assertEqual(count_islands([[1, 0], [0, 1]]), 2)

    def test_empty_water_and_solid_land(self):
        self.assertEqual(count_islands([]), 0)
        self.assertEqual(count_islands([[], []]), 0)
        self.assertEqual(count_islands([[0, 0]]), 0)
        self.assertEqual(count_islands([[1, 1], [1, 1]]), 1)

    def test_rejects_invalid_grids(self):
        for grid in ([[1], []], [[], [1]], [[1, 2]], [["1"]]):
            with self.subTest(grid=grid):
                with self.assertRaises(ValueError):
                    count_islands(grid)

    def test_input_is_preserved(self):
        grid = [[1, 0, 1], [1, 1, 0]]
        original = copy.deepcopy(grid)
        count_islands(grid)
        self.assertEqual(grid, original)

    def test_long_island_avoids_recursion_limit(self):
        self.assertEqual(count_islands([[1] * 2000]), 1)

    def test_matches_disjoint_sets_on_all_small_grids(self):
        for rows, columns in ((1, 3), (2, 3), (3, 3)):
            for values in product((0, 1), repeat=rows * columns):
                grid = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                with self.subTest(grid=grid):
                    self.assertEqual(count_islands(grid), count_with_disjoint_sets(grid))


if __name__ == "__main__":
    unittest.main()
