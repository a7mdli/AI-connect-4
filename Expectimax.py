from helperFunctions import *

probabilities = {
    'chosen': 0.6,   # Probability of disc falling in chosen column
    'neighbor': 0.2  # Probability of disc falling into neighboring columns
}

def expectiminimax(grid_string, depth, is_max, probabilities, width=7):
    if depth == 0 or game_over(grid_string):  # Base case
        return heuristic_evaluation(grid_string, weights)  # Use our heuristic

    if is_max:  # Max Node (AI's turn)
        best_score = float('-inf')
        for col in range(width):
            new_grid = drop_disc(grid_string, col, 'a', width)
            if new_grid:
                score = expectiminimax(new_grid, depth - 1, False, probabilities, width)
                best_score = max(best_score, score)
        return best_score

    elif not is_max:  # Min Node (Player's turn)
        best_score = float('inf')
        for col in range(width):
            new_grid = drop_disc(grid_string, col, 'p', width)
            if new_grid:
                score = expectiminimax(new_grid, depth - 1, "chance", probabilities, width)
                best_score = min(best_score, score)
        return best_score

    else:  # Chance Node
        total_score = 0
        for col in range(width):
            new_grid = drop_disc(grid_string, col, 'a', width)
            if new_grid:
                probability = (
                    probabilities['chosen'] if col == current_col else probabilities['neighbor']
                )
                total_score += probability * expectiminimax(new_grid, depth - 1, True, probabilities, width)
        return total_score
