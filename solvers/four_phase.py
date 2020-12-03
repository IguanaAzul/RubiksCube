import numpy as np
from rubiks_cube import Cube
from utils import colors, fix_scramble
from solvers import ida_star
from time import time
max_oriented = 18


def is_g1(cube):
    return not (cube.get_pieces()[:12, 1]).any()


def is_g2(cube):
    matrix = cube.get_color_matrix()
    return np.array([i in [colors[0], colors[3]] for i in matrix[0]]).all() and \
        np.array([i in [colors[0], colors[3]] for i in matrix[3]]).all()


def is_g3(cube):
    matrix = cube.get_color_matrix()
    return is_g2(cube) and np.array([i in [colors[2], colors[5]] for i in matrix[2]]).all() and \
        np.array([i in [colors[2], colors[5]] for i in matrix[5]]).all() and \
        np.array([i in [colors[1], colors[4]] for i in matrix[1]]).all() and \
        np.array([i in [colors[1], colors[4]] for i in matrix[4]]).all()


def calc_cost_1(cost, cube):
    return cost + (cube.get_pieces()[:12, 1]).sum()


def calc_cost_2(cost, cube):
    return cost + 12 - (cube.get_pieces()[12:, 1]).sum()


def four_phase(cube):
    new_cube = Cube()
    new_cube.set_cube((cube.get_color_matrix(), cube.get_pieces()))
    allowed_moves = ["U", "R", "F", "L", "B", "D",
                     "U'", "R'", "F'", "L'", "B'", "D'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    t0 = time()
    phase1 = ida_star(new_cube, is_g1, calc_cost_1, allowed_moves)
    new_cube.scramble(phase1)
    # return fix_scramble(phase1), time() - t0
    allowed_moves = ["U", "D", "U'", "D'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    phase2 = ida_star(new_cube, is_g2, calc_cost_2, allowed_moves)
    new_cube.scramble(phase2)
    return fix_scramble(" ".join((phase1, phase2))), time() - t0


    phase3 = ida_star(new_cube, is_g2, calc_cost, allowed_moves)
    new_cube.scramble(phase3)
    phase4 = ida_star(new_cube, is_g2, calc_cost, allowed_moves)
    new_cube.scramble(phase4)
    return fix_scramble(" ".join((phase1, phase2, phase3, phase4))), new_cube