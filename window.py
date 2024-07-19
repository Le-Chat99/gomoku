from tkinter import Tk, BOTH, Canvas
from Point import *

class Window:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.__root = Tk()  # Create the root window
        self.__root.title("GomokuMaster10.000")  # Set the title
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
        self.canvas= Canvas(self.__root, width=self.width, height=self.height, bg='white')
        self.canvas.pack(fill=BOTH, expand=True)
        self.running=False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update() 

    def wait_for_close(self):
        self.running=True
        while self.running:
            self.redraw()
    def close(self):
        self.running=False

    def draw_line(self, Line, fill_color):
        Line.draw(self.canvas, fill_color)

    def game_control(self,player):
        self.__root.bind("a", lambda event: player.move_left())
        self.__root.bind("d", lambda event: player.move_right())
        self.__root.bind("w", lambda event: player.move_up())
        self.__root.bind("s", lambda event: player.move_down())
        self.__root.bind("f", lambda event: player._plant_move())
        self.canvas.pack()