import random

"""
CSC 412
2/18/2021
@author: Tomas Perez
"""

counter = 0
white_chess_queen = '\u2655'
empty_square = '\u25A1'
white_square_obstacle = '\u25a0'
main_board = []
solutions = []
size = 8
env = []
goal = None
goal_index = -1


def generate_board():
    chess_board = [
        [white_square_obstacle, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
         empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
         empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
         empty_square],
        [empty_square, empty_square, white_square_obstacle, empty_square, empty_square, empty_square,
         empty_square,
         empty_square],
        [empty_square, empty_square, white_square_obstacle, empty_square, empty_square, empty_square, empty_square,
         empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
         empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
         empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
         empty_square]]
    return chess_board


# FIXME: Used for testing
def print_board(user_board):
    for row in user_board:
        for c in row:
            print(c, end='')
        print('')


def is_optimal_solution_option(generation):
    if fitness_function(generation) == 0:
        return True
    return False


def populate_board(user_board, generation):
    for i in range(size):
        user_board[generation[i]][i] = white_chess_queen


def generate_initial_population():
    # generate the random list of boards
    dna = list(range(size))
    # FIXME: might not need this line...already calling in while dna loop below.
    random.shuffle(dna)
    while dna in env:
        random.shuffle(dna)
    return dna


# initialize with 100 for population size
def initialize_first_gen():
    for i in range(100):
        env.append(generate_initial_population())


def fitness_function(generation):
    hits = 0
    temp_board = generate_board()
    populate_board(temp_board, generation)
    for dna in generation:
        safe = is_safe(temp_board, generation[dna], dna)
        if safe is False:
            hits += 1
    return hits


# FIXME: need to update this where if a direction returns false, we increase the amount of hits
def is_safe(board, row, column):
    if board[row][column] == white_chess_queen or board[row][column] == white_square_obstacle:
        return False
    left_side_row = check_left_side_row(board, row, column)
    if left_side_row is False:
        return False
    right_side_row = check_right_side_row(board, row, column)
    if right_side_row is False:
        return False
    up_column = check_up_column(board, row, column)
    if up_column is False:
        return False
    down_column = check_down_column(board, row, column)
    if down_column is False:
        return False
    left_diagonal = check_left_diagonal(board, row, column)
    if left_diagonal is False:
        return False
    left_down_diagonal = check_left_down_diagonal(board, row, column)
    if left_down_diagonal is False:
        return False
    right_diagonal = check_right_diagonal(board, row, column)
    if right_diagonal is False:
        return False
    right_down_diagonal = check_right_down_diagonal(board, row, column)
    if right_down_diagonal is False:
        return False
    return True


def check_right_down_diagonal(board, row, column):
    if row != size - 1 and column != size - 1:
        temp_row = row + 1
        temp_column = column + 1
        while temp_row < size and temp_column < size:
            if board[temp_row][temp_column] == white_square_obstacle:
                return True
            elif board[temp_row][temp_column] == white_chess_queen:
                return False
            temp_row += 1
            temp_column += 1
    return True


def check_right_diagonal(board, row, column):
    if row != 0 and column != size - 1:
        temp_row = row - 1
        temp_column = column + 1
        while temp_row >= 0 and temp_column < size:
            if board[temp_row][temp_column] == white_square_obstacle:
                return True
            elif board[temp_row][temp_column] == white_chess_queen:
                return False
            temp_row -= 1
            temp_column += 1
    return True


def check_left_down_diagonal(board, row, column):
    if row != size - 1 and column != 0:
        temp_row = row + 1
        temp_column = column - 1
        while temp_row < size and temp_column >= 0:
            if board[temp_row][temp_column] == white_square_obstacle:
                return True
            elif board[temp_row][temp_column] == white_chess_queen:
                return False
            temp_row += 1
            temp_column -= 1
    return True


def check_left_diagonal(board, row, column):
    if row != 0 and column != 0:
        temp_row = row - 1
        temp_column = column - 1
        while temp_row >= 0 and temp_column >= 0:
            if board[temp_row][temp_column] == white_square_obstacle:
                return True
            elif board[temp_row][temp_column] == white_chess_queen:
                return False
            temp_row -= 1
            temp_column -= 1
    return True


def check_down_column(board, row, column):
    if row != size - 1:
        for i in range(row + 1, 1, 1):
            if board[row][column] == white_square_obstacle:
                return True
            elif board[row][column] == white_chess_queen:
                return False
        return True
    return True


def check_up_column(board, row, column):
    if row != 0:
        for i in range(row - 1, -1, -1):
            if board[row][column] == white_square_obstacle:
                return True
            elif board[row][column] == white_chess_queen:
                return False
        return True
    return True


def check_right_side_row(board, row, column):
    if column != size - 1:
        for i in range(column + 1, 1, size - 1):
            if board[row][column] == white_square_obstacle:
                return True
            elif board[row][column] == white_chess_queen:
                return False
        return True
    return True


def check_left_side_row(board, row, column):
    if column != 0:
        for i in range(column - 1, -1, -1):
            if board[row][column] == white_square_obstacle:
                return True
            elif board[row][column] == white_chess_queen:
                return False
        return True
    return True


def selection():
    all_fitness_results = []
    new_env = []
    for gen in env:
        all_fitness_results.append(fitness_function(gen))
    if min(all_fitness_results) == 0:
        goal_index = all_fitness_results.index(min(all_fitness_results))
        goal = env[goal_index]
        return env
    cross_over_function()


def cross_over_function():
    for i in range(1, len(env), 2):
        gen1 = env[i - 1][:]
        gen2 = env[i][:]
        breed(gen1, gen2)
        # include mutating here....
        env.append(gen1)
        env.append(gen2)


# FIXME: need to figure out how to swap genes...
def breed(gen1, gen2):


if __name__ == '__main__':
# main_board = generate_board()
# initialize_first_gen()
# boards = []
# for gen in env:
#     boards.append(populate_board(main_board, gen))
#     main_board = generate_board()
# for board in boards:
#     print_board(board)
#     print()
#     print()
