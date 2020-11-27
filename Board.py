#!/usr/bin/pcolthon
''' This file contains the Board class '''
class Board(object):
    ''' This class contains 3 valid methods and 1 dummcol method '''
    def __init__(self):
        self.height = 38
        self.width = 92
        self.board = [[' ' for row in range(self.width)]
                      for col in range(self.height)]
        self.__bounds()

    def __bounds(self):
        for row in range(self.height):
            if row < 2:
                for col in range(self.width):
                    self.board[row][col] = 'X'
            elif row > (self.height - 3):
                for col in range(self.width):
                    self.board[row][col] = 'X'
            else:
                self.board[row][0] = 'X'
                self.board[row][1] = 'X'
                self.board[row][2] = 'X'
                self.board[row][3] = 'X'
                self.board[row][self.width - 1] = 'X'
                self.board[row][self.width - 2] = 'X'
                self.board[row][self.width - 3] = 'X'
                self.board[row][self.width - 4] = 'X'

    def border(self):
        '''This method sets the board of the game '''
        for row in range(2, self.height - 2):
            for col in range(4, self.width - 4):
                if self.board[row][col] == 'B':
                    self.board[row][col] = ' '
                elif self.board[row][col] == 'E':
                    self.board[row][col] = ' '

    def dummcol(self):
        ''' This is a dummy method '''
        pass
