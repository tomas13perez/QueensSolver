white_chess_queen = '\u2655'
empty_square = '\u25A1'
white_square_obstacle = '\u25a0'
chess_board = [
    [white_square_obstacle, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square,
     empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
    [empty_square, empty_square, white_square_obstacle, empty_square, empty_square, empty_square, empty_square,
     empty_square],
    [empty_square, empty_square, white_square_obstacle, empty_square, empty_square, empty_square, empty_square,
     empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
    [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]]
for row in chess_board:
    for c in row:
        print(c, end='')
    print('')
