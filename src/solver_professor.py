from board import Board


class DeterministicSolver:
    def __init__(self, size: int):
        """
        Initialize the Deterministic Solver with a given board size.

        Args:
            size (int): The size of the chessboard (n x n).
        """
        self.size = size
        self.board = Board(size)
        self.solved = False

    def solve(self):
        """
        Solve the N-Queens problem using a deterministic backtracking algorithm.

        Returns:
            bool: True if a solution is found, False otherwise.
        """
        self.solved = self._backtrack(0)
        if self.solved:
            print("\n[Professor] Successful resolution. Board:")
            self.print_board()
        else:
            print("\n[Professor] No solution found.")
        return self.solved

    def _backtrack(self, row: int):
        """
        Recursive helper method for solving the N-Queens problem using backtracking.

        Args:
            row (int): The current row being processed.

        Returns:
            bool: True if a valid configuration is found, False otherwise.
        """
        if row == self.size:
            return True
        for col in range(self.size):
            if self.board.is_safe(row, col):
                self.board.place_queen(row, col)
                if self._backtrack(row + 1):
                    return True
                self.board.remove_queen(row, col)
        return False

    def print_board(self):
        """
        Print the current state of the board.
        """
        for row in self.board.board:
            print(" ".join("Q" if cell else "." for cell in row))

    def solve_time(self):
        """
        Get the time taken to perform the solve operation.
        """
        # TODO: vary constant to manipulate the time taken and profit simulation
        return self.size * 0.5  # proportional to the board size
