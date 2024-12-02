import copy

uppermost_row = 0

initial_state = [['e', 'e', 'e', 'e', 'e', 'e', 'e'],
                 ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
                 ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
                 ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
                 ['e', 'e', 'e', 'e', 'e', 'e', 'e'],
                 ['e', 'e', 'e', 'e', 'e', 'e', 'e']]


def heuristic(state):
    return ord(state[5][0]) - ord('a')


def terminal(state):
    for col in range(7):
        if state[0][col] == 'e':
            return False
    return True


def next_state(state, column, player):  # uppermost
    for row in range(5, -1, -1):
        if state[row][column] == 'e':
            state[row][column] = player
            return state


def print_state(state):
    for row in state:
        print(row)


def maximize(state, depth, pruning, alpha, beta, heuristic_map, print_list, pre_col):
    if terminal(state) or depth == 1:
        print_list.append([pre_col, depth, f'H = {heuristic(state)}'])
        return heuristic(state), None

    max_utility, best_column = -1 * 2 ** 30, None
    index = len(print_list)
    print_list.append([pre_col, depth])
    equal = True

    for col in range(7):
        if state[uppermost_row][col] != 'e':
            continue

        state2 = copy.deepcopy(state)
        next_state(state2, col, 'a')

        if str(state2) in heuristic_map:
            utility = heuristic_map[str(state2)]
        else:
            utility, _ = minimize(state2, depth - 1, pruning, alpha, beta, heuristic_map, print_list, col)

        if utility > max_utility:
            max_utility, best_column = utility, col

        if pruning and utility >= beta:
            equal = False
            break
        if pruning and alpha < utility:
            alpha = utility

    heuristic_map[str(state)] = max_utility
    if equal:
        print_list[index].append(f'H = {max_utility}')
    else:
        print_list[index].append(f'H >= {max_utility}')
    return max_utility, best_column


def minimize(state, depth, pruning, alpha, beta, heuristic_map, print_list, pre_col):
    if terminal(state) or depth == 1:
        print_list.append([pre_col, depth, f'H = {heuristic(state)}'])
        return heuristic(state), None

    min_utility, best_column = 2 ** 30, None
    index = len(print_list)
    print_list.append([pre_col, depth])
    equal = True

    for col in range(7):
        if state[uppermost_row][col] != 'e':
            continue

        state2 = copy.deepcopy(state)
        next_state(state2, col, 'p')

        if str(state2) in heuristic_map:
            utility = heuristic_map[str(state2)]
        else:
            utility, _ = maximize(state2, depth - 1, pruning, alpha, beta, heuristic_map, print_list, col)

        if utility < min_utility:
            min_utility, best_column = utility, col

        if pruning and utility <= alpha:
            equal = False
            break
        if pruning and beta > utility:
            beta = utility

    heuristic_map[str(state)] = min_utility
    if equal:
        print_list[index].append(f'H = {min_utility}')
    else:
        print_list[index].append(f'H <= {min_utility}')
    return min_utility, best_column


def minimax(state, k, pruning):
    heuristic_map = {}
    print_list = []
    utility, column = maximize(state, k, pruning, -1 * 2 ** 30, 2 ** 30, heuristic_map, print_list, -1)

    for [col, depth, value] in print_list:
        if col == -1:
            print(f'Root, {value}')
        else:
            print(((k - depth) * 2) * " " + f'col = {col}, {value}')

    print(f'The Agent plays in column {column}')


minimax(initial_state, 4, True)
