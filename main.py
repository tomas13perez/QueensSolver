"""
CSC 412
2/18/2021
@author: Tomas Perez
"""


white_chess_queen = '\u2655'
empty_square = '\u25A1'
white_square_obstacle = '\u25a0'
chess_board = [
    [white_square_obstacle, empty_square, white_chess_queen, empty_square, empty_square, empty_square, empty_square,
     empty_square],
    [white_chess_queen, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
     empty_square],
    [empty_square, empty_square, empty_square, white_chess_queen, empty_square, empty_square, empty_square,
     empty_square],
    [empty_square, white_chess_queen, white_square_obstacle, empty_square, empty_square, empty_square,
     white_chess_queen,
     empty_square],
    [empty_square, empty_square, white_square_obstacle, empty_square, white_chess_queen, empty_square, empty_square,
     empty_square],
    [empty_square, empty_square, white_chess_queen, empty_square, empty_square, empty_square, empty_square,
     empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, white_chess_queen, empty_square,
     empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
     white_chess_queen]]
for row in chess_board:
    for c in row:
        print(c, end='')
    print('')
