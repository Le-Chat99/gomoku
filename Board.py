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
        time.sleep(0.001)

    def count_point(self,i,j,curentclr,count=1):
        directs=[[1,0,-1,0],[0,1,0,-1],[1,1,-1,-1], [-1,+1,+1,-1]]
        for i1,j1,i2,j2 in directs:
            temcount=1
            ni,nj=i,j
            while self.dicect_advance(ni,nj,i1,j1,curentclr):
                temcount+=1
                ni,nj=ni+i1,nj+j1
            ni,nj=i,j
            while self.dicect_advance(ni,nj,i2,j2,curentclr):
                temcount+=1
                ni,nj=ni+i2,nj+j2

            if temcount> count: count=temcount
        return count
    
    def dicect_advance(self,i,j,si,sj,curentclr):
        
        ni=i+si
        nj=j+sj
        print(f"{ni},{nj}")
        if ni < 0 or ni >= 15 or nj < 0 or nj >= 15:
            return False
        if self._cells[ni][nj]._cl!=curentclr:
            return False
        return True
