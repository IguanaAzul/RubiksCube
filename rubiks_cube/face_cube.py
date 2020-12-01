import numpy as np
from utils import matrix_ref, int_face, notation, swap4, colors, corners


class FaceCube:
    def __init__(self):
        self.color_matrix = matrix_ref.copy()

    def swap(self, to_swap, way):
        (self.color_matrix[to_swap[0]], self.color_matrix[to_swap[1]],
         self.color_matrix[to_swap[2]], self.color_matrix[to_swap[3]]) = \
            swap4(self.color_matrix[to_swap[0]].copy(), self.color_matrix[to_swap[1]].copy(),
                  self.color_matrix[to_swap[2]].copy(), self.color_matrix[to_swap[3]].copy(),
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
        return np.array_equal(self.color_matrix, matrix_ref)

    def n_colors_in_place(self):
        return np.sum(self.color_matrix == matrix_ref)

    def print(self):
        print("rubiks_cube: \n")
        print("      {0} {1} {2}".format(self.color_matrix[4, 8], self.color_matrix[4, 3], self.color_matrix[4, 7]))
        print("      {0} {1} {2}".format(self.color_matrix[4, 4], self.color_matrix[4, 0], self.color_matrix[4, 2]))
        print("      {0} {1} {2}".format(self.color_matrix[4, 5], self.color_matrix[4, 1], self.color_matrix[4, 6]))
        print("      -----")
        print("{0} {1} {2}|{3} {4} {5}|{6} {7} {8}|{9} {10} {11}"
              .format(self.color_matrix[5, 8], self.color_matrix[5, 3], self.color_matrix[5, 7],
                      self.color_matrix[0, 8], self.color_matrix[0, 3], self.color_matrix[0, 7],
                      self.color_matrix[2, 8], self.color_matrix[2, 3], self.color_matrix[2, 7],
                      self.color_matrix[3, 8], self.color_matrix[3, 3], self.color_matrix[3, 7]))
        print("{0} {1} {2}|{3} {4} {5}|{6} {7} {8}|{9} {10} {11}"
              .format(self.color_matrix[5, 4], self.color_matrix[5, 0], self.color_matrix[5, 2],
                      self.color_matrix[0, 4], self.color_matrix[0, 0], self.color_matrix[0, 2],
                      self.color_matrix[2, 4], self.color_matrix[2, 0], self.color_matrix[2, 2],
                      self.color_matrix[3, 4], self.color_matrix[3, 0], self.color_matrix[3, 2]))
        print("{0} {1} {2}|{3} {4} {5}|{6} {7} {8}|{9} {10} {11}"
              .format(self.color_matrix[5, 5], self.color_matrix[5, 1], self.color_matrix[5, 6],
                      self.color_matrix[0, 5], self.color_matrix[0, 1], self.color_matrix[0, 6],
                      self.color_matrix[2, 5], self.color_matrix[2, 1], self.color_matrix[2, 6],
                      self.color_matrix[3, 5], self.color_matrix[3, 1], self.color_matrix[3, 6]))
        print("      -----")
        print("      {0} {1} {2}".format(self.color_matrix[1, 8], self.color_matrix[1, 3], self.color_matrix[1, 7]))
        print("      {0} {1} {2}".format(self.color_matrix[1, 4], self.color_matrix[1, 0], self.color_matrix[1, 2]))
        print("      {0} {1} {2}".format(self.color_matrix[1, 5], self.color_matrix[1, 1], self.color_matrix[1, 6]))
        print()

    def scramble(self, scramble):
        turns = [notation[turn] for turn in scramble.split()]
        for turn in turns:
            self.turn_face(turn[0], turn[1])

    def assert_valid_matrix(self):
        count_colors = {"color_U": 0, "color_F": 0, "color_R": 0, "color_D": 0, "color_B": 0, "color_L": 0}
        for face in self.color_matrix:
            for facelet in face:
                if facelet not in colors:
                    print("Invalid Matrix")
                    return
                elif facelet == colors[0]:
                    count_colors["color_U"] += 1
                elif facelet == colors[1]:
                    count_colors["color_F"] += 1
                elif facelet == colors[2]:
                    count_colors["color_R"] += 1
                elif facelet == colors[3]:
                    count_colors["color_D"] += 1
                elif facelet == colors[4]:
                    count_colors["color_B"] += 1
                elif facelet == colors[5]:
                    count_colors["color_L"] += 1
        for counted in count_colors.values():
            if counted != 9:
                print("Invalid Matrix")
                return

    def get_color_matrix(self):
        return self.color_matrix

    def set_color_matrix(self, matrix):
        self.color_matrix = matrix

    def get_binary_array(self, one_hot=False):
        if one_hot:
            binary_array = np.zeros(288).astype(int)
            for i in range(6):
                for j in range(1, 9):
                    if self.color_matrix[i][j] == colors[0]:
                        binary_array[(j - 1) * 6 + i * 48] = 1
                    elif self.color_matrix[i][j] == colors[1]:
                        binary_array[(j - 1) * 6 + 1 + i * 48] = 1
                    elif self.color_matrix[i][j] == colors[2]:
                        binary_array[(j - 1) * 6 + 2 + i * 48] = 1
                    elif self.color_matrix[i][j] == colors[3]:
                        binary_array[(j - 1) * 6 + 3 + i * 48] = 1
                    elif self.color_matrix[i][j] == colors[4]:
                        binary_array[(j - 1) * 6 + 4 + i * 48] = 1
                    elif self.color_matrix[i][j] == colors[5]:
                        binary_array[(j - 1) * 6 + 5 + i * 48] = 1
        else:
            binary_array = np.zeros(144).astype(int)
            for i in range(6):
                for j in range(1, 9):
                    if self.color_matrix[i][j] == colors[1]:
                        binary_array[(j - 1) * 3 + 1 + i * 24] = 1
                    elif self.color_matrix[i][j] == colors[2]:
                        binary_array[(j - 1) * 3 + 1 + i * 24] = 1
                        binary_array[(j - 1) * 3 + 2 + i * 24] = 1
                    elif self.color_matrix[i][j] == colors[3]:
                        binary_array[(j - 1) * 3 + i * 24] = 1
                    elif self.color_matrix[i][j] == colors[4]:
                        binary_array[(j - 1) * 3 + i * 24] = 1
                        binary_array[(j - 1) * 3 + 2 + i * 24] = 1
                    elif self.color_matrix[i][j] == colors[5]:
                        binary_array[(j - 1) * 3 + i * 24] = 1
                        binary_array[(j - 1) * 3 + 1 + i * 24] = 1

        return binary_array

    def set_corner(self, facelets, piece, position):
        type1_corners = [corners[0], corners[2], corners[5], corners[7]]
        if position > 3:
            position += 1
        if (piece[0] in type1_corners and position % 2 == 0) or (piece[0] not in type1_corners and position % 2 == 1):
            if piece[1] == 0:
                self.color_matrix[facelets[0]] = piece[0][0]
                self.color_matrix[facelets[1]] = piece[0][1]
                self.color_matrix[facelets[2]] = piece[0][2]
            elif piece[1] == 1:
                self.color_matrix[facelets[1]] = piece[0][0]
                self.color_matrix[facelets[2]] = piece[0][1]
                self.color_matrix[facelets[0]] = piece[0][2]
            else:
                self.color_matrix[facelets[2]] = piece[0][0]
                self.color_matrix[facelets[0]] = piece[0][1]
                self.color_matrix[facelets[1]] = piece[0][2]
        else:
            if piece[1] == 0:
                self.color_matrix[facelets[0]] = piece[0][0]
                self.color_matrix[facelets[2]] = piece[0][1]
                self.color_matrix[facelets[1]] = piece[0][2]
            elif piece[1] == 1:
                self.color_matrix[facelets[1]] = piece[0][0]
                self.color_matrix[facelets[0]] = piece[0][1]
                self.color_matrix[facelets[2]] = piece[0][2]
            else:
                self.color_matrix[facelets[2]] = piece[0][0]
                self.color_matrix[facelets[1]] = piece[0][1]
                self.color_matrix[facelets[0]] = piece[0][2]

    def set_matrix_from_pieces(self, pieces):
        # Set from edges
        # UF
        if pieces[0, 1] == 0:
            self.color_matrix[0, 1] = pieces[0, 0][0]
            self.color_matrix[1, 3] = pieces[0, 0][1]
        else:
            self.color_matrix[0, 1] = pieces[0, 0][1]
            self.color_matrix[1, 3] = pieces[0, 0][0]
        # UR
        if pieces[1, 1] == 0:
            self.color_matrix[0, 2] = pieces[1, 0][0]
            self.color_matrix[2, 4] = pieces[1, 0][1]
        else:
            self.color_matrix[0, 2] = pieces[1, 0][1]
            self.color_matrix[2, 4] = pieces[1, 0][0]
        # UB
        if pieces[2, 1] == 0:
            self.color_matrix[0, 3] = pieces[2, 0][0]
            self.color_matrix[4, 1] = pieces[2, 0][1]
        else:
            self.color_matrix[0, 3] = pieces[2, 0][1]
            self.color_matrix[4, 1] = pieces[2, 0][0]
        # UL
        if pieces[3, 1] == 0:
            self.color_matrix[0, 4] = pieces[3, 0][0]
            self.color_matrix[5, 2] = pieces[3, 0][1]
        else:
            self.color_matrix[0, 4] = pieces[3, 0][1]
            self.color_matrix[5, 2] = pieces[3, 0][0]
        # FL
        if pieces[4, 1] == 0:
            self.color_matrix[1, 4] = pieces[4, 0][0]
            self.color_matrix[5, 1] = pieces[4, 0][1]
        else:
            self.color_matrix[1, 4] = pieces[4, 0][1]
            self.color_matrix[5, 1] = pieces[4, 0][0]
        # FR
        if pieces[5, 1] == 0:
            self.color_matrix[1, 2] = pieces[5, 0][0]
            self.color_matrix[2, 1] = pieces[5, 0][1]
        else:
            self.color_matrix[1, 2] = pieces[5, 0][1]
            self.color_matrix[2, 1] = pieces[5, 0][0]
        # BR
        if pieces[6, 1] == 0:
            self.color_matrix[4, 2] = pieces[6, 0][0]
            self.color_matrix[2, 3] = pieces[6, 0][1]
        else:
            self.color_matrix[4, 2] = pieces[6, 0][1]
            self.color_matrix[2, 3] = pieces[6, 0][0]
        # BL
        if pieces[7, 1] == 0:
            self.color_matrix[4, 4] = pieces[7, 0][0]
            self.color_matrix[5, 3] = pieces[7, 0][1]
        else:
            self.color_matrix[4, 4] = pieces[7, 0][1]
            self.color_matrix[5, 3] = pieces[7, 0][0]
        # DF
        if pieces[8, 1] == 0:
            self.color_matrix[3, 1] = pieces[8, 0][0]
            self.color_matrix[1, 1] = pieces[8, 0][1]
        else:
            self.color_matrix[3, 1] = pieces[8, 0][1]
            self.color_matrix[1, 1] = pieces[8, 0][0]
        # DR
        if pieces[9, 1] == 0:
            self.color_matrix[3, 4] = pieces[9, 0][0]
            self.color_matrix[2, 2] = pieces[9, 0][1]
        else:
            self.color_matrix[3, 4] = pieces[9, 0][1]
            self.color_matrix[2, 2] = pieces[9, 0][0]
        # DB
        if pieces[10, 1] == 0:
            self.color_matrix[3, 3] = pieces[10, 0][0]
            self.color_matrix[4, 3] = pieces[10, 0][1]
        else:
            self.color_matrix[3, 3] = pieces[10, 0][1]
            self.color_matrix[4, 3] = pieces[10, 0][0]
        # DL
        if pieces[11, 1] == 0:
            self.color_matrix[3, 2] = pieces[11, 0][0]
            self.color_matrix[5, 4] = pieces[11, 0][1]
        else:
            self.color_matrix[3, 2] = pieces[11, 0][1]
            self.color_matrix[5, 4] = pieces[11, 0][0]

        # Set from corners
        facelets = [(0, 5), (1, 8), (5, 6)]
        self.set_corner(facelets, pieces[12], 0)
        facelets = [(0, 6), (1, 7), (2, 5)]
        self.set_corner(facelets, pieces[13], 1)
        facelets = [(0, 7), (4, 6), (2, 8)]
        self.set_corner(facelets, pieces[14], 2)
        facelets = [(0, 8), (4, 5), (5, 7)]
        self.set_corner(facelets, pieces[15], 3)
        facelets = [(3, 6), (1, 5), (5, 5)]
        self.set_corner(facelets, pieces[16], 4)
        facelets = [(3, 5), (1, 6), (2, 6)]
        self.set_corner(facelets, pieces[17], 5)
        facelets = [(3, 8), (4, 7), (2, 7)]
        self.set_corner(facelets, pieces[18], 6)
        facelets = [(3, 7), (4, 8), (5, 8)]
        self.set_corner(facelets, pieces[19], 7)
