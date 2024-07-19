from window import *
from Point import *
from Cell import *
from Board import *
from Player import *
def main():
    win = Window(800, 800)
    num_cols = 15
    num_rows = 15
    Br = Board(100, 100, num_rows, num_cols, 40, 40,win)
    Plr= player(Br, win)
    Plr._plant_move()
    win.game_control(Plr)
    win.wait_for_close()


main()