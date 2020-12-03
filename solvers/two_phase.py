import numpy as np
from solvers import ida_star
from rubiks_cube import Cube
from utils import fix_scramble, colors
max_oriented = 18


def count_oriented(cube):
    matrix = cube.get_color_matrix()
    return np.array([i in ["w", "y"] for i in matrix[0]]).sum() + \
        np.array([i in ["w", "y"] for i in matrix[3]]).sum()


def calc_cost_1(cost, cube):
    return cost + (max_oriented - count_oriented(cube))


def is_g1(cube):
    matrix = cube.get_color_matrix()
    return np.array([i in [colors[0], colors[3]] for i in matrix[0]]).all() and \
        np.array([i in [colors[0], colors[3]] for i in matrix[3]]).all()


def is_g2(cube):
    return cube.is_solved()


def two_phase(cube):
    new_cube = Cube()
    new_cube.set_cube((cube.get_color_matrix(), cube.get_pieces()))
    allowed_moves = ["U", "R", "F", "L", "B", "D",
                     "U'", "R'", "F'", "L'", "B'", "D'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    phase1 = ida_star(new_cube, is_g1, calc_cost_1, allowed_moves)

    new_cube.scramble(phase1)
    return fix_scramble(phase1), new_cube
    allowed_moves = ["U", "D", "U'", "D'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    phase2 = ida_star(new_cube, is_g2, calc_cost_2, allowed_moves)
    new_cube.scramble(phase2)
    return fix_scramble(" ".join((phase1, phase2))), new_cube
