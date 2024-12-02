#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island described in grid.
    
    Args:
    grid (list of list of ints): A rectangular grid where 1 represents land and 0 represents water.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    
    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check the four sides of the land cell
                if i == 0 or grid[i - 1][j] == 0:  # Check above
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Check below
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1
                
    return perimeter
