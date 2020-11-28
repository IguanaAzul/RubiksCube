import numpy as np
from utils import matrix_ref, int_face, notation, swap4, colors


class FaceCube:
    def __init__(self):
        self.matrix_colors = matrix_ref.copy()

    def swap(self, to_swap, way):
        (self.matrix_colors[to_swap[0]], self.matrix_colors[to_swap[1]],
         self.matrix_colors[to_swap[2]], self.matrix_colors[to_swap[3]]) = \
            swap4(self.matrix_colors[to_swap[0]].copy(), self.matrix_colors[to_swap[1]].copy(),
                  self.matrix_colors[to_swap[2]].copy(), self.matrix_colors[to_swap[3]].copy(),
                  way)

    def turn_face(self, face, way=0):
        turn = int_face[face]

        # Turn edge facelets in the turning face
        self.swap([(turn, 1), (turn, 2), (turn, 3), (turn, 4)], way)
        self.swap([(turn, 5), (turn, 6), (turn, 7), (turn, 8)], way)

        # UP
        if turn == 0:
            lateral_edges_to_swap = [(1, 3), (2, 4), (4, 1), (5, 2)]
            lateral_corners_to_swap_1 = [(1, 7), (2, 8), (4, 5), (5, 6)]
            lateral_corners_to_swap_2 = [(1, 8), (2, 5), (4, 6), (5, 7)]

        # FRONT
        elif turn == 1:
            lateral_edges_to_swap = [(3, 1), (2, 1), (0, 1), (5, 1)]
            lateral_corners_to_swap_1 = [(3, 5), (2, 5), (0, 5), (5, 5)]
            lateral_corners_to_swap_2 = [(3, 6), (2, 6), (0, 6), (5, 6)]

        # RIGHT
        elif turn == 2:
            lateral_edges_to_swap = [(0, 2), (1, 2), (3, 4), (4, 2)]
            lateral_corners_to_swap_1 = [(0, 6), (1, 6), (3, 8), (4, 6)]
            lateral_corners_to_swap_2 = [(0, 7), (1, 7), (3, 5), (4, 7)]

        # DOWN
        elif turn == 3:
            lateral_edges_to_swap = [(1, 1), (5, 4), (4, 3), (2, 2)]
            lateral_corners_to_swap_1 = [(5, 8), (4, 7), (2, 6), (1, 5)]
            lateral_corners_to_swap_2 = [(5, 5), (4, 8), (2, 7), (1, 6)]

        # BACK
        elif turn == 4:
            lateral_edges_to_swap = [(0, 3), (2, 3), (3, 3), (5, 3)]
            lateral_corners_to_swap_1 = [(0, 8), (2, 8), (3, 8), (5, 8)]
            lateral_corners_to_swap_2 = [(0, 7), (2, 7), (3, 7), (5, 7)]

        # LEFT
        elif turn == 5:
            lateral_edges_to_swap = [(0, 4), (4, 4), (3, 2), (1, 4)]
            lateral_corners_to_swap_1 = [(1, 8), (0, 8), (4, 8), (3, 6)]
            lateral_corners_to_swap_2 = [(1, 5), (0, 5), (4, 5), (3, 7)]

        else:
            print("Error: Invalid face to turn")
            return

        # Turn edge facelets in the lateral faces
        self.swap(lateral_edges_to_swap, way)
        # Turn corner facelets in the lateral faces part 1
        self.swap(lateral_corners_to_swap_1, way)
        # Turn corner facelets in the lateral faces part 2
        self.swap(lateral_corners_to_swap_2, way)

    def is_solved(self):
        return np.array_equal(self.matrix_colors, matrix_ref)

    def n_colors_in_place(self):
        return np.sum(self.matrix_colors == matrix_ref)

    def print(self):
        print("rubiks_cube: \n")
        print("      {0} {1} {2}".format(self.matrix_colors[4, 8], self.matrix_colors[4, 3], self.matrix_colors[4, 7]))
        print("      {0} {1} {2}".format(self.matrix_colors[4, 4], self.matrix_colors[4, 0], self.matrix_colors[4, 2]))
        print("      {0} {1} {2}".format(self.matrix_colors[4, 5], self.matrix_colors[4, 1], self.matrix_colors[4, 6]))
        print("      -----")
        print("{0} {1} {2}|{3} {4} {5}|{6} {7} {8}|{9} {10} {11}"
              .format(self.matrix_colors[5, 8], self.matrix_colors[5, 3], self.matrix_colors[5, 7],
                      self.matrix_colors[0, 8], self.matrix_colors[0, 3], self.matrix_colors[0, 7],
                      self.matrix_colors[2, 8], self.matrix_colors[2, 3], self.matrix_colors[2, 7],
                      self.matrix_colors[3, 8], self.matrix_colors[3, 3], self.matrix_colors[3, 7]))
        print("{0} {1} {2}|{3} {4} {5}|{6} {7} {8}|{9} {10} {11}"
              .format(self.matrix_colors[5, 4], self.matrix_colors[5, 0], self.matrix_colors[5, 2],
                      self.matrix_colors[0, 4], self.matrix_colors[0, 0], self.matrix_colors[0, 2],
                      self.matrix_colors[2, 4], self.matrix_colors[2, 0], self.matrix_colors[2, 2],
                      self.matrix_colors[3, 4], self.matrix_colors[3, 0], self.matrix_colors[3, 2]))
        print("{0} {1} {2}|{3} {4} {5}|{6} {7} {8}|{9} {10} {11}"
              .format(self.matrix_colors[5, 5], self.matrix_colors[5, 1], self.matrix_colors[5, 6],
                      self.matrix_colors[0, 5], self.matrix_colors[0, 1], self.matrix_colors[0, 6],
                      self.matrix_colors[2, 5], self.matrix_colors[2, 1], self.matrix_colors[2, 6],
                      self.matrix_colors[3, 5], self.matrix_colors[3, 1], self.matrix_colors[3, 6]))
        print("      -----")
        print("      {0} {1} {2}".format(self.matrix_colors[1, 8], self.matrix_colors[1, 3], self.matrix_colors[1, 7]))
        print("      {0} {1} {2}".format(self.matrix_colors[1, 4], self.matrix_colors[1, 0], self.matrix_colors[1, 2]))
        print("      {0} {1} {2}".format(self.matrix_colors[1, 5], self.matrix_colors[1, 1], self.matrix_colors[1, 6]))
        print()

    def scramble(self, scramble):
        turns = [notation[turn] for turn in scramble.split()]
        for turn in turns:
            self.turn_face(turn[0], turn[1])

    def get_matrix(self):
        return self.matrix_colors

    def set_matrix(self, matrix):
        self.matrix_colors = matrix

    def get_binary_array(self, one_hot=False):
        if one_hot:
            binary_array = np.zeros(288).astype(int)
            for i in range(6):
                for j in range(1, 9):
                    if self.matrix_colors[i][j] == colors[0]:
                        binary_array[(j - 1) * 6 + i * 48] = 1
                    elif self.matrix_colors[i][j] == colors[1]:
                        binary_array[(j - 1) * 6 + 1 + i * 48] = 1
                    elif self.matrix_colors[i][j] == colors[2]:
                        binary_array[(j - 1) * 6 + 2 + i * 48] = 1
                    elif self.matrix_colors[i][j] == colors[3]:
                        binary_array[(j - 1) * 6 + 3 + i * 48] = 1
                    elif self.matrix_colors[i][j] == colors[4]:
                        binary_array[(j - 1) * 6 + 4 + i * 48] = 1
                    elif self.matrix_colors[i][j] == colors[5]:
                        binary_array[(j - 1) * 6 + 5 + i * 48] = 1
        else:
            binary_array = np.zeros(144).astype(int)
            for i in range(6):
                for j in range(1, 9):
                    if self.matrix_colors[i][j] == colors[1]:
                        binary_array[(j - 1) * 3 + 1 + i * 24] = 1
                    elif self.matrix_colors[i][j] == colors[2]:
                        binary_array[(j - 1) * 3 + 1 + i * 24] = 1
                        binary_array[(j - 1) * 3 + 2 + i * 24] = 1
                    elif self.matrix_colors[i][j] == colors[3]:
                        binary_array[(j - 1) * 3 + i * 24] = 1
                    elif self.matrix_colors[i][j] == colors[4]:
                        binary_array[(j - 1) * 3 + i * 24] = 1
                        binary_array[(j - 1) * 3 + 2 + i * 24] = 1
                    elif self.matrix_colors[i][j] == colors[5]:
                        binary_array[(j - 1) * 3 + i * 24] = 1
                        binary_array[(j - 1) * 3 + 1 + i * 24] = 1

        return binary_array

    def set_matrix_from_pieces(self, pieces):
        # TODO
        return
