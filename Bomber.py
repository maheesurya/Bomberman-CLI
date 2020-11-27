''' This file contains Bomber class '''
import time
from Person import Person


class Bomberman(Person):
    ''' This is class docstring '''
    def __init__(self):
        super(Bomberman, self).__init__()
        self.lives = 3
        self.row = 2
        self.col = 4
        self.score = 0

    def position(self, board):
        ''' This is position string '''
        if board.board[self.row][self.col] == ' ':
            for i in range(0, 2):
                for j in range(0, 4):
                    board.board[self.row + i][self.col + j] = 'B'

    def move(self, board, val):
        ''' This is move string '''
        if val == 'a':
            if (board.board[self.row][self.col - 4] == ' ' and
                    board.board[self.row + 1][self.col - 4] == ' '):
                self.col -= 4
                time.sleep(0.3)
            if (board.board[self.row][self.col - 4] == 'e' and
                    board.board[self.row + 1][self.col - 4] == 'e'):
                self.lives -= 1
        elif val == 'd':
            if (board.board[self.row][self.col + 7] == ' ' and
                    board.board[self.row + 1][self.col + 7] == ' '):
                self.col += 4
                time.sleep(0.3)
            if (board.board[self.row][self.col + 7] == 'e' and
                    board.board[self.row + 1][self.col + 7] == 'e'):
                self.lives -= 1
        elif val == 'w':
            if (board.board[self.row - 2][self.col] == ' ' and
                    board.board[self.row - 2][self.col + 3] == ' '):
                self.row -= 2
                time.sleep(0.3)
            if (board.board[self.row - 2][self.col] == 'e' and
                    board.board[self.row - 2][self.col + 3] == 'e'):
                self.lives -= 1
        elif val == 's':
            if (board.board[self.row + 3][self.col] == ' ' and
                    board.board[self.row + 3][self.col + 3] == ' '):
                self.row += 2
                time.sleep(0.3)
            if (board.board[self.row + 3][self.col] == 'e' and
                    board.board[self.row + 3][self.col + 3] == 'e'):
                self.lives -= 1

    def get_life(self):
        ''' Go get a life '''
        return self.lives
