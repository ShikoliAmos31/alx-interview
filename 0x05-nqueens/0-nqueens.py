#!/usr/bin/python3
"""N-Queens Problem
"""

import sys
from typing import List

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    board_size = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if board_size < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board: List[int], row: int, col: int) -> bool:
    """
    Check if it's safe to place a queen at the given position.

    Args:
        board (List[int]): The current state of the board.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens_util(board: List[int], col: int) -> None:
    """
    Utility function to recursively solve the N-Queens problem.

    Args:
        board (List[int]): The current state of the board.
        col (int): The current column being processed.
    """
    if col == board_size:
        print(str([[i, board[i]] for i in range(board_size)]))
        return
    for i in range(board_size):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens_util(board, col + 1)
            board[col] = -1


def solve_nqueens() -> None:
    """Main function to solve the N-Queens problem."""
    board = [-1 for _ in range(board_size)]
    solve_nqueens_util(board, 0)


solve_nqueens()
