from helperFunctions import *


def calculate_column_probabilities(chosen_col):
    probabilities = {
        'chosen': 0.6,   # Base probability for chosen column
        'neighbor_left': 0.0,  # Probability for left neighbor
        'neighbor_right': 0.0  # Probability for right neighbor
    }
    
    # Determine probabilities based on column position
    if chosen_col == 0:  # Leftmost column
        probabilities['chosen'] = 0.6
        probabilities['neighbor_right'] = 0.4
    elif chosen_col == 6:  # Rightmost column
        probabilities['chosen'] = 0.6
        probabilities['neighbor_left'] = 0.4
    else:  # Middle columns
        probabilities['chosen'] = 0.6
        probabilities['neighbor_left'] = 0.2
        probabilities['neighbor_right'] = 0.2
    
    return probabilities

def log_step(depth, node_type, col, score=None, probs=None, chosen_col=None):
    """
    Logs the details of each step in a structured and beautiful way.
    """
    indent = "  " * (3 - depth)  # Indent based on the depth for clarity
    print(f"{indent}Depth: {depth}, Node Type: {node_type.upper()}")
    
    if col is not None:
        print(f"{indent}  Evaluating Column: {col + 1} (Index {col})")
    
    if chosen_col is not None:
        print(f"{indent}  Chosen Column for Chance: {chosen_col + 1} (Index {chosen_col})")
    
    if probs:
        print(f"{indent}  Probabilities: {probs}")
    
    if score is not None:
        print(f"{indent}  Score: {score}")
    
    print(f"{indent}{'-' * 40}")

def expectiminimax(grid_string, depth, node_type, chosen_col=None):
    if depth == 0 or game_over(grid_string):
        score = heuristic_evaluation(grid_string)
        log_step(depth, node_type, None, score=score)
        return score, None

    if node_type == "max":  # Max Node (AI's turn)
        best_score = float('-inf')
        best_move = None
        for col in range(7):
            new_grid = drop_disc(grid_string, col, 'a')
            if new_grid:
                log_step(depth, node_type, col)
                score, _ = expectiminimax(
                    new_grid, depth - 1, "chance", chosen_col=col
                )
                if score > best_score:
                    best_score = score
                    best_move = col
        return best_score, best_move

    elif node_type == "min":  # Min Node (Opponent's turn)
        best_score = float('inf')
        best_move = None
        for col in range(7):
            new_grid = drop_disc(grid_string, col, 'p')
            if new_grid:
                log_step(depth, node_type, col)
                score, _ = expectiminimax(
                    new_grid, depth - 1, "chance", chosen_col=col
                )
                if score < best_score:
                    best_score = score
                    best_move = col
        return best_score, best_move

    elif node_type == "chance":  # Chance Node
        if chosen_col is None:
            chosen_col = 7 // 2  # Default to middle column
        
        probs = calculate_column_probabilities(chosen_col)
        log_step(depth, node_type, None, probs=probs, chosen_col=chosen_col)
        
        total_score = 0.0
        for col in range(7):
            new_grid = drop_disc(grid_string, col, 'a' if depth % 2 == 0 else 'p')
            if new_grid:
                prob = probs['chosen'] if col == chosen_col else (
                    probs['neighbor_left'] if col == chosen_col - 1 else (
                        probs['neighbor_right'] if col == chosen_col + 1 else 0.0))
                
                score, _ = expectiminimax(
                    new_grid, depth - 1, 
                    "min" if depth % 2 == 0 else "max", chosen_col=col
                )
                total_score += prob * score

        log_step(depth, node_type, None, score=total_score)
        return total_score, None


def expectiminimax_2d(grid, depth):
    """
    Wrapper to handle 2D grid input for Expectiminimax algorithm
    """
    grid_string = grid_to_string(grid)
    return expectiminimax(grid_string, depth, "max" , None)

grid = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e']
]


depth = 3

# Run the algorithm with beautiful logging
best_score, best_move = expectiminimax_2d(grid, depth)
print(f"\nFinal Decision:")
print(f"Best score for AI: {best_score}")
print(f"Best move for AI: {best_move + 1} (Column {best_move})")