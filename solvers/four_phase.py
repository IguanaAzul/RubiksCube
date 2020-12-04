import numpy as np
from rubiks_cube import Cube
from utils import colors, fix_scramble
from solvers.breadth_first_search import bfs
from time import time


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


def is_g4(cube):
    return cube.is_solved()


def four_phase(cube):
    new_cube = Cube()
    new_cube.set_cube((cube.get_color_matrix(), cube.get_pieces()))
    allowed_moves = ["U", "R", "F", "L", "B", "D",
                     "U'", "R'", "F'", "L'", "B'", "D'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    t0 = time()
    phase1, new_cube = bfs(new_cube, is_g1, allowed_moves)
    t = time()
    print("phase1:")
    print(t-t0)
    print(phase1)
    phase1 = " ".join(phase1)
    allowed_moves = ["U", "D", "U'", "D'", "R", "R'", "L", "L'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    t0 = time()
    phase2, new_cube = bfs(new_cube, is_g2, allowed_moves)
    t = time()
    print("phase2:")
    print(t-t0)
    print(phase2)
    phase2 = " ".join(phase2)
    allowed_moves = ["U", "D", "U'", "D'",
                     "U2", "R2", "F2", "L2", "B2", "D2"]
    t0 = time()
    phase3, new_cube = bfs(new_cube, is_g3, allowed_moves)
    t = time()
    print("phase3:")
    print(t-t0)
    print(phase3)
    phase3 = " ".join(phase3)
    allowed_moves = ["U2", "R2", "F2", "L2", "B2", "D2"]
    t0 = time()
    phase4, new_cube = bfs(new_cube, is_g4, allowed_moves)
    t = time()
    print("phase4:")
    print(t-t0)
    print(phase4)
    phase4 = " ".join(phase4)
    return fix_scramble(" ".join((phase1, phase2, phase3, phase4)))
