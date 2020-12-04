import numpy as np
from rubiks_cube import rubiks_cube
max_depth = 10
max_oriented = 18


def is_equiv(move1, move2):
    if move1 == "":
        return False
    elif move1[0] == move2[0]:
        return True
    else:
        return False


def successors(node, cost, cost_function, allowed_moves):
    cubes = list()
    for move in allowed_moves:
        openning_node_cube = rubiks_cube.Cube()
        openning_node_cube.set_cube((node[1].get_color_matrix().copy(), node[1].get_pieces().copy()))
        openning_node_cube.scramble(move)
        f_openning_node = cost_function(cost, openning_node_cube)
        cubes.append((move, openning_node_cube, f_openning_node))
    return sorted(cubes, key=lambda tup: tup[2])


def ida_star(cube, check_function, cost_function, allowed_moves):
    cube_node = rubiks_cube.Cube()
    cube_node.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))
    path = [("", cube_node)]
    bound = cost_function(0, path[-1][1])
    while True:
        t = search(path, 0, bound, check_function, cost_function, allowed_moves)
        if t == "Found":
            break
        bound = t
    return " ".join([i[0] for i in path[1:]])


def search(path, g, bound, check_function, cost_function, allowed_moves):
    node = path[-1]
    least = max_oriented
    f = g + cost_function(g, node[1])
    if f > bound:
        return f
    if check_function(node[1]):
        return "Found"
    for suc in successors(node, f, cost_function, allowed_moves):
        if not is_equiv(node[0], suc[0]):
            path.append(suc)
            t = search(path, g + 1, bound, check_function, cost_function, allowed_moves)
            if t == "Found":
                return t
            least = t if t < least else least
            path.pop()
            print([i[0] for i in path], t)
    return least
