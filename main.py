import random

"""
CSC 412
2/26/2021
@author: Tomas Perez
"""

counter = 0
white_chess_queen = '\u2655'
empty_square = '\u25A1'
white_square_obstacle = '\u25a0'
main_board = []
solutions = []
size = 9
env = []
goal = None
goal_index = -1
iteration_count = 0
perform_mutation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

"""
This helper method generates and returns 
a blank board with the obstacles present.
@:return - an empty chess board.
"""


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


"""
This helper method receives a board
and prints it to the console.
@user_board:param - the board to be printed.
"""


def print_board(user_board):
    for row in user_board:
        for c in row:
            print(c, end='')
        print('')


"""
This helper method checks to see if a 
given generation is an optimal solution.
@generation:param - the generation to be evaluated.
@:return - True is the generation is
            an optimal solution, False
            if not.
"""


def is_optimal_solution_option(generation):
    if fitness_function(generation) == 0:
        return True
    return False


"""
This method populates a chess board based off of a 
given generation.
@user_board:param - the board to be written onto.
@generation:param - the generation to be printed to the board.
"""


def populate_board(user_board, generation):
    temp_insert = generation[3]
    del generation[3]
    for i in range(size - 1):
        if i == 2:
            user_board[generation[i]][i] = white_chess_queen
            user_board[temp_insert][i] = white_chess_queen
        else:
            user_board[generation[i]][i] = white_chess_queen
    generation.insert(3, temp_insert)


"""
This method populates and returns a chess board with the 
solution generation.
@generation:param - the generation that is found to be the solution.
@:return - the solution board.
"""


def populate_final_board(generation):
    temp_insert = generation[3]
    del generation[3]
    temp_board = generate_board()
    for i in range(size - 1):
        if i == 2:
            temp_board[generation[i]][i] = white_chess_queen
            temp_board[temp_insert][i] = white_chess_queen
        else:
            temp_board[generation[i]][i] = white_chess_queen
    generation.insert(3, temp_insert)
    return temp_board


"""
This helper method generates random generations for
the initialization of the genetic algorithm.
@:return - a randomized generation.
"""


def generate_initial_population():
    # generate the random list of boards
    dna = list(range(size - 1))
    dna.append(random.randint(0, 7))
    while dna in env:
        random.shuffle(dna)
    while dna[2] == dna[3]:
        random.shuffle(dna)
    return dna


"""
This method initializes the first random
set of generations for the algorithm.
"""


def initialize_first_gen():
    for i in range(3000):
        env.append(generate_initial_population())


"""
This method is the fitness function that
calculates how optimal a given generation
is based off of the amount of collisions it 
find in the board.
@generation:param - the generation to be evaluated.
@:return - how optimal the generation is.
"""


def fitness_function(generation):
    correct_queens = 0
    hits = 0
    temp_board = generate_board()
    populate_board(temp_board, generation)
    temp_insert = generation[3]
    del generation[3]
    gen_size = len(generation)
    for dna in range(gen_size):
        if dna == 2:
            safe = is_safe(temp_board, generation[dna], dna)
            if safe is False:
                hits += 1
            else:
                correct_queens += 1
            safe_temp_insert = is_safe(temp_board, temp_insert, dna)
            if safe_temp_insert is False:
                hits += 1
            else:
                correct_queens += 1
            if temp_insert == generation[dna]:
                hits += 1
            else:
                correct_queens += 1
        else:
            safe = is_safe(temp_board, generation[dna], dna)
            if safe is False:
                hits += 1
            else:
                correct_queens += 1
    generation.insert(3, temp_insert)
    return hits


"""
This helper method checks the left, up, and 
both upper diagonal directions to see if 
there is an intersection with another queen,
and checks to see if a queen is being placed 
an obstacle.
@board:param - the board to be checked.
@row:param - the current row.
@column:param - the current column.
@:return - True if the queen placement is safe,
            False if not.
"""


def is_safe(board, row, column):
    if row == 3 and column == 2:
        return False
    if row == 4 and column == 2:
        return False
    if row == 0 and column == 0:
        return False
    left_side_row = check_left_side_row(board, row, column)
    if left_side_row is False:
        return False
    up_column = check_up_column(board, row, column)
    if up_column is False:
        return False
    left_diagonal = check_left_diagonal(board, row, column)
    if left_diagonal is False:
        return False
    right_diagonal = check_right_diagonal(board, row, column)
    if right_diagonal is False:
        return False
    return True


