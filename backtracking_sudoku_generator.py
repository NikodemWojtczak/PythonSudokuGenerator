import random

class BackTrackingSudokuGenerator:
    def generate_sudoku(self):
        sudoku_board = [0] * 81
        self.backtracking(sudoku_board)
        return sudoku_board

    def can_be_placed(self, sudoku_board, index, value):
        x = index % 9
        y = index // 9
        box_x = x // 3
        box_y = y // 3
        box_offset = 27 * box_y + 3 * box_x

        for i in range(9):
            column_value = sudoku_board[x + i * 9]
            row_value = sudoku_board[y * 9 + i]
            box_value = sudoku_board[box_offset + i % 3 + 9 * (i // 3)]
            if column_value == value or row_value == value or box_value == value:
                return False

        return True

    def backtracking(self, sudoku_board, index=0):
        if index == 81:
            return True

        if sudoku_board[index] != 0:
            return self.backtracking(sudoku_board, index + 1)

        numbers_to_fill = list(range(1, 10))
        random.shuffle(numbers_to_fill)

        for number in numbers_to_fill:
            if self.can_be_placed(sudoku_board, index, number):
                sudoku_board[index] = number
                if self.backtracking(sudoku_board, index + 1):
                    return True

                sudoku_board[index] = 0

        return False