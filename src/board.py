class Board:
    def __init__(self, size: int):
        """
        Initialize the chessboard with a given size.

        Args:
            size (int): The size of the chessboard (n x n).
        """
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def is_safe(self, row: int, col: int) -> bool:
        """
        Check if it's safe to place a queen at the given position.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        # Check this column on upper rows
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.size)):
            if self.board[i][j] == 1:
                return False
        return True

    def place_queen(self, row: int, col: int):
        """
        Place a queen at the specified position on the board.

        Args:
            row (int): The row index.
            col (int): The column index.
        """
        self.board[row][col] = 1

    def remove_queen(self, row: int, col: int):
        """
        Remove a queen from the specified position on the board.

        Args:
            row (int): The row index.
            col (int): The column index.
        """
        self.board[row][col] = 0

    def reset(self):
        """
        Reset the board to the initial state with no queens placed.
        """
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
