from Board import *
from Tictac import *

class player:
    def __init__(self, board, win, is_player1=True):
        self.board=board
        self.win=win
        self.is_player1=is_player1
    def _location(self,i,j):
        self.board._cells[i][j].player_here()
    def _move(self,i,j):
        self.board._cells[i][j].player_leave()
        self.board._cells[i+5][j].player_here()
