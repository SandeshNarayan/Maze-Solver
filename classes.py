from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas(self.root, width=width, height=height)
        self.root.title("Maze")
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def draw(self, canvas , fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width = 2)

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        fill = "black"
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        

        if self.has_left_wall:
            line = Line(x1,y1,x1,y2)
            self._win.draw_line(line, fill)

        if self.has_right_wall:
            line = Line(x2,y1,x2,y2)
            self._win.draw_line(line, fill)

        if self.has_top_wall:
            line = Line(x1,y1,x2,y1)
            self._win.draw_line(line, fill)

        if self.has_bottom_wall:
            line = Line(x1,y2,x2,y2)
            self._win.draw_line(line, fill)


    def draw_move(self, to_cell, undo = False):
        if undo == False:
            fill = "grey"
        else:
            fill = "red"

        line = Line((self._x1+self._x2)/2, (self._y1+self._y2)/2, (to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        
        self._win.draw_line(line, fill)

        