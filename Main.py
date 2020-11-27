''' This file contains Main class '''
import tty
import termios
import sys
import os
from select import select
from threading import Timer
from Board import Board
from Wall import Walls
from Brick import Brick
from Bomber import Bomberman
from Bomb import Bomb
from Enemy import Enemy


class Main(object):
    ''' The main class '''
    def __init__(self):
        board = Board()
        self.done_val = 4
        self.time = 0
        self.init(board)
        self.iter = 0

    def __printer(self, board, bomber):
        os.system('clear')
        for item in range(board.height):
            print(''.join(board.board[item]))
        print("LIVES:", bomber.lives,
              "   ", "SCORE:", bomber.score, "   ", "TIME:", 200 - self.time)

    def __check(self, board, bomb, bomber):
        for posx in range(42):
            for posy in range(92):
                if (bomb.bomb[posx][posy] == 'O') and (board.board[posx][posy] == ' '):
                    board.board[posx][posy] = bomb.bomb[posx][posy]
        self.__printer(board, bomber)

    @classmethod
    def __getchar(cls):
        fild = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fild)
        try:
            tty.setraw(sys.stdin.fileno())
            if select([sys.stdin.fileno()], [], [], 0.8)[0]:
                char = sys.stdin.read(1)
            else:
                char = None
        finally:
            termios.tcsetattr(fild, termios.TCSADRAIN, old_settings)
        return char

    @classmethod
    def dum(cls, board):
        ''' This is a func '''
        Walls(board)
        Brick(board)

    @classmethod
    def printy(cls, val):
        ''' This is for printing '''
        if val == 0:
            print("\n")
            print("GAME OVER")
        elif val == 1:
            print("\n")
            print("SUCCESS")
            print("GAME COMPLETED")
            print("\n")

    def init(self, board):
        ''' This is init method '''
        self.dum(board)
        board.border()
        bomber = Bomberman()
        bomber.position(board)
        bomb = Bomb()
        os.system('clear')
        list_enem = []
        for i in range(0, 4):
            rem = Enemy(board)
            rem.pos(board)
            list_enem.append(rem)
        while True:
            self.time += 1
            self.__check(board, bomb, bomber)
            board.border()
            Walls(board)
            val = self.__getchar()
            if val == 'q':
                self.printy(0)
                break
            elif val == 'b':
                bomb.pos(bomber.row, bomber.col)
                timm = Timer(2, bomb.explode, [board, bomber, list_enem])
                timm.start()
            elif val is not None:
                bomber.move(board, val)
            bomber.position(board)
            done = []
            for i in range(self.done_val):
                done.append(0)
            self.iter = len(list_enem)
            for i in range(self.iter):
                if(bomber.row == list_enem[i].col) \
                and (bomber.col == list_enem[i].row):
                    bomber.lives = bomber.lives -1
                done[i] = list_enem[i].move(board)
                list_enem[i].pos(board)
            for i in range(self.done_val):
                if list_enem[i].life == 0:
                    del list_enem[i]
                    self.done_val -= 1
                    break
            if self.done_val == 0:
                self.printy(1)
                break
            if self.time == 0:
                print("\n GAME OVER \n")
                break
            if bomber.lives == 0:
                print("\n GAME OVER \n")
                break
            self.iter = len(list_enem)
            for i in range(self.iter):
                if done[i] == 1:
                    done[i] = 0
                    bomber.lives -= 1
                    bomber.row = 2
                    bomber.col = 4
                    bomber.position(board)
                    self.__check(board, bomb, bomber)
