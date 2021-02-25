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
iteration_count = 0
perform_mutation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


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
    # return user_board


def populate_final_board(generation):
    temp_board = generate_board()
    for i in range(size):
        temp_board[generation[i]][i] = white_chess_queen
    return temp_board


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
    gen_size = len(generation)
    for dna in range(gen_size):
        safe = is_safe(temp_board, generation[dna], dna)
        if safe is False:
            hits += 1
    return hits


# FIXME: need to update this where if a direction returns false, we increase the amount of hits
def is_safe(board, row, column):
    cell = board[row][column]
    if board[row][column] == white_square_obstacle:
        return False
    left_side_row = check_left_side_row(board, row, column)
    if left_side_row is False:
        return False
    # right_side_row = check_right_side_row(board, row, column)
    # if right_side_row is False:
    #     return False
    up_column = check_up_column(board, row, column)
    if up_column is False:
        return False
    # down_column = check_down_column(board, row, column)
    # if down_column is False:
    #     return False
    left_diagonal = check_left_diagonal(board, row, column)
    if left_diagonal is False:
        return False
    # left_down_diagonal = check_left_down_diagonal(board, row, column)
    # if left_down_diagonal is False:
    #     return False
    right_diagonal = check_right_diagonal(board, row, column)
    if right_diagonal is False:
        return False
    # right_down_diagonal = check_right_down_diagonal(board, row, column)
    # if right_down_diagonal is False:
    #     return False
    return True


# def check_right_down_diagonal(board, row, column):
#     if row != size - 1 and column != size - 1:
#         temp_row = row + 1
#         temp_column = column + 1
#         while temp_row < size and temp_column < size:
#             if board[temp_row][temp_column] == white_square_obstacle:
#                 return True
#             elif board[temp_row][temp_column] == white_chess_queen:
#                 return False
#             temp_row += 1
#             temp_column += 1
#     return True


# TODO: keep this one
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


# def check_left_down_diagonal(board, row, column):
#     if row != size - 1 and column != 0:
#         temp_row = row + 1
#         temp_column = column - 1
#         while temp_row < size and temp_column >= 0:
#             if board[temp_row][temp_column] == white_square_obstacle:
#                 return True
#             elif board[temp_row][temp_column] == white_chess_queen:
#                 return False
#             temp_row += 1
#             temp_column -= 1
#     return True


# TODO: keep this one
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


# def check_down_column(board, row, column):
#     if row != size - 1:
#         for i in range(row + 1, 1, 1):
#             if board[row][column] == white_square_obstacle:
#                 return True
#             elif board[row][column] == white_chess_queen:
#                 return False
#         return True
#     return True


# TODO: keep this one
def check_up_column(board, row, column):
    if row != 0:
        for i in range(row - 1, -1, -1):
            if board[i][column] == white_square_obstacle:
                return True
            elif board[i][column] == white_chess_queen:
                return False
        return True
    return True


# def check_right_side_row(board, row, column):
#     if column != size - 1:
#         for i in range(column + 1, 1, size - 1):
#             if board[row][column] == white_square_obstacle:
#                 return True
#             elif board[row][column] == white_chess_queen:
#                 return False
#         return True
#     return True


# TODO: keep this one
def check_left_side_row(board, row, column):
    if column != 0:
        for i in range(column - 1, -1, -1):
            if board[row][i] == white_square_obstacle:
                return True
            elif board[row][i] == white_chess_queen:
                return False
        return True
    return True


def selection():
    global goal_index
    global goal
    all_fitness_results = []
    new_env = []
    for gen in env:
        all_fitness_results.append(fitness_function(gen))
    if min(all_fitness_results) == 0:
        goal_index = all_fitness_results.index(min(all_fitness_results))
        goal = env[goal_index]
        return env
    smallest_fitness_function = None
    while len(new_env) < size:
        smallest_fitness_function = min(all_fitness_results)
        smallest_index = all_fitness_results.index(smallest_fitness_function)
        new_env.append(env[smallest_index])
        all_fitness_results.remove(smallest_fitness_function)
        env.remove(env[smallest_index])
    return new_env


def cross_over_function():
    for i in range(1, len(env), 2):
        gen1 = env[i - 1][:]
        gen2 = env[i][:]
        gen1, gen2 = breed(gen1, gen2)
        random.shuffle(perform_mutation)
        if perform_mutation[0] == 1:
            gen1, gen2 = mutate(gen1, gen2)
        env.append(gen1)
        env.append(gen2)


def mutate(gen1, gen2):
    index1 = random.randint(0, 7)
    index2 = random.randint(0, 7)
    gen1[index1] = index1
    gen2[index2] = index2
    return gen1, gen2


def breed(gen1, gen2):
    gen1_temp = []
    gen2_temp = []
    for i in range(3):
        gen1_temp.append(gen1.pop(0))
    for i in range(3):
        gen2_temp.append(gen2.pop(0))
    for i in range(5):
        gen1_temp.append(gen2.pop(0))
        gen2_temp.append(gen1.pop(0))
    return gen1_temp, gen2_temp


if __name__ == '__main__':
    main_board = generate_board()
    initialize_first_gen()
    # boards = []
    # for gen in env:
    #     boards.append(populate_board(main_board, gen))
    # main_board = generate_board()
    # for board in boards:
    #     print_board(board)
    # print()
    # print()
    for gen in env:
        if is_optimal_solution_option(gen):
            solution_board = populate_final_board(gen)
            print_board(solution_board)
    while True:
        cross_over_function()
        env = selection()
        counter += 1
        if goal_index >= 0:
            print(counter)
            temp_solution_board = populate_final_board(goal)
            print_board(temp_solution_board)
