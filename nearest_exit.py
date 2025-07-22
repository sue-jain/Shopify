from collections import deque
from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    """
    Find the shortest path from entrance to nearest exit in a maze.
    
    Args:
        maze: 2D grid with '.' as empty cells and '+' as walls
        entrance: Starting position [row, col]
    
    Returns:
        Number of steps to nearest exit, or -1 if no path exists
    """
    m, n = len(maze), len(maze[0])
    start_row, start_col = entrance
    
    # BFS queue: (row, col, steps)
    queue = deque([(start_row, start_col, 0)])
    visited = {(start_row, start_col)}
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col, steps = queue.popleft()
        
        # Check if current position is an exit (border cell, not entrance)
        if steps > 0 and (row == 0 or row == m - 1 or col == 0 or col == n - 1):
            return steps
        
        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check boundaries and if cell is valid
            if (0 <= new_row < m and 0 <= new_col < n and 
                maze[new_row][new_col] == '.' and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    
    return -1


# Test with the example
if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1, 2]
    result = nearestExit(maze, entrance)
    print(f"Example 1: {result}")  # Expected: 1
    
    # Additional test cases
    maze2 = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance2 = [1, 0]
    result2 = nearestExit(maze2, entrance2)
    print(f"Example 2: {result2}")  # Expected: 2
    
    maze3 = [[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]]
    entrance3 = [0, 4]
    result3 = nearestExit(maze3, entrance3)
    print(f"Example 3: {result3}")  # Expected: 0 (already at exit)