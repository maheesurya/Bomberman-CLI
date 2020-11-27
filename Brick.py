''' This is Brick file '''
from random import randint


class Brick(object):
    ''' This is Brick class '''
    def __init__(self, board):
        self.__align_bricks(board)
        self.cnt = 60
    @classmethod
    def __align_bricks(cls, board):
        val = 0
        while val != 60:
            row = randint(2, 89)
            col = randint(4, 37)
            if(board.board[col][row] == ' ') \
                and (board.board[col + 1][row] == ' ') \
                and (board.board[col][row + 3] == ' ') \
                    and (board.board[col + 1][row + 3] == ' '):
                if (row % 4 == 0) and (col % 2 == 0):
                    val += 1
                    for i in range(0, 2):
                        for j in range(0, 4):
                            board.board[col + i][row + j] = '\\'
    def dummy(self):
        ''' This is dummy '''
        pass
    def demmy(self):
        ''' This is demmy '''
        pass
