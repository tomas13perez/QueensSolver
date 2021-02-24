
"""
CSC 412
2/18/2021
@author: Tomas Perez
"""

counter = 0
white_chess_queen = '\u2655'
empty_square = '\u25A1'
white_square_obstacle = '\u25a0'
env = []


class SolveQueensGenetic:
    def __int__(self):
        self.board = self.generate_board()
        self.solutions = []
        self.size = 8
        self.goal = None
        self.goalIndex = -1

    @staticmethod
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

    @staticmethod
    def print_board(user_board):
        for row in user_board:
            for c in row:
                print(c, end='')
            print('')

    def populate_board(self, user_board, generation):
        for i in range(self.size):
            user_board[generation[i][i]] = white_chess_queen
        return user_board

    def generate_initial_population(self):
        # generate the random list of boards
        import random
        dna = list(range(self.size))
        # FIXME: might not need this line...already calling in while dna loop below.
        random.shuffle(dna)
        while dna in env:
            random.shuffle(dna)
        return dna

    # initialize with 100 for population size
    def initialize_first_gen(self):
        for i in range(100):
            env.append(self.generate_initial_population())

    # def fitness_function(self, generation):
    #     hits = 0

    def solve_chess_board(self):
        self.initialize_first_gen()
        boards = []
        for gen in env:
            boards.append(self.populate_board(self.board, gen))
        for board in boards:
            self.print_board(board)
            print()
            print()
