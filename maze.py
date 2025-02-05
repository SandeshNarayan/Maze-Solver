from cell import Cell
import time, random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed 
        if not self.seed:
            random.seed(self.seed)

        self._cells =[]
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()


    
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
        if not self.win:
            return
        cell = self._cells[i][j]
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.05)
   

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_left_cell = self._cells[self.num_cols-1][self.num_rows-1]

        top_left_cell.has_top_wall = False
        self._draw_cells(0, 0)
        bottom_left_cell.has_bottom_wall = False
        self._draw_cells(self.num_cols-1, self.num_rows-1)


    def _break_walls_r(self, i, j):
        if i < 0 or i >= self.num_cols or j < 0 or j >= self.num_rows:
            return
        cell = self._cells[i][j]
        if cell.visited:
            return
        cell.visited = True

        while True:
            possible_directions = []

            if i>0 and not self._cells[i-1][j].visited:
                possible_directions.append(("left", i-1, j))

            if i<self.num_cols-1 and not self._cells[i+1][j].visited:
                possible_directions.append(("right", i+1, j))

            if j>0 and not self._cells[i][j-1].visited:
                possible_directions.append(("top", i, j-1))

            if j<self.num_rows-1 and not self._cells[i][j+1].visited:
                possible_directions.append(("bottom", i, j+1))

            if not possible_directions:
                self._draw_cells(i,j)
                return

            direction, next_i, next_j = random.choice(possible_directions)





            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False  

            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False  

            elif direction == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False  

            elif direction == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False 

            self._draw_cells(i,j)
            self._break_walls_r(next_i,next_j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                cell = self._cells[i][j]
                cell.visited = False
        