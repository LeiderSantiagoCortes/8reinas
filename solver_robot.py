import random
from board import Board

class LasVegasSolver:
    def __init__(self, size: int):
        self.size = size
        self.board = Board(size)

    def solve(self) -> bool:
        attempts = 0
        while attempts < 1000:  # Máximo de intentos para evitar loops infinitos
            self.board.reset()
            queens = 0
            while queens < self.size:
                row = queens
                col = random.randint(0, self.size - 1)
                if self.board.is_safe(row, col):
                    self.board.place_queen(row, col)
                    queens += 1
            if queens == self.size:  # Si se colocaron todas las reinas
                print("\n[Robot] Resolución exitosa. Tablero:")
                self.print_board()
                return True
            attempts += 1

        print("\n[Robot] No se encontró solución.")
        return False  # No se encontró solución en los intentos

    def print_board(self):
        for row in self.board.board:
            print(" ".join("Q" if cell else "." for cell in row))
