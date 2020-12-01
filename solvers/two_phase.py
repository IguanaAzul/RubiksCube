import numpy as np
from rubiks_cube import rubiks_cube
from utils import scramble_generator

max_oriented = 18
max_depth = 10


def is_g1(cube):
    matrix = cube.get_color_matrix()
    if matrix[0, 0] != "w":
        print("Error: This method only supports cubes with white in position 0")
        return None

    return np.array([i in ["w", "y"] for i in matrix[0]]).all() and \
        np.array([i in ["w", "y"] for i in matrix[3]]).all()


def count_oriented(cube):
    matrix = cube.get_color_matrix()
    if matrix[0, 0] != "w":
        print("Error: This method only supports cubes with white in position 0")
        return None

    return np.array([i in ["w", "y"] for i in matrix[0]]).sum() + \
        np.array([i in ["w", "y"] for i in matrix[3]]).sum()


allowed_moves = ["U", "R", "F", "L", "B", "D",
                 "U'", "R'", "F'", "L'", "B'", "D'",
                 "U2", "R2", "F2", "L2", "B2", "D2"]


def is_equiv(move1, move2):
    if move1 == "":
        return False
    elif move1[0] == move2[0]:
        return True
    else:
        return False


def calc_cost(cost, cube):
    return cost + (max_oriented - count_oriented(cube))


def successors(node, cost):
    cubes = list()
    for move in allowed_moves:
        openning_node_cube = rubiks_cube.Cube()
        openning_node_cube.set_matrix(node[1].get_color_matrix().copy())
        openning_node_cube.set_pieces(node[1].get_pieces().copy())
        openning_node_cube.scramble(move)
        f_openning_node = calc_cost(cost, openning_node_cube)
        cubes.append((move, openning_node_cube, f_openning_node))
    return sorted(cubes, key=lambda tup: tup[2])


def ida_star(cube):
    cube_node = rubiks_cube.Cube()
    cube_node.set_matrix(cube.get_color_matrix().copy())
    cube_node.set_pieces(cube.get_pieces().copy())
    path = [("", cube_node)]
    bound = calc_cost(0, path[-1][1])
    while True:
        t = search(path, 0, bound)
        if t == "Found":
            break
        bound = t
    return " ".join([i[0] for i in path[1:]])


def search(path, g, bound):
    node = path[-1]
    least = max_oriented
    f = g + calc_cost(g, node[1])
    if f > bound:
        return f
    if is_g1(node[1]):
        return "Found"
    for suc in successors(node, f):
        if not is_equiv(node[0], suc[0]):
            path.append(suc)
            t = search(path, g + 1, bound)
            if t == "Found":
                return t
            least = t if t < least else least
            path.pop()
            # print(" ".join([i[0] for i in path[1:]]))
    return least
