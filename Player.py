from Board import *
from tkinter import Tk, BOTH, Canvas

class player:
    def __init__(self, board, win):
        self.board=board
        self.win=win
        self.is_player1=True
        self.i=7
        self.j=7
    def _location(self):
        if self.is_player1:
            oL="blue"
        else:
            oL="red"
        self.board._cells[self.i][self.j].player_here(oL)
    def _not_here(self):
        self.board._cells[self.i][self.j].player_leave()
    def _plant_move(self):
        color=self.board._cells[self.i][self.j]._cl
        if self.is_player1:
            if color=='none':
                self.board._cells[self.i][self.j].plant_b()
                self.is_player1=False
        else:
            if color=='none':
                self.board._cells[self.i][self.j].plant_w()
                self.is_player1=True
        curentclr=self.board._cells[self.i][self.j]._cl
        count = self.board.count_point(self.i,self.j,curentclr)
        if count==5: print("GAME end")
    def move_left(self):
        self._not_here()
        if self.i > 0:
            self.i-=1
        else: self.i=14
        self._location()
    def move_right(self):
        self._not_here()
        if self.i < 14:
            self.i+=1
        else: self.i=0
        self._location()
    def move_up(self):
        self._not_here()
        if self.j > 0:
            self.j-=1
        else: self.j=14
        self._location()
    def move_down(self):
        self._not_here()
        if self.j < 14:
            self.j+=1
        else: self.j=0
        self._location()

    
