import itertools
import unittest

from word_search import word_exists


def word_by_path_enumeration(board, word):
    """Reference: enumerate simple paths without pruning nonmatching prefixes."""
    if word == "":
        return True
    rows = len(board)
    columns = len(board[0]) if board else 0
    pending = [
        (row, column, ((row, column),), board[row][column])
        for row in range(rows)
        for column in range(columns)
    ]
    while pending:
        row, column, path, text = pending.pop()
        if text == word:
            return True
        if len(text) == len(word):
            continue
        for row_step, column_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_row, next_column = row + row_step, column + column_step
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and (next_row, next_column) not in path
            ):
                pending.append((
                    next_row, next_column,
                    path + ((next_row, next_column),),
                    text + board[next_row][next_column],
                ))
    return False


class WordSearchTests(unittest.TestCase):
    def test_examples_with_turns_and_failed_search(self):
        board = [list("ABCE"), list("SFCS"), list("ADEE")]
        self.assertTrue(word_exists(board, "ABCCED"))
        self.assertTrue(word_exists(board, "SEE"))
        self.assertFalse(word_exists(board, "ABCB"))

    def test_empty_word_and_empty_board_shapes(self):
        for board in ([], [[]], [[], []], [["A"]]):
            with self.subTest(board=board):
                self.assertTrue(word_exists(board, ""))
        self.assertFalse(word_exists([], "A"))
        self.assertFalse(word_exists([[], []], "A"))

    def test_single_cell_is_case_sensitive(self):
        self.assertTrue(word_exists([["A"]], "A"))
        self.assertFalse(word_exists([["A"]], "a"))
        self.assertFalse(word_exists([["A"]], "AA"))

    def test_diagonal_steps_and_cell_reuse_are_forbidden(self):
        self.assertFalse(word_exists([list("AB"), list("CD")], "AD"))
        self.assertFalse(word_exists([list("AB"), list("XY")], "ABA"))

    def test_rejects_ragged_boards_even_with_empty_word(self):
        for board in ([["A"], ["B", "C"]], [[], ["A"]], [["A"], []]):
            for word in ("", "A"):
                with self.subTest(board=board, word=word), self.assertRaises(ValueError):
                    word_exists(board, word)

    def test_rejects_invalid_cells_even_with_empty_word(self):
        for cell in ("", "AB", None, 1, ["A"]):
            for word in ("", "A"):
                with self.subTest(cell=cell, word=word), self.assertRaises(ValueError):
                    word_exists([[cell]], word)

    def test_rejects_non_list_rows(self):
        for board in (["AB"], [("A",)], [None]):
            with self.subTest(board=board), self.assertRaises(ValueError):
                word_exists(board, "")

    def test_board_is_unchanged_after_success_and_failure(self):
        board = [list("ABCE"), list("SFCS"), list("ADEE")]
        original = [row.copy() for row in board]
        for word in ("ABCCED", "ABCB", "SEE", ""):
            word_exists(board, word)
            self.assertEqual(board, original)

    def test_matches_all_simple_paths_on_small_boards(self):
        words = [
            "".join(characters)
            for size in range(5)
            for characters in itertools.product("AB", repeat=size)
        ]
        for cells in itertools.product("AB", repeat=4):
            board = [list(cells[:2]), list(cells[2:])]
            for word in words:
                self.assertEqual(word_exists(board, word), word_by_path_enumeration(board, word))


if __name__ == "__main__":
    unittest.main()
