
weights = [
    [3, 4, 5, 7, 5, 4, 3],
    [4, 6, 8, 10, 8, 6, 4],
    [5, 8, 11, 13, 11, 8, 5],
    [5, 8, 11, 13, 11, 8, 5],
    [4, 6, 8, 10, 8, 6, 4],
    [3, 4, 5, 7, 5, 4, 3],
]

def heuristic_evaluation(grid_string, weights, width=7):
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

def string_to_grid(grid_string, width=7):
    return [list(grid_string[i:i+width]) for i in range(0, len(grid_string), width)]

