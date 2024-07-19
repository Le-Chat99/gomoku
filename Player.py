from Board import *
from Tictac import *
from tkinter import Tk, BOTH, Canvas

class player:
    def __init__(self, board, win, is_player1=True):
        self.board=board
        self.win=win
        self.is_player1=is_player1
        self.i=7
        self.j=7
    def _location(self):
        self.board._cells[self.i][self.j].player_here()
    def _not_here(self):
        self.board._cells[self.i][self.j].player_leave()
    def move_left(self):
        self._not_here()
        self.i-=1
        self._location()
    def move_right(self):
        self._not_here()
        self.i+=1
        self._location()
    def move_up(self):
        self._not_here()
        self.j-=1
        self._location()
    def move_down(self):
        self._not_here()
        self.j+=1
        self._location()

