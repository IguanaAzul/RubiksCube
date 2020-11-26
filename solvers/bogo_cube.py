from rubiks_cube import scramble_generator


def bogo_cube(cube, how_long=10000):
    solution = ""
    i = 0
    while not cube.is_solved() and i < how_long:
        move = scramble_generator(1)
        solution += move + " "
        cube.scramble(move)
        i += 1
    return solution, cube
