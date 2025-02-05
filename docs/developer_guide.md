Developer Guide

    Project Structure

    The Maze Solver project is organized as follows:

    maze-solver/
    ├── graphics.py      # Contains core classes like Window, Line, and Point
    ├── main.py          # Entry point for running the application
    ├── README.md        # Project overview and basic usage instruction
    ├── cell.py          # Contains Cell class and its methods
    ├── maze.py          # Contains Maze class and its methods
    ├── tests.py         # Contains tests
    └── .gitignore       # Files to be ignored by Git

    Prerequisites

        Ensure you have the following before working on development:

            Python 3.10 or later

            Tkinter library

            Git for version control

        Setting Up the Development Environment

            Clone the repository:

                git clone https://github.com/yourusername/maze-solver.git

                Navigate to the project folder:

                cd maze-solver

            Install dependencies (if applicable):

                pip install -r requirements.txt

    Code Structure

        Window Class

            Manages the graphical window and drawing operations.

        Line Class

            Handles drawing lines on the canvas.

        Cell Class

            Represents an individual maze cell with walls and drawing logic.

        main.py

            The main entry point that initializes the window and generates the maze.

        Maze Class

            Represents etire maze grid



    Future Enhancements

        Implement maze-solving algorithms.

        Improve UI with better visualization.

        Optimize performance for larger mazes.


    Window


        Constructor

            __init__(self, width, height)

            Parameters:

                width (int): The width of the window in pixels.

                height (int): The height of the window in pixels.

            Description:

                Initializes a new window using Tkinter.

                Creates a canvas inside the window.

                Sets the window title to "Maze".

                Enables automatic resizing of the canvas.

                Defines a protocol to handle window closure.

            Code:

                self.root = Tk()
                self.canvas = Canvas(self.root, width=width, height=height)
                self.root.title("Maze")
                self.canvas.pack(fill=BOTH, expand=True)
                self.running = False
                self.root.protocol("WM_DELETE_WINDOW", self.close)

        Methods

            redraw(self)

                Description:

                    Updates the graphical window to reflect any changes.

                Code:

                    self.root.update_idletasks()
                    self.root.update()

            wait_for_close(self)

                Description:

                    Keeps the window running until closed.

                Code:

                    self.running = True
                    while self.running:
                        self.redraw()

            close(self)

                Description:

                    Stops the window loop and allows closure.

                Code:

                    self.running = False

            draw_line(self, line, fill_color)

                Parameters:

                    line (Line object): The line to be drawn.

                    fill_color (str): The color of the line.

                Description:

                    Draws a line on the canvas using the given color.

                Code:

                    line.draw(self.canvas, fill_color)

    Point
        Represent a point in 2D coordinate

        Constructor
            def __init__(self, x, y)

            Parameters:
                x (int/float): X-coordinate of the point.
                y (int/float): Y-coordinate of the point.

    Line 
        Represents a straight line between two points

        Constructor
            def __init__(self, x1, y1, x2, y2)

            Parameters:
                x1, y1 (int/float): Coordinates of the starting point.
                x2, y2 (int/float): Coordinates of the ending point.

        Methods:
            draw(canvas, fill_color)
                Draws the line on a given canvas.

                Parameters: 
                    canvas (Canvas): A Tkinter Canvas object where the line is drawn.
                    fill_color (str): The color of the line (e.g., "black", "red").


    Cell
        The Cell class represents a single unit within a grid-based maze. It maintains information about its position, walls, and whether it has been visited. It also provides methods for drawing the cell and visualizing movement.

        Constructor:
            def __init__(self, win=None)
        
        Parameters
            win (Window): An optional window object where the cell will be drawn.

        Attributes
            has_left_wall, 
            has_right_wall, 
            has_top_wall, 
            has_bottom_wall (bool): Booleans indicating whether each wall exists.


            _x1, 
            _x2, 
            _y1, 
            _y2 (int/float): Coordinates defining the cell's boundaries.
            
            visited (bool): Marks if the cell has been visited.

        Metods:

            draw(x1, y1, x2, y2)
                Draws the cell, including its walls, within the specified coordinates.

                Parameters
                    x1, y1, x2, y2 (int/float): The bounding coordinates for the cell.
                    
                Walls are drawn in black ("black") if present; otherwise, they are erased ("#d9d9d9").

            draw_move(to_cell, undo=False)
                Draws a move from the current cell to the target cell, visualizing movement.

                Parameters
                    to_cell (Cell): The destination cell.
                    undo (bool, default=False): If True, the move is drawn in red ("red") to indicate backtracking; otherwise, it is drawn in gray ("grey").

            
    Maze Class 

        Overview

            The Maze class is responsible for generating a random maze using a recursive backtracking algorithm. It allows for visualization using a graphical window, and it maintains a grid of Cell objects, each representing an individual maze cell.

        Initialization

            __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None)

                Initializes the Maze instance with the given parameters.

            Parameters:

                x1 (int): The x-coordinate of the top-left corner of the maze.

                y1 (int): The y-coordinate of the top-left corner of the maze.

                num_rows (int): The number of rows in the maze.

                num_cols (int): The number of columns in the maze.

                cell_size_x (int): The width of each cell.

                cell_size_y (int): The height of each cell.

                win (object, optional): A window object for visualization.

                seed (int, optional): A seed value for randomization.

        Private Methods

            _create_cells(self)

                Creates a 2D list of Cell objects representing the maze grid and initializes their drawing.

            _draw_cells(self, i, j)

                Draws a cell at position (i, j) in the grid if a graphical window is provided.

                Parameters:

                    i (int): Column index of the cell.

                    j (int): Row index of the cell.

            _animate(self)

                Redraws the graphical window with a short delay to visualize the maze generation.

            _break_entrance_and_exit(self)

                Removes the top wall of the starting cell (0,0) and the bottom wall of the exit cell (num_cols-1, num_rows-1) to create an entrance and exit.

            _break_walls_r(self, i, j)

                Recursively breaks walls between neighboring cells using a depth-first search approach to generate a solvable maze.

                Parameters:

                    i (int): Column index of the current cell.

                    j (int): Row index of the current cell.

                Process:

                    Marks the current cell as visited.

                    Determines possible neighboring cells that have not been visited.

                    Randomly selects a neighboring cell and removes the wall between the current and next cell.

                    Recursively repeats the process until all cells are visited.

            _reset_cells_visited(self)
                Resets the 'visited' attribute of all cells in the maze to False.
                This method is used to prepare the maze for a new maze generation or a new maze solving process.
                It iterates through all cells in the maze and sets their 'visited' attribute to False.
