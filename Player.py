from Board import *
from Tictac import *

class player:
    def __init__(self, board, win, is_player1=True):
        self.board=board
        self.win=win
        self.is_player1=is_player1
        self.i=0
        self.j=0
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
        self.j+=1
        self._location()
    def move_down(self):
        self._not_here()
        self.j-=1
        self._location()
class game(Tk):
    def __init__(self,board, win, player):
        self.board=board
        self.win=win
        self.player=player
        self.player._location(7,7)
        self.win.bind("<Left>", lambda event: self.player.move_left())
        self.bind("<Right>", lambda event: self.player.move_right())
        self.bind("<Up>", lambda event: self.player.move_up())
        self.bind("<Down>", lambda event: self.player.move_down())
        self.canvas = Canvas(self, width=board.num_cols * board.cell_size_x, 
        height=board.num_rows * board.cell_size_y)
        self.canvas.pack()
        self._play_game()
    def _play_game(self):
        self.mainloop()