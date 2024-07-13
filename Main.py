from window import *
from Point import *
from Cell import *
from Board import *


win = Window(800, 800)
num_cols = 15
num_rows = 15
m1 = Board(100, 100, num_rows, num_cols, 40, 40,win)
win.wait_for_close()