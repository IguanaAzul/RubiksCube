import numpy as np
from rubiks_cube import scramble_generator, rubiks_cube
from copy import deepcopy
import itertools


def is_g1(cube):
    matrix = cube.get_matrix()
    if matrix[0, 0] != "w":
        print("Error: This method only supports cubes with white in position 0")
        return None

    return np.array([i in ["w", "y"] for i in matrix[0]]).all() and \
        np.array([i in ["w", "y"] for i in matrix[3]]).all()


def count_oriented(cube):
    matrix = cube.get_matrix()
    if matrix[0, 0] != "w":
        print("Error: This method only supports cubes with white in position 0")
        return None

    return np.array([i in ["w", "y"] for i in matrix[0]]).sum() + \
        np.array([i in ["w", "y"] for i in matrix[3]]).sum()


def phase1(cube):
    allowed_moves = ["U", "R", "F", "L", "B", "D",
                      "U'", "R'", "F'", "L'", "B'", "D'",
                      "U2", "R2", "F2", "L2", "B2", "D2"]
    color_matrix = cube.get_matrix().copy()
    best = cube
    best_value = count_oriented(cube)
    solution = ""
    best_move = ""
    best_changed = False
    depth = 1
    possible_moves = allowed_moves.copy()
    while not is_g1(cube):
        for move in possible_moves:
            evaluated = rubiks_cube.Cube()
            evaluated.set_matrix(color_matrix.copy())
            move = " ".join([move for move in move]) if type(move) is tuple else move
            evaluated.scramble(move)
            evaluation = count_oriented(evaluated)
            if evaluation > best_value:
                best_value = evaluation
                best = evaluated
                best_move = move
                best_changed = True
        if not best_changed:
            depth += 1
            possible_moves = itertools.combinations(allowed_moves, depth)
        else:
            depth = 1
            possible_moves = allowed_moves.copy()
        best_changed = False
        color_matrix = best.get_matrix()
        cube = rubiks_cube.Cube()
        cube.set_matrix(color_matrix)
        solution += best_move + " "
    return solution


def phase2():
    phase2 = ""

    return phase2
