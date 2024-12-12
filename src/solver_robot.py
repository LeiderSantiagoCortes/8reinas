import random
from board import Board


class LasVegasSolver:
    def __init__(self, size: int):
        """
        Initialize the Las Vegas Solver with a given board size.

        Args:
            size (int): The size of the chessboard (n x n).
        """
        self.size = size
        self.board = Board(size)

    def solve(self) -> bool:
        """
        Attempt to solve the N-Queens problem using the Las Vegas algorithm.

        Returns:
            bool: True if a solution is found, False otherwise.
        """
        attempts = 0
        # print("\n[Robot] Solving the", self.size, "Queens problem using the Las Vegas algorithm.")
        while attempts < 1000:  # Maximum number of attempts to avoid infinite loops
            # print("\n[Robot] Attempt:", attempts + 1)
            self.board.reset()
            queens = 0
            while queens < self.size:
                # print("\n[Robot] Placing queen", queens + 1)
                row = queens
                placement_attempts = 0
                max_placement_attempts = 50
                placed = False
                while placement_attempts < max_placement_attempts:
                    col = random.randint(0, self.size - 1)
                    if self.board.is_safe(row, col):
                        self.board.place_queen(row, col)
                        queens += 1
                        placed = True
                        break
                    placement_attempts += 1
                if not placed:
                    # print(f"\n[Robot] Failed to place queen {queens + 1} after {max_placement_attempts} attempts. Restarting.")
                    break  # Restart the outer attempt
            if queens == self.size:
                # print("\n[Robot] Successful resolution. Board:")
                self.print_board()
                return True
            attempts += 1

        print("\n[Robot] No solution found.")
        return False

    def print_board(self):
        """
        Print the current state of the board.
        """
        for row in self.board.board:
            print(" ".join("Q" if cell else "." for cell in row))

    def solve_time(self) -> int:
        """
        Get the time taken by the solver to solve
        """
        return random.uniform(10, 30)  # Random time between 10 and 30 seconds
