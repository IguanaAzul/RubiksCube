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
            cubes.append((moves, openning_node_cube.compress_cube()))
    return cubes


def bfs(cube, check_function, allowed_moves):
    cube_node = Cube()
    cube_node.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))
    path = [([""], cube_node.compress_cube())]
    return search(path, check_function, allowed_moves, 1)


def search(layer, check_function, allowed_moves, lvl):
    new_layer = list()
    print(lvl)
    for node in layer:
        cube = Cube()
        cube.decompress_cube(node[1])
        if check_function(cube):
            return node[0], cube
        for suc in successors(node[0], cube, allowed_moves, node[0][-1]):
            new_layer.append(suc)
    del layer
    return search(new_layer, check_function, allowed_moves, lvl+1)
