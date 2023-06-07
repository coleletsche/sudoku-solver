
# Sudoku Solver with GUI

This script is a Sudoku solver that provides a graphical user interface (GUI) using Pygame. 

## Functionality

1. Imports the `pygame` module for creating the GUI.

2. Defines a `Cell` class to represent each cell in the Sudoku grid. This class includes properties for the row and column of the cell, the number in the cell, whether the cell is highlighted, and methods for rendering the cell in the GUI.

3. Defines several functions:
   - `board_to_string()`: Prints the current Sudoku grid to the console.
   - `render_cells()`: Calls the render method of each cell in the grid, drawing it to the GUI.
   - `render_lines()`: Draws the grid lines on the GUI.
   - `is_valid_choice(rowNum, colNum, num)`: Checks if a number can be placed at a certain position in the grid without breaking the Sudoku rules.
   - `solve()`: Recursively tries to solve the Sudoku puzzle by filling in numbers and backtracking when it reaches a dead end.

4. Reads the initial state of the Sudoku grid from a text file specified by the user.

5. Creates a Pygame window and enters a game loop where it:
   - Checks for the Pygame QUIT event (closing the window) and exits the loop if it occurs.
   - Checks if the space bar is pressed and if the puzzle has not been solved yet. If so, it calls the solve function and prints the solved puzzle to the console.
   - Renders the cells and lines of the grid to the GUI.
   - Updates the Pygame display.

## Requirements

- Python 3
- `pygame` module

## Usage

Run the script with Python and provide the name of the text file containing the initial state of the Sudoku grid when prompted:

```
python main.py
```

Press the space bar in the Pygame window to solve the puzzle.
