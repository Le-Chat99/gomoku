
class Tictac:
    def __init__(self, x, y, win,is_o=False):
        self.x=x
        self.y=y
        self.win=win
        self.is_o=is_o
    
    def _draw_move(self):
        radius=7
        if self.is_o:
            self.win.canvas.create_oval(self.x - radius, self.y - radius, self.x + radius, self.y + radius, outline='red', width=2)
        else:
            self.win.canvas.create_line(self.x - radius, self.y - radius, self.y + radius, self.y + radius, outline='blue', width=2)
            self.win.canvas.create_line(self.x + radius, self.y - radius, self.y - radius, self.y + radius, outline='blue', width=2)
        