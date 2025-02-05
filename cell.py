from graphics import Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        fill = "black"
        unfill = "#d9d9d9"
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if not self._win:
            return

        line = Line(x1,y1,x1,y2)
        if self.has_left_wall:
            self._win.draw_line(line, fill)
        else:
            self._win.draw_line(line, unfill)


        line = Line(x2,y1,x2,y2)
        if self.has_right_wall:
            self._win.draw_line(line, fill)
        else:
            self._win.draw_line(line, unfill)


        line = Line(x1,y1,x2,y1)
        if self.has_top_wall:
            self._win.draw_line(line, fill)
        else:
            self._win.draw_line(line, unfill)


        line = Line(x1,y2,x2,y2)
        if self.has_bottom_wall:
            self._win.draw_line(line, fill)
        else:
            self._win.draw_line(line, unfill)

    def draw_move(self, to_cell, undo = False):
        if not self._win:
            raise ValueError("Can't draw")
        
        if undo == False:
            fill = "grey"
        else:
            fill = "red"

        line = Line((self._x1+self._x2)/2, (self._y1+self._y2)/2, (to_cell._x1+to_cell._x2)/2, (to_cell._y1+to_cell._y2)/2)
        
        self._win.draw_line(line, fill)
