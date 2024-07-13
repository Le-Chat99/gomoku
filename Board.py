from Cell import *
from window import *
import time
import random


class Board:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y,
            win
            ):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._create_cells()
    def _create_cells(self):
        self._cells=[]
        for i in range(self.num_cols):
            rows=[]
            for j in range(self.num_rows):
                x1=self.x1+(self.cell_size_x*i)
                x2=x1+self.cell_size_x
                y1=self.y1+(self.cell_size_y*j)
                y2=y1+self.cell_size_y
                C=Cell(x1,x2,y1,y2,self.win)
                rows.append(C)
            self._cells.append(rows)
        for i in range(self.num_cols):
            for j in range(self.num_rows):     
                self._draw_cell(i,j)       
    def _draw_cell(self,i,j):
        cell = self._cells[i][j]
        cell.Draw("grey")
        self._animate()
    def _animate(self):
        self.win.redraw()
        time.sleep(0.0001)