"""
This helper method checks the 
upper right diagonal direction.
@board:param - the board to be used.
@row:param - the current row.
@column:param - the current column.
@:return - True if the direction is
            clear of intersections,
            False if not.
"""


def check_right_diagonal(board, row, column):
    if row != 0 and column != size - 1:
        temp_row = row - 1
        temp_column = column + 1
        while temp_row >= 0 and temp_column < size - 1:
            if board[temp_row][temp_column] == white_square_obstacle:
                return True
            elif board[temp_row][temp_column] == white_chess_queen:
                return False
            temp_row -= 1
            temp_column += 1
    return True


"""
This helper method checks the 
upper left diagonal direction.
@board:param - the board to be used.
@row:param - the current row.
@column:param - the current column.
@:return - True if the direction is
            clear of intersections,
            False if not.
"""


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


"""
This helper method checks the 
up column direction.
@board:param - the board to be used.
@row:param - the current row.
@column:param - the current column.
@:return - True if the direction is
            clear of intersections,
            False if not.
"""


def check_up_column(board, row, column):
    if row != 0:
        for i in range(row - 1, -1, -1):
            if board[i][column] == white_square_obstacle:
                return True
            elif board[i][column] == white_chess_queen:
                return False
        return True
    return True


"""
This helper method checks the 
left row direction.
@board:param - the board to be used.
@row:param - the current row.
@column:param - the current column.
@:return - True if the direction is
            clear of intersections,
            False if not.
"""


def check_left_side_row(board, row, column):
    if column != 0:
        for i in range(column - 1, -1, -1):
            if board[row][i] == white_square_obstacle:
                return True
            elif board[row][i] == white_chess_queen:
                return False
        return True
    return True


"""
This method is the selection portion 
of the genetic algorithm and will calculate
all of the fitness functions for each
generation within the environment, from there
it checks to see if the solution has been found,
if not, then it searches for the closet matches
for the optimal solution and adds them to the
new environment iteration.
@:return - the new environment to be used for
            the genetic algorithm.
"""


def selection():
    global goal_index
    global goal
    all_fitness_results = []
    new_env = []
    for generation in env:
        all_fitness_results.append(fitness_function(generation))
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


"""
This method iterates through half of the environment
and performs breeding on two generations at a time
and inserts them back into the current environment.
"""


def cross_over_function():
    switch = False
    for i in range(1, len(env) // 2, 2):
        gen1 = env[i - 1][:]
        gen2 = env[i][:]
        if switch is False:
            gen1, gen2 = breed(gen1, gen2)
            switch = True
        else:
            gen1, gen2 = secondary_breed(gen1, gen2)
            switch = False
        gen1, gen2 = mutate(gen1, gen2)

        env.append(gen1)
        env.append(gen2)


"""
This method handles the mutation for 
two generations by randomizing two 
chromosomes within each generation.
@gen1:param - the first generation.
@gen2:param - the second generation.
@:return - the mutated generations.
"""


def mutate(gen1, gen2):
    for i in range(2):
        index1 = random.randint(0, 7)
        index2 = random.randint(0, 7)
        gen1[index1] = index1
        gen2[index2] = index2
    return gen1, gen2


"""
This first breed function will select
the last 6 chromosomes of both generations
and swaps them into the other.
@gen1:param - the first generation.
@gen2:param - the second generation.
@:return - both generations.
"""


def breed(gen1, gen2):
    gen1_temp = []
    gen2_temp = []
    for i in range(3):
        gen1_temp.append(gen1.pop(0))
    for i in range(3):
        gen2_temp.append(gen2.pop(0))
    for i in range(6):
        gen1_temp.append(gen2.pop(0))
        gen2_temp.append(gen1.pop(0))
    return gen1_temp, gen2_temp


"""
This second breed function will select
the last 3 chromosomes of both generations
and swaps them into the other.
@gen1:param - the first generation.
@gen2:param - the second generation.
@:return - both generations.
"""


def secondary_breed(gen1, gen2):
    gen1_temp = []
    gen2_temp = []
    for i in range(6):
        gen1_temp.append(gen1.pop(0))
    for i in range(6):
        gen2_temp.append(gen2.pop(0))
    for i in range(3):
        gen1_temp.append(gen2.pop(0))
        gen2_temp.append(gen1.pop(0))
    return gen1_temp, gen2_temp


if __name__ == '__main__':
    main_board = generate_board()
    initialize_first_gen()
    temp_counter = 0
    for gen in env:
        temp_counter += 1
        if is_optimal_solution_option(gen):
            print("Generation 1")
            print("Random board: {0}".format(temp_counter))
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
