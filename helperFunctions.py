

def heuristic_evaluation(grid_string):
    width=7
    weights = [
        [3, 4, 5, 7, 5, 4, 3],
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8, 11, 13, 11, 8, 5],
        [5, 8, 11, 13, 11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5, 7, 5, 4, 3],
    ]
    height = len(weights)  # Number of rows
    score = 0

    for idx, cell in enumerate(grid_string):
        row = idx // width  # Compute row index
        col = idx % width   # Compute column index
        
        if cell == 'a':  # AI piece
            score += weights[row][col]
        elif cell == 'p':  # Player piece
            score -= weights[row][col]

    return score

def grid_to_string(grid):
    return ''.join([''.join(row) for row in grid])

def string_to_grid(grid_string):
    width=7
    return [list(grid_string[i:i+width]) for i in range(0, len(grid_string), width)]

def drop_disc(grid_string, column, disc):
    width=7
    grid = string_to_grid(grid_string)
    for row in reversed(range(len(grid))):  # Start from bottom row
        if grid[row][column] == 'e':  # Find the first empty slot
            grid[row][column] = disc
            return grid_to_string(grid)  # Return new grid as string
    return None  # Invalid move if column is full

def game_over(grid_string):
    width=7
    height=6
    # Convert string to 2D grid
    grid = string_to_grid(grid_string)

    # Check for a winning line
    if check_victory(grid, 'a') or check_victory(grid, 'p'):
        return True

    # Check if the board is full
    if all(cell != 'e' for cell in grid_string):
        return True

    return False

def check_victory(grid, disc):
    width = len(grid[0])
    height = len(grid)

    # Check horizontal lines
    for row in range(height):
        for col in range(width - 3):  # Ensure there are enough columns left
            if all(grid[row][col + i] == disc for i in range(4)):
                return True

    # Check vertical lines
    for col in range(width):
        for row in range(height - 3):  # Ensure there are enough rows left
            if all(grid[row + i][col] == disc for i in range(4)):
                return True

    # Check diagonal lines (bottom-left to top-right)
    for row in range(height - 3):
        for col in range(width - 3):
            if all(grid[row + i][col + i] == disc for i in range(4)):
                return True

    # Check diagonal lines (top-left to bottom-right)
    for row in range(3, height):
        for col in range(width - 3):
            if all(grid[row - i][col + i] == disc for i in range(4)):
                return True

    return False
