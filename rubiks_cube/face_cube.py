import numpy as np
from utils import matrix_ref, int_face, notation, swap4, colors


class FaceCube:
    def __init__(self):
        self.matrix_colors = matrix_ref.copy()

    def turn_face(self, face, way=0):
        turn = int_face[face]
        self.matrix_colors[turn, 1], self.matrix_colors[turn, 2], \
            self.matrix_colors[turn, 3], self.matrix_colors[turn, 4] = swap4(self.matrix_colors[turn, 1],
                                                                             self.matrix_colors[turn, 2],
                                                                             self.matrix_colors[turn, 3],
                                                                             self.matrix_colors[turn, 4],
                                                                             way)

        self.matrix_colors[turn, 5], self.matrix_colors[turn, 6], \
            self.matrix_colors[turn, 7], self.matrix_colors[turn, 8] = swap4(self.matrix_colors[turn, 5],
                                                                             self.matrix_colors[turn, 6],
                                                                             self.matrix_colors[turn, 7],
                                                                             self.matrix_colors[turn, 8],
                                                                             way)
        # UP
        if turn == 0:
            self.matrix_colors[1, 3], self.matrix_colors[2, 4], \
                self.matrix_colors[4, 1], self.matrix_colors[5, 2] = swap4(self.matrix_colors[1, 3],
                                                                           self.matrix_colors[2, 4],
                                                                           self.matrix_colors[4, 1],
                                                                           self.matrix_colors[5, 2],
                                                                           way)

            self.matrix_colors[1, 7], self.matrix_colors[2, 8], \
                self.matrix_colors[4, 5], self.matrix_colors[5, 6] = swap4(self.matrix_colors[1, 7],
                                                                           self.matrix_colors[2, 8],
                                                                           self.matrix_colors[4, 5],
                                                                           self.matrix_colors[5, 6],
                                                                           way)

            self.matrix_colors[1, 8], self.matrix_colors[2, 5], \
                self.matrix_colors[4, 6], self.matrix_colors[5, 7] = swap4(self.matrix_colors[1, 8],
                                                                           self.matrix_colors[2, 5],
                                                                           self.matrix_colors[4, 6],
                                                                           self.matrix_colors[5, 7],
                                                                           way)
        # FRONT
        elif turn == 1:
            self.matrix_colors[3, 1], self.matrix_colors[2, 1], \
                self.matrix_colors[0, 1], self.matrix_colors[5, 1] = swap4(self.matrix_colors[3, 1],
                                                                           self.matrix_colors[2, 1],
                                                                           self.matrix_colors[0, 1],
                                                                           self.matrix_colors[5, 1],
                                                                           way)

            self.matrix_colors[3, 5], self.matrix_colors[2, 5], \
                self.matrix_colors[0, 5], self.matrix_colors[5, 5] = swap4(self.matrix_colors[3, 5],
                                                                           self.matrix_colors[2, 5],
                                                                           self.matrix_colors[0, 5],
                                                                           self.matrix_colors[5, 5],
                                                                           way)

            self.matrix_colors[3, 6], self.matrix_colors[2, 6], \
                self.matrix_colors[0, 6], self.matrix_colors[5, 6] = swap4(self.matrix_colors[3, 6],
                                                                           self.matrix_colors[2, 6],
                                                                           self.matrix_colors[0, 6],
                                                                           self.matrix_colors[5, 6],
                                                                           way)
        # RIGHT
        elif turn == 2:
            self.matrix_colors[0, 2], self.matrix_colors[1, 2], \
                self.matrix_colors[3, 4], self.matrix_colors[4, 2] = swap4(self.matrix_colors[0, 2],
                                                                           self.matrix_colors[1, 2],
                                                                           self.matrix_colors[3, 4],
                                                                           self.matrix_colors[4, 2],
                                                                           way)

            self.matrix_colors[0, 6], self.matrix_colors[1, 6], \
                self.matrix_colors[3, 8], self.matrix_colors[4, 6] = swap4(self.matrix_colors[0, 6],
                                                                           self.matrix_colors[1, 6],
                                                                           self.matrix_colors[3, 8],
                                                                           self.matrix_colors[4, 6],
                                                                           way)

            self.matrix_colors[0, 7], self.matrix_colors[1, 7], \
                self.matrix_colors[3, 5], self.matrix_colors[4, 7] = swap4(self.matrix_colors[0, 7],
                                                                           self.matrix_colors[1, 7],
                                                                           self.matrix_colors[3, 5],
                                                                           self.matrix_colors[4, 7],
                                                                           way)
        # DOWN
        elif turn == 3:
            self.matrix_colors[1, 1], self.matrix_colors[5, 4], \
                self.matrix_colors[4, 3], self.matrix_colors[2, 2] = swap4(self.matrix_colors[1, 1],
                                                                           self.matrix_colors[5, 4],
                                                                           self.matrix_colors[4, 3],
                                                                           self.matrix_colors[2, 2],
                                                                           way)

            self.matrix_colors[5, 8], self.matrix_colors[4, 7], \
                self.matrix_colors[2, 6], self.matrix_colors[1, 5] = swap4(self.matrix_colors[5, 8],
                                                                           self.matrix_colors[4, 7],
                                                                           self.matrix_colors[2, 6],
                                                                           self.matrix_colors[1, 5],
                                                                           way)

            self.matrix_colors[5, 5], self.matrix_colors[4, 8], \
                self.matrix_colors[2, 7], self.matrix_colors[1, 6] = swap4(self.matrix_colors[5, 5],
                                                                           self.matrix_colors[4, 8],
                                                                           self.matrix_colors[2, 7],
                                                                           self.matrix_colors[1, 6],
                                                                           way)
        # BACK
        elif turn == 4:
            self.matrix_colors[0, 3], self.matrix_colors[2, 3], \
                self.matrix_colors[3, 3], self.matrix_colors[5, 3] = swap4(self.matrix_colors[0, 3],
                                                                           self.matrix_colors[2, 3],
                                                                           self.matrix_colors[3, 3],
                                                                           self.matrix_colors[5, 3],
                                                                           way)

            self.matrix_colors[0, 8], self.matrix_colors[2, 8], \
                self.matrix_colors[3, 8], self.matrix_colors[5, 8] = swap4(self.matrix_colors[0, 8],
                                                                           self.matrix_colors[2, 8],
                                                                           self.matrix_colors[3, 8],
                                                                           self.matrix_colors[5, 8],
                                                                           way)

            self.matrix_colors[0, 7], self.matrix_colors[2, 7], \
                self.matrix_colors[3, 7], self.matrix_colors[5, 7] = swap4(self.matrix_colors[0, 7],
                                                                           self.matrix_colors[2, 7],
                                                                           self.matrix_colors[3, 7],
                                                                           self.matrix_colors[5, 7],
                                                                           way)
        # LEFT
        elif turn == 5:
            self.matrix_colors[0, 4], self.matrix_colors[4, 4], \
                self.matrix_colors[3, 2], self.matrix_colors[1, 4] = swap4(self.matrix_colors[0, 4],
                                                                           self.matrix_colors[4, 4],
                                                                           self.matrix_colors[3, 2],
                                                                           self.matrix_colors[1, 4],
                                                                           way)

            self.matrix_colors[1, 8], self.matrix_colors[0, 8], \
                self.matrix_colors[4, 8], self.matrix_colors[3, 6] = swap4(self.matrix_colors[1, 8],
                                                                           self.matrix_colors[0, 8],
                                                                           self.matrix_colors[4, 8],
                                                                           self.matrix_colors[3, 6],
                                                                           way)

            self.matrix_colors[1, 5], self.matrix_colors[0, 5], \
                self.matrix_colors[4, 5], self.matrix_colors[3, 7] = swap4(self.matrix_colors[1, 5],
                                                                           self.matrix_colors[0, 5],
                                                                           self.matrix_colors[4, 5],
                                                                           self.matrix_colors[3, 7],
                                                                           way)

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
