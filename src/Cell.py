from Point import *
import time


class Cell:
    def __init__(self, x1,x2,y1,y2,win):
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
        self._win=win
        self.visited=False
        self._cl='none'

    def Draw(self, fill_color):
        def bleh():
            p1=Point(self._x1, self._y1)
            p2=Point(self._x1, self._y2)
            Line(p1,p2).draw(self._win.canvas, fill_color)
            
            p1=Point(self._x2, self._y1)
            p2=Point(self._x2, self._y2)
            Line(p1,p2).draw(self._win.canvas, fill_color)

            p1=Point(self._x1, self._y1)
            p2=Point(self._x2, self._y1)
            Line(p1,p2).draw(self._win.canvas, fill_color)

            p1=Point(self._x1, self._y2)
            p2=Point(self._x2, self._y2)
            Line(p1,p2).draw(self._win.canvas, fill_color)
        self._win.canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, fill = None)
    def draw_move(self, to_cell):
        fill_color="red"
        x1= (self._x1 + self._x2)/2
        y1= (self._y1 + self._y2)/2
        x2= (to_cell._x1 + to_cell._x2)/2
        y2= (to_cell._y1 + to_cell._y2)/2
        p1=Point(x1,y1)
        p2=Point(x2,y2)
        Line(p1,p2).draw(self._win.canvas,fill_color)
    def player_here(self,oL):
        self.visited=True
        self.rec_p = self._win.canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, width=3, outline=oL)

        
    def player_leave(self):
        if self.visited:
            self._win.canvas.delete(self.rec_p)
            self.visited=False

    def plant_b(self):
        self._cl='bl'
        self._win.canvas.create_oval(self._x1+3, self._y1+3, self._x2-3, self._y2-3, fill= "black")
    def plant_w(self):
        self._cl='wh'
        self._win.canvas.create_oval(self._x1+3, self._y1+3, self._x2-3, self._y2-3, fill= "white")
