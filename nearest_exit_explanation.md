# Nearest Exit in Maze - Implementation Explanation

## Problem Understanding
We need to find the shortest path from a given entrance to any exit in a maze where:
- `.` represents empty cells (walkable)
- `+` represents walls (blocked)
- Exit = any empty cell on the border (except the entrance itself)
- We can move up, down, left, or right

## Implementation Step-by-Step

### 1. Algorithm Choice: BFS (Breadth-First Search)
BFS guarantees finding the shortest path in an unweighted graph, which is perfect for this problem.

### 2. Implementation Details

```python
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
```

#### Step 1: Initialize Variables
```python
m, n = len(maze), len(maze[0])  # Get maze dimensions
start_row, start_col = entrance  # Extract starting position
```

#### Step 2: Set up BFS Data Structures
```python
queue = deque([(start_row, start_col, 0)])  # (row, col, steps)
visited = {(start_row, start_col)}  # Track visited cells
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
```

#### Step 3: BFS Loop
```python
while queue:
    row, col, steps = queue.popleft()
```
- Process cells level by level (all cells at distance k before k+1)

#### Step 4: Check for Exit
```python
if steps > 0 and (row == 0 or row == m - 1 or col == 0 or col == n - 1):
    return steps
```
- `steps > 0`: Ensures we don't count entrance as exit
- Border check: Cell is on maze edge

#### Step 5: Explore Neighbors
```python
for dr, dc in directions:
    new_row, new_col = row + dr, col + dc
    
    if (0 <= new_row < m and 0 <= new_col < n and 
        maze[new_row][new_col] == '.' and 
        (new_row, new_col) not in visited):
        
        visited.add((new_row, new_col))
        queue.append((new_row, new_col, steps + 1))
```
- Check boundaries
- Ensure cell is empty (not a wall)
- Avoid revisiting cells

#### Step 6: No Path Found
```python
return -1  # If queue empties without finding exit
```

## Alternative Approaches Considered

### 1. DFS (Depth-First Search)
- **Pros**: Uses less memory (O(min(m,n)) vs O(m*n))
- **Cons**: Doesn't guarantee shortest path
- **Verdict**: Rejected because we need the shortest path

### 2. Dijkstra's Algorithm
- **Pros**: Works for weighted graphs
- **Cons**: Overkill for unweighted graph, same complexity as BFS
- **Verdict**: Unnecessary complexity

### 3. A* Algorithm
- **Pros**: Can be faster with good heuristic
- **Cons**: Hard to design good heuristic for "nearest exit" (multiple targets)
- **Verdict**: Not beneficial for this problem

### 4. Multi-source BFS
- **Approach**: Start from all exits simultaneously, find entrance
- **Pros**: Elegant when many entrances, few exits
- **Cons**: More complex, same time complexity
- **Verdict**: Standard BFS is simpler and equally efficient

## Complexity Analysis

### Time Complexity: O(m × n)
- Worst case: Visit every cell in the maze
- Each cell is visited at most once

### Space Complexity: O(m × n)
- Queue can contain up to O(m × n) cells
- Visited set stores up to O(m × n) cells

## Edge Cases Handled

1. **Entrance is already an exit**: Check `steps > 0`
2. **No path exists**: Return -1 when queue is empty
3. **Single cell maze**: Works correctly
4. **Maze with all walls except entrance**: Returns -1
5. **Multiple exits**: Finds the nearest one due to BFS