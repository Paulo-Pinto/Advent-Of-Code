class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board = solve_single_check(board)


def solve_single_check(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for guess in range(1, 10):
                    if check_position(board, r, c, str(guess)):  # if it returns true, continue on that path
                        board[r][c] = str(guess)
                        solve_single_check(board)
                        board[r][c] = "."
                return
    print(board)


def check_position(board, row, col, guess):
    for i in range(9):
        if board[row][i] == guess:
            return False
        if board[i][col] == guess:
            return False

    row_square = (row // 3) * 3
    col_square = (col // 3) * 3

    for r in range(0, 3):
        for c in range(0, 3):
            if board[row_square + r][col_square + c] == guess:
                return False
    return True
