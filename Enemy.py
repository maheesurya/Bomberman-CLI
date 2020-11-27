''' This is Enemy file '''
from random import randint
from Person import Person

class Enemy(Person):
    ''' This Enemy is dangerous '''
    def __init__(self, board):
        super(Enemy, self).__init__()
        self.__position(board)
        self.life = 1
        self.status = -1

    def __position(self, board):
        val = 0
        while val != 1:
            row = randint(2, 89)
            col = randint(4, 37)
            if(board.board[col][row] == ' ') and (board.board[col + 1][row] == ' '):
                if (board.board[col][row + 3] == ' ') \
                        and (board.board[col + 1][row + 3] == ' '):
                    if (row % 4 == 0) and (col % 2 == 0):
                        val = 1
                        self.row = row
                        self.col = col

    def pos(self, board):
        ''' This sets the position '''
        for i in range(0, 2):
            for j in range(0, 4):
                if board.board[self.col + i][self.row + j] != 'e':
                    board.board[self.col + i][self.row + j] = 'E'

    def move(self, board):
        ''' This moves the enemy '''
        while True:
            ranx = randint(1, 4)
            self.status = -1
            if ranx == 1:
                if (board.board[self.col][self.row - 4] == ' ') \
                        and (board.board[self.col + 1][self.row - 4] == ' '):
                    self.row -= 4
                    self.status = 0
                elif (board.board[self.col][self.row - 4] == 'B') \
                        and (board.board[self.col + 1][self.row - 4] == 'B'):
                    self.row -= 4
                    self.status = 1
                elif (board.board[self.col][self.row - 4] == 'e') \
                        and (board.board[self.col + 1][self.row - 4] == 'e'):
                    self.row -= 4
                    self.life = 0
                    self.status = 0

            if ranx == 2:
                if (board.board[self.col][self.row + 7] == ' ') \
                        and (board.board[self.col + 1][self.row + 7] == ' '):
                    self.row += 4
                    self.status = 0
                elif (board.board[self.col][self.row + 7] == 'B') \
                        and (board.board[self.col + 1][self.row + 7] == 'B'):
                    self.row += 4
                    self.status = 1
                elif (board.board[self.col][self.row + 7] == 'e') \
                        and (board.board[self.col + 1][self.row + 7] == 'e'):
                    self.row += 4
                    self.life = 0
                    self.status = 0

            if ranx == 3:
                if (board.board[self.col - 2][self.row] == ' ') \
                        and (board.board[self.col - 2][self.row + 3] == ' '):
                    self.col -= 2
                    self.status = 0
                elif (board.board[self.col - 2][self.row] == 'B') \
                        and (board.board[self.col - 2][self.row + 3] == 'B'):
                    self.col -= 2
                    self.status = 1
                elif (board.board[self.col - 2][self.row] == 'e') \
                        and (board.board[self.col - 2][self.row + 3] == 'e'):
                    self.col -= 2
                    self.life = 0
                    self.status = 0

            if ranx == 4:
                if (board.board[self.col + 3][self.row] == ' ') \
                        and (board.board[self.col + 3][self.row + 3] == ' '):
                    self.col += 2
                    self.status = 0
                elif (board.board[self.col + 3][self.row] == 'B') \
                        and (board.board[self.col + 3][self.row + 3] == 'B'):
                    self.col += 2
                    self.status = 1
                elif (board.board[self.col + 3][self.row] == 'e') \
                        and (board.board[self.col + 3][self.row + 3] == 'e'):
                    self.col += 2
                    self.life = 0
                    self.status = 0

            if self.status == 0:
                return 0
            elif self.status == 1:
                return 1
