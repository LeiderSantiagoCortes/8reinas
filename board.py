class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def is_safe(self, row: int, col: int) -> bool:
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, self.size)):
            if self.board[i][j] == 1:
                return False
        return True

    def place_queen(self, row: int, col: int):
        self.board[row][col] = 1

    def remove_queen(self, row: int, col: int):
        self.board[row][col] = 0

    def reset(self):
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
