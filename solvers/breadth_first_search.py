import numpy as np
from rubiks_cube import Cube


def is_equiv(move1, move2):
    move1 = move1.strip()
    move2 = move2.strip()
    if move1 == "":
        return False
    elif move1[0] == move2[0]:
        return True
    else:
        return False


def successors(old_moves, cube, allowed_moves, last_move):
    cubes = list()
    for move in allowed_moves:
        if not is_equiv(last_move, move):
            openning_node_cube = Cube()
            openning_node_cube.set_cube(cube.get_color_matrix())
            openning_node_cube.scramble(move)
            moves = list(old_moves)
            moves.append(move)
            cubes.append((moves, openning_node_cube))
    return cubes


def bfs(cube, check_function, allowed_moves):
    cube_node = Cube()
    cube_node.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))
    path = [([""], cube_node)]
    return search(path, check_function, allowed_moves)


def search(path, check_function, allowed_moves):
    done = check_function(path[-1][1])
    layer = [path[-1]]
    lvl = 1
    while not done:
        # print(lvl)
        new_layer = list()
        for node in layer:
            for suc in successors(node[0], node[1], allowed_moves, node[0][-1]):
                done = check_function(suc[1])
                if done:
                    return suc[0], suc[1]
                new_layer.append(suc)
        layer = new_layer.copy()
        del new_layer
        lvl += 1
    return path
