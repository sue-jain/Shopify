import unittest
from nearest_exit import nearestExit


class TestNearestExit(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example case"""
        maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
        entrance = [1, 2]
        self.assertEqual(nearestExit(maze, entrance), 1)
    
    def test_entrance_already_at_exit(self):
        """Test when entrance is at the border (should not count as exit)"""
        maze = [[".",".","."],[".",".","."],[".",".","."]]
        entrance = [0, 0]
        self.assertEqual(nearestExit(maze, entrance), 1)
    
    def test_no_exit_available(self):
        """Test when no exit is reachable"""
        maze = [["+","+","+"],[".",".","+"],["+","+","+"]]
        entrance = [1, 0]
        self.assertEqual(nearestExit(maze, entrance), -1)
    
    def test_single_cell_maze_with_wall(self):
        """Test 1x1 maze with wall"""
        maze = [["+"]]
        entrance = [0, 0]
        # This should raise an error or return -1 since entrance is a wall
        # But based on problem constraints, entrance is always empty
        # So this is an invalid test case
    
    def test_single_cell_maze_empty(self):
        """Test 1x1 maze with empty cell"""
        maze = [["."]]
        entrance = [0, 0]
        # Single cell at border - entrance doesn't count as exit
        self.assertEqual(nearestExit(maze, entrance), -1)
    
    def test_multiple_exits_choose_nearest(self):
        """Test maze with multiple exits"""
        maze = [
            [".", ".", ".", "."],
            ["+", ".", "+", "."],
            [".", ".", ".", "."],
            [".", "+", "+", "."]
        ]
        entrance = [1, 1]
        # Nearest exit should be at [0,1] which is 1 step up
        self.assertEqual(nearestExit(maze, entrance), 1)
    
    def test_long_path_to_exit(self):
        """Test maze requiring longer path"""
        maze = [
            ["+", "+", "+", "+", "."],
            [".", ".", ".", "+", "."],
            ["+", "+", ".", "+", "."],
            ["+", "+", ".", ".", "."],
            ["+", "+", "+", "+", "."]
        ]
        entrance = [1, 0]
        # Must navigate through the maze to reach exit
        self.assertEqual(nearestExit(maze, entrance), 6)
    
    def test_large_empty_maze(self):
        """Test large maze with all empty cells"""
        maze = [["." for _ in range(10)] for _ in range(10)]
        entrance = [5, 5]
        # Nearest exit is 4 steps away (to any border)
        self.assertEqual(nearestExit(maze, entrance), 4)
    
    def test_maze_with_dead_ends(self):
        """Test maze with dead ends"""
        maze = [
            [".", "+", ".", "+", "."],
            [".", "+", ".", "+", "."],
            [".", ".", ".", ".", "."],
            ["+", "+", "+", "+", "."],
            [".", ".", ".", ".", "."]
        ]
        entrance = [2, 2]
        # Should find the nearest exit despite dead ends
        self.assertEqual(nearestExit(maze, entrance), 2)
    
    def test_entrance_surrounded_by_walls(self):
        """Test entrance completely surrounded by walls"""
        maze = [
            ["+", "+", "+"],
            ["+", ".", "+"],
            ["+", "+", "+"]
        ]
        entrance = [1, 1]
        self.assertEqual(nearestExit(maze, entrance), -1)
    
    def test_spiral_maze(self):
        """Test spiral-shaped maze"""
        maze = [
            [".", ".", ".", ".", "."],
            [".", "+", "+", "+", "."],
            [".", "+", ".", "+", "."],
            [".", "+", "+", "+", "."],
            [".", ".", ".", ".", "."]
        ]
        entrance = [2, 2]
        # Entrance is surrounded by walls - no exit possible
        self.assertEqual(nearestExit(maze, entrance), -1)
    
    def test_entrance_near_border(self):
        """Test entrance very close to border"""
        maze = [
            ["+", "+", "+", "+"],
            ["+", ".", ".", "."],
            ["+", ".", "+", "."],
            ["+", "+", "+", "."]
        ]
        entrance = [1, 1]
        # Nearest exit is at [1,3] which is 2 steps
        self.assertEqual(nearestExit(maze, entrance), 2)
    
    def test_rectangular_maze(self):
        """Test non-square maze"""
        maze = [
            [".", ".", ".", ".", ".", ".", "."],
            ["+", "+", "+", "+", "+", "+", "."],
            [".", ".", ".", ".", ".", ".", "."]
        ]
        entrance = [1, 0]
        # Entrance is surrounded by walls on left, must go up or down
        self.assertEqual(nearestExit(maze, entrance), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)