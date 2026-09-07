import numpy as np
import os

class Board:
    items = [" ", "X", "O"]

    def __init__(self):
        self.grid = np.zeros((6, 7), dtype=int)

    def print(self):
        for row in range(6):
            for col in range(7):
                print(f"| {self.items[self.grid[row][col]]} ", end="")
            print("|")
            print('-' * 29)
        print("  A   B   C   D   E   F   G")

    def get_value(self, row, col):
        return self.grid[row][col]

    def drop_piece(self, col, player):
        for row in range(5, -1, -1):
            if self.grid[row][col] == 0:
                self.grid[row][col] = player
                return row
        else:
            print("It is not an valid move")
            return None

    def check_winner(self, row, col):
        player = self.grid[row][col]

        if any(np.all(self.grid[row, col:col + 4] == player) for col in range(4)):
            return True

        if any(np.all(self.grid[row:row + 4, col] == player) for row in range(3)):
            return True

        if any(np.all(np.diagonal(self.grid[row:row + 4, col:col + 4]) == player) for row in range(3) for col in range(4)):
            return True

        if any(np.all(np.diagonal(np.flipud(self.grid[row:row + 4, col:col + 4])) == player) for row in range(3) for col in range(4)):
            return True

        return False

    def is_filled(self, col):
        return self.grid[0][col] != 0

    def reinit(self):
        self.grid.fill(0)


class ConnectFour:
    players = ["X", "O"]
    col_indicates = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}

    def __init__(self):
        self.active_player = 0
        self.board = Board()

    def start_game(self):
        while True:
            print("\n" + 30 * "=")
            print("Player", self.players[self.active_player], "'s turn")
            print(30 * "=" + "\n")
            self.board.print()

            try:
                col_input = input("enter your move(A-G): ").upper()
                col = self.col_indicates.get(col_input)
                if col is None:
                    raise ValueError("\nIt is not an valid move. enter a valid column(A-G)")
                elif self.board.is_filled(col):
                    raise ValueError("\nColumn is filled. enter another column")
            except ValueError as e:
                print(e)
                continue

            row = self.board.drop_piece(col, self.active_player + 1)
            if row is not None:
                if self.board.check_winner(row, col):
                    os.system('cls')
                    self.board.print()
                    print("Player", self.players[self.active_player], "win")
                    break
                elif np.all(self.board.grid != 0):
                    os.system('cls')
                    self.board.print()
                    print("It is a draw")
                    break

                self.active_player ^= 1

        while True:
            user_answer = input("New game? (Y/N): ").upper()
            if user_answer == "Y":
                self.reinit()
                break
            elif user_answer == "N":
                break
            else:
                print("Invalid input. Enter Y or N")

    def reinit(self):
        self.active_player = 0
        self.board.reinit()
        self.start_game()

game = ConnectFour()
game.start_game()
