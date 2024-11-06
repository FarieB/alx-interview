#!/usr/bin/python3
'''N Queens Challenge'''

import sys


def is_safe(placed_queens, row, col):
    """Check if a queen can be placed at (row, col) safely."""
    for r, c in placed_queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n):
    """Solve the N queens problem using backtracking and return solutions."""
    def backtrack(row):
        if row == n:
            solutions.append(placed_queens[:])
            return
        for col in range(n):
            if is_safe(placed_queens, row, col):
                placed_queens.append([row, col])
                backtrack(row + 1)
                placed_queens.pop()

    solutions = []
    placed_queens = []
    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
