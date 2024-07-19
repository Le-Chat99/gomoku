from Board import *
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
    def _plant_move(self):
        self.board._cells[self.i][self.j].plant_b()
    def move_left(self):
        self._not_here()
        if self.i > 0:
            self.i-=1
        self._location()
    def move_right(self):
        self._not_here()
        if self.i < 14:
            self.i+=1
        self._location()
    def move_up(self):
        self._not_here()
        if self.j > 0:
            self.j-=1
        self._location()
    def move_down(self):
        self._not_here()
        if self.j < 14:
            self.j+=1
        self._location()


