from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells =[]
        self._create_cells()

    
    def _create_cells(self):
        for _ in range(self.num_cols):
            column = []
            for _ in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cells(i,j)

    def _draw_cells(self, i, j):
        cell = self._cells[i][j]
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
   