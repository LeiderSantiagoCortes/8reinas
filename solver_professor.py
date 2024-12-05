from board import Board

class DeterministicSolver:
    def __init__(self, size: int):
        self.size = size
        self.board = Board(size)
        self.solved = False

    def solve(self):
        self.solved = self._backtrack(0)
        if self.solved:
            print("\n[Profesor] Resolución exitosa. Tablero:")
            self.print_board()
        else:
            print("\n[Profesor] No se encontró solución.")
        return self.solved

    def _backtrack(self, row: int):
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
        for row in self.board.board:
            print(" ".join("Q" if cell else "." for cell in row))
