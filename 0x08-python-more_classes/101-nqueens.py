#!/usr/bin/python3
"""Solves the N-queens puzzle"""
import sys


def b_init(n):
    """Initializes an `n`x`n` sized chessboard with 0's"""
    b = []
    [b.append([]) for i in range(n)]
    [r.append(' ') for i in range(n) for r in b]
    return (b)


def cpy_b(board):
    """Returns a deepcopy of a chessboard."""
    if type(board) is list:
        return list(map(cpy_b, board))
    return (board)


def solve_b(board):
    """Returns the list of lists representation of a solved chessboard."""
    s = []
    for row in range(len(board)):
        for chess in range(len(board)):
            if board[row][chess] == "Q":
                s.append([row, chess])
                break
    return (s)


def x_out(b, row, col):
    """X out spots on a chessboard.

    Args:
        b (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    for c in range(col + 1, len(b)):
        b[row][c] = "x"
    for c in range(col - 1, -1, -1):
        b[row][c] = "x"
    for r in range(row + 1, len(b)):
        b[r][col] = "x"
    for r in range(row - 1, -1, -1):
        b[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(b)):
        if c >= len(b):
            break
        b[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        b[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(b):
            break
        b[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(b)):
        if c < 0:
            break
        b[r][c] = "x"
        c -= 1


def solve_recur(b, row, q, s):
    """Recursively solve an N-queens puzzle.

    Args:
        b (list): The current working chessboard.
        row (int): The current working row.
        q (int): The current number of placed queens.
        s (list): A list of lists of solutions.
    Returns:
        solution
    """
    if q == len(b):
        s.append(solve_b(b))
        return (s)

    for c in range(len(b)):
        if b[row][c] == " ":
            tmp_board = cpy_b(b)
            tmp_board[row][c] = "Q"
            x_out(tmp_board, row, c)
            s = solve_recur(tmp_board, row + 1, q + 1, s)
    return (s)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    b = b_init(int(sys.argv[1]))
    s = solve_recur(b, 0, 0, [])
    for sol in s:
        print(sol)
