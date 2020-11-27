#!/usr/bin/python
''' This file sets the walls on the board '''
class Walls:
    ''' This class contains 2 private methods and 2 dummy public methods '''
    def __init__(self, board):
        self.__wall(board)

    @classmethod
    def __wall(cls, board):
        for col in range(2, board.height - 2):
            if (col % 4 == 0) or (col % 4 == 1):
                for row in range(4, board.width - 4):
                    if (row % 8 == 0) or (row % 8 == 1) \
                            or (row % 8 == 2) or (row % 8 == 3):
                        board.board[col][row] = 'X'

    def dumm1(self):
        ''' This is the first dummy method '''
        pass

    def dumm2(self):
        ''' This is the second dummy method '''
        pass
