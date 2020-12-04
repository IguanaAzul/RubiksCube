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


def successors(node, allowed_moves, last_move):
    cubes = list()
    for move in allowed_moves:
        if not is_equiv(last_move, move):
            openning_node_cube = Cube()
            openning_node_cube.set_cube((node[1].get_color_matrix().copy(), node[1].get_pieces().copy()))
            openning_node_cube.scramble(move)
            moves = list(node[0])
            moves.append(move)
            cubes.append((moves, openning_node_cube))
    return cubes


def bfs(cube, check_function, allowed_moves):
    cube_node = Cube()
    cube_node.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))
    path = [([""], cube_node)]
    return search(path, check_function, allowed_moves)


def search(layer, check_function, allowed_moves):
    new_layer = list()
    for node in layer:
        if check_function(node[1]):
            return node
        for suc in successors(node, allowed_moves, node[0][-1]):
            new_layer.append(suc)
    del layer
    return search(new_layer, check_function, allowed_moves)


















# class Graph:
#     def __init__(self, cube, allowed_moves) -> None:
#         self.graph = {(cube, ""): cube}
#         self.parent = {}
#         self.source_vertex = cube
#         self.allowed_moves = allowed_moves
#
#     def breath_first_search(self) -> None:
#         visited = {self.source_vertex}
#         self.parent[self.source_vertex] = None
#         queue = [self.source_vertex]  # first in first out queue
#
#         while queue:
#             vertex = queue.pop(0)
#             for move in self.allowed_moves:
#                 new_cube = Cube()
#                 new_cube.set_cube(vertex[0])
#                 new_cube.scramble(move)
#                 self.graph[(vertex[0], move)] = new_cube
#             for adjacent_vertex in self.graph[vertex[0]]:
#                 if adjacent_vertex not in visited:
#                     visited.add(adjacent_vertex)
#                     self.parent[adjacent_vertex] = vertex[0]
#                     queue.append(adjacent_vertex)
#
#     def shortest_path(self, target_vertex):
#         if target_vertex.is_equal(self.source_vertex):
#             return f"{self.source_vertex}"
#         elif not self.parent.get(target_vertex):
#             return f"No path from vertex:{self.source_vertex} to vertex:{target_vertex}"
#         else:
#             return self.shortest_path(self.parent[target_vertex]) + f"->{target_vertex}"
