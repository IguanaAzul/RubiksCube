import numpy as np
from itertools import groupby
import random


matrix_ref = np.array([['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                       ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'],
                       ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']])

pieces_ref = np.array([[1, 'w', 'g', None], [1, 'w', 'r', None], [1, 'w', 'b', None], [1, 'w', 'o', None],
                       [1, 'g', 'o', None], [1, 'g', 'r', None], [1, 'r', 'b', None], [1, 'b', 'o', None],
                       [1, 'y', 'g', None], [1, 'y', 'r', None], [1, 'y', 'b', None], [1, 'y', 'o', None],
                       [2, 'w', 'g', 'o'], [2, 'w', 'g', 'r'], [2, 'w', 'b', 'r'], [2, 'w', 'b', 'o'],
                       [2, 'y', 'g', 'o'], [2, 'y', 'g', 'r'], [2, 'y', 'b', 'r'], [2, 'y', 'b', 'o']])

to_int = {'w': 0, 'g': 1, 'r': 2, 'y': 3, 'b': 4, 'o': 5, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

to_color = {0: 'w', 1: 'g', 2: 'r', 3: 'y', 4: 'b', 5: 'o', 'w': 'w', 'g': 'g', 'r': 'r', 'y': 'y', 'b': 'b', 'o': 'o'}

char_face = {0: 'U', 1: 'F', 2: 'R', 3: 'D', 4: 'B', 5: 'L', 'U': 'U', 'F': 'F', 'R': 'R', 'D': 'D', 'B': 'B', 'L': 'L'}

int_face = {'U': 0, 'F': 1, 'R': 2, 'D': 3, 'B': 4, 'L': 5, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

notation = {'U': [0, 0], 'F': [1, 0], 'R': [2, 0], 'D': [3, 0], 'B': [4, 0], 'L': [5, 0],
            'U\'': [0, 1], 'F\'': [1, 1], 'R\'': [2, 1], 'D\'': [3, 1], 'B\'': [4, 1], 'L\'': [5, 1],
            'U2': [0, 2], 'F2': [1, 2], 'R2': [2, 2], 'D2': [3, 2], 'B2': [4, 2], 'L2': [5, 2]}


def swap4(a, b, c, d, way):
    """
    Swaps Four Values.
    :param a: Value 1.
    :param b: Value 2.
    :param c: Value 3.
    :param d: Value 4.
    :param way: 0 to clockwise swap, 1 to counterclockwise swap, 2 to double swap.
    :return: swapped values.
    """
    if way:
        aux = d
        d = c
        c = b
        b = a
        a = aux
        if way == 2:
            a, b, c, d = swap4(a, b, c, d, 1)
    else:
        aux = a
        a = b
        b = c
        c = d
        d = aux
    return a, b, c, d


def scramble_generator(length):
    """
    Generates Scramble.
    :param length: Length of the random scramble.
    :return: Random scramble.
    """
    int_to_turn = {1: 'U', 2: 'F', 3: 'R', 4: 'D', 5: 'B', 6: 'L',
                   7: 'U\'', 8: 'F\'', 9: 'R\'', 10: 'D\'', 11: 'B\'', 12: 'L\'',
                   13: 'U2', 14: 'F2', 15: 'R2', 16: 'D2', 17: 'B2', 18: 'L2'}
    scramble = np.random.randint(6, size=length) + 1
    scramble = [k for k, g in groupby(scramble) if k != 0]
    for idx in range(len(scramble)):
        odds = random.randint(0, 300)
        if odds < 100:
            scramble[idx] += 6
        elif odds < 200:
            scramble[idx] += 12
    return ' '.join([int_to_turn[i] for i in scramble]) + '\n'


class Cube:
    """
    Implements a 3x3x3 Rubiks Cube.
    """
    def __init__(self):
        self.matrix_colors = matrix_ref.copy()
        self.pieces = pieces_ref.copy()

    def turn_face(self, face, way=0):
        """
        Makes a turn on the cube.
        :param face: Face to turn (Should be one of [U, R, B, D, F, L]).
        :param way: 0 to clockwise turn, 1 to counterclockwise turn, 2 to double turn.
        :return: No return, the cube gets turned inplace.
        """
        turn = int_face[face]
        self.matrix_colors[turn, 1], self.matrix_colors[turn, 2], self.matrix_colors[turn, 3], self.matrix_colors[turn, 4] = swap4(self.matrix_colors[turn, 1],
        self.matrix_colors[turn, 2], self.matrix_colors[turn, 3], self.matrix_colors[turn, 4], way)

        self.matrix_colors[turn, 5], self.matrix_colors[turn, 6], self.matrix_colors[turn, 7], self.matrix_colors[turn, 8] = swap4(self.matrix_colors[turn, 5],
        self.matrix_colors[turn, 6], self.matrix_colors[turn, 7], self.matrix_colors[turn, 8], way)
        # UP
        if turn == 0:
            self.pieces[0], self.pieces[1], self.pieces[2], self.pieces[3] = swap4(self.pieces[0], self.pieces[1], 
                                                                               self.pieces[2], self.pieces[3], way)

            self.pieces[12], self.pieces[13], self.pieces[14], self.pieces[15] = swap4(self.pieces[12], self.pieces[13], 
                                                                                   self.pieces[14], self.pieces[15], way)

            self.matrix_colors[1, 3], self.matrix_colors[2, 4], self.matrix_colors[4, 1], self.matrix_colors[5, 2] = swap4(self.matrix_colors[1, 3],
            self.matrix_colors[2, 4], self.matrix_colors[4, 1], self.matrix_colors[5, 2], way)

            self.matrix_colors[1, 7], self.matrix_colors[2, 8], self.matrix_colors[4, 5], self.matrix_colors[5, 6] = swap4(self.matrix_colors[1, 7],
            self.matrix_colors[2, 8], self.matrix_colors[4, 5], self.matrix_colors[5, 6], way)

            self.matrix_colors[1, 8], self.matrix_colors[2, 5], self.matrix_colors[4, 6], self.matrix_colors[5, 7] = swap4(self.matrix_colors[1, 8],
            self.matrix_colors[2, 5], self.matrix_colors[4, 6], self.matrix_colors[5, 7], way)
        # FRONT
        elif turn == 1:
            self.pieces[8], self.pieces[5], self.pieces[0], self.pieces[4] = swap4(self.pieces[8], self.pieces[5], 
                                                                               self.pieces[0], self.pieces[4], way)

            self.pieces[16], self.pieces[17], self.pieces[13], self.pieces[12] = swap4(self.pieces[16], self.pieces[17], 
                                                                                   self.pieces[13], self.pieces[12], way)

            self.matrix_colors[3, 1], self.matrix_colors[2, 1], self.matrix_colors[0, 1], self.matrix_colors[5, 1] = swap4(self.matrix_colors[3, 1],
            self.matrix_colors[2, 1], self.matrix_colors[0, 1], self.matrix_colors[5, 1], way)

            self.matrix_colors[3, 5], self.matrix_colors[2, 5], self.matrix_colors[0, 5], self.matrix_colors[5, 5] = swap4(self.matrix_colors[3, 5],
            self.matrix_colors[2, 5], self.matrix_colors[0, 5], self.matrix_colors[5, 5], way)

            self.matrix_colors[3, 6], self.matrix_colors[2, 6], self.matrix_colors[0, 6], self.matrix_colors[5, 6] = swap4(self.matrix_colors[3, 6],
            self.matrix_colors[2, 6], self.matrix_colors[0, 6], self.matrix_colors[5, 6], way)
        # RIGHT
        elif turn == 2:
            self.pieces[1], self.pieces[5], self.pieces[9], self.pieces[6] = swap4(self.pieces[1], self.pieces[5], 
                                                                               self.pieces[9], self.pieces[6], way)

            self.pieces[17], self.pieces[18], self.pieces[14], self.pieces[13] = swap4(self.pieces[17], self.pieces[18], 
                                                                                   self.pieces[14], self.pieces[13], way)

            self.matrix_colors[0, 2], self.matrix_colors[1, 2], self.matrix_colors[3, 4], self.matrix_colors[4, 2] = swap4(self.matrix_colors[0, 2],
            self.matrix_colors[1, 2], self.matrix_colors[3, 4], self.matrix_colors[4, 2], way)

            self.matrix_colors[0, 6], self.matrix_colors[1, 6], self.matrix_colors[3, 8], self.matrix_colors[4, 6] = swap4(self.matrix_colors[0, 6],
            self.matrix_colors[1, 6], self.matrix_colors[3, 8], self.matrix_colors[4, 6], way)

            self.matrix_colors[0, 7], self.matrix_colors[1, 7], self.matrix_colors[3, 5], self.matrix_colors[4, 7] = swap4(self.matrix_colors[0, 7],
            self.matrix_colors[1, 7], self.matrix_colors[3, 5], self.matrix_colors[4, 7], way)
        # DOWN
        elif turn == 3:
            self.pieces[11], self.pieces[10], self.pieces[9], self.pieces[8] = swap4(self.pieces[11], self.pieces[10], 
                                                                                 self.pieces[9], self.pieces[8], way)

            self.pieces[19], self.pieces[18], self.pieces[17], self.pieces[16] = swap4(self.pieces[19], self.pieces[18], 
                                                                                   self.pieces[17], self.pieces[16], way)

            self.matrix_colors[1, 1], self.matrix_colors[5, 4], self.matrix_colors[4, 3], self.matrix_colors[2, 2] = swap4(self.matrix_colors[1, 1],
            self.matrix_colors[5, 4], self.matrix_colors[4, 3], self.matrix_colors[2, 2], way)

            self.matrix_colors[5, 8], self.matrix_colors[4, 7], self.matrix_colors[2, 6], self.matrix_colors[1, 5] = swap4(self.matrix_colors[5, 8],
            self.matrix_colors[4, 7], self.matrix_colors[2, 6], self.matrix_colors[1, 5], way)

            self.matrix_colors[5, 5], self.matrix_colors[4, 8], self.matrix_colors[2, 7], self.matrix_colors[1, 6] = swap4(self.matrix_colors[5, 5],
            self.matrix_colors[4, 8], self.matrix_colors[2, 7], self.matrix_colors[1, 6], way)
        # BACK
        elif turn == 4:
            self.pieces[2], self.pieces[6], self.pieces[10], self.pieces[7] = swap4(self.pieces[2], self.pieces[6], 
                                                                                self.pieces[10], self.pieces[7], way)

            self.pieces[14], self.pieces[15], self.pieces[18], self.pieces[19] = swap4(self.pieces[14], self.pieces[15], 
                                                                                   self.pieces[18], self.pieces[19], way)

            self.matrix_colors[0, 3], self.matrix_colors[2, 3], self.matrix_colors[3, 3], self.matrix_colors[5, 3] = swap4(self.matrix_colors[0, 3],
            self.matrix_colors[2, 3], self.matrix_colors[3, 3], self.matrix_colors[5, 3], way)

            self.matrix_colors[0, 8], self.matrix_colors[2, 8], self.matrix_colors[3, 8], self.matrix_colors[5, 8] = swap4(self.matrix_colors[0, 8],
            self.matrix_colors[2, 8], self.matrix_colors[3, 8], self.matrix_colors[5, 8], way)

            self.matrix_colors[0, 7], self.matrix_colors[2, 7], self.matrix_colors[3, 7], self.matrix_colors[5, 7] = swap4(self.matrix_colors[0, 7],
            self.matrix_colors[2, 7], self.matrix_colors[3, 7], self.matrix_colors[5, 7], way)
        # LEFT
        elif turn == 5:
            self.pieces[3], self.pieces[7], self.pieces[11], self.pieces[4] = swap4(self.pieces[3], self.pieces[7], 
                                                                                self.pieces[11], self.pieces[4], way)

            self.pieces[12], self.pieces[15], self.pieces[19], self.pieces[16] = swap4(self.pieces[12], self.pieces[15], 
                                                                                   self.pieces[19], self.pieces[16], way)

            self.matrix_colors[0, 4], self.matrix_colors[4, 4], self.matrix_colors[3, 2], self.matrix_colors[1, 4] = swap4(self.matrix_colors[0, 4],
            self.matrix_colors[4, 4], self.matrix_colors[3, 2], self.matrix_colors[1, 4], way)

            self.matrix_colors[1, 8], self.matrix_colors[0, 8], self.matrix_colors[4, 8], self.matrix_colors[3, 6] = swap4(self.matrix_colors[1, 8],
            self.matrix_colors[0, 8], self.matrix_colors[4, 8], self.matrix_colors[3, 6], way)

            self.matrix_colors[1, 5], self.matrix_colors[0, 5], self.matrix_colors[4, 5], self.matrix_colors[3, 7] = swap4(self.matrix_colors[1, 5],
            self.matrix_colors[0, 5], self.matrix_colors[4, 5], self.matrix_colors[3, 7], way)

    def is_solved(self):
        """
        Checks if cube is solved.
        :return: True for solved and False for not solved.
        """
        return np.array_equal(self.matrix_colors, matrix_ref)

    def n_colors_in_place(self):
        """
        Counts how many colors are in the correct place.
        :return: Number of colors in the correct place.
        """
        return np.sum(self.matrix_colors == matrix_ref)

    def n_pieces_in_place(self):
        """
        Counts how many pieces are in the correct place.
        :return: Number of pieces in the correct place.
        """
        return sum(np.all(self.pieces == pieces_ref, axis=1))

    def n_oriented_pieces_in_place(self):
        """
        Counts how many pieces are in the correct place and also oriented correctly.
        :return: Number of pieces in the correct place and also oriented correctly.
        """
        k = 0
        for idx, i in enumerate(np.all(self.pieces == pieces_ref, axis=1)):
            if i:
                if idx == 0 and self.matrix_colors[0, 1] == 'w':
                    k += 1
                elif idx == 1 and self.matrix_colors[0, 2] == 'w':
                    k += 1
                elif idx == 2 and self.matrix_colors[0, 3] == 'w':
                    k += 1
                elif idx == 3 and self.matrix_colors[0, 4] == 'w':
                    k += 1
                elif idx == 4 and self.matrix_colors[1, 4] == 'g':
                    k += 1
                elif idx == 5 and self.matrix_colors[1, 2] == 'g':
                    k += 1
                elif idx == 6 and self.matrix_colors[2, 3] == 'r':
                    k += 1
                elif idx == 7 and self.matrix_colors[5, 3] == 'o':
                    k += 1
                elif idx == 8 and self.matrix_colors[1, 1] == 'g':
                    k += 1
                elif idx == 9 and self.matrix_colors[2, 2] == 'r':
                    k += 1
                elif idx == 10 and self.matrix_colors[4, 3] == 'b':
                    k += 1
                elif idx == 11 and self.matrix_colors[5, 4] == 'o':
                    k += 1
                elif idx == 12 and self.matrix_colors[0, 5] == 'w':
                    k += 1
                elif idx == 13 and self.matrix_colors[0, 6] == 'w':
                    k += 1
                elif idx == 14 and self.matrix_colors[0, 7] == 'w':
                    k += 1
                elif idx == 15 and self.matrix_colors[0, 8] == 'w':
                    k += 1
                elif idx == 16 and self.matrix_colors[3, 6] == 'y':
                    k += 1
                elif idx == 17 and self.matrix_colors[3, 5] == 'y':
                    k += 1
                elif idx == 18 and self.matrix_colors[3, 8] == 'y':
                    k += 1
                elif idx == 19 and self.matrix_colors[3, 7] == 'y':
                    k += 1
        return k
    
    def print_cube(self):
        """
        Prints the state of the rubiks cube.
        :return: None.
        """
        print("rubiks_cube: \n")
        print("      {0} {1} {2}".format(self.matrix_colors[4, 8], self.matrix_colors[4, 3], self.matrix_colors[4, 7]))
        print("      {0} {1} {2}".format(self.matrix_colors[4, 4], self.matrix_colors[4, 0], self.matrix_colors[4, 2]))
        print("      {0} {1} {2}".format(self.matrix_colors[4, 5], self.matrix_colors[4, 1], self.matrix_colors[4, 6]))
        print("      -----")
        print("{0} {1} {2}|".format(self.matrix_colors[5, 8], self.matrix_colors[5, 3], self.matrix_colors[5, 7]), end='')
        print("{0} {1} {2}|".format(self.matrix_colors[0, 8], self.matrix_colors[0, 3], self.matrix_colors[0, 7]), end='')
        print("{0} {1} {2}|".format(self.matrix_colors[2, 8], self.matrix_colors[2, 3], self.matrix_colors[2, 7]), end='')
        print("{0} {1} {2}".format(self.matrix_colors[3, 8], self.matrix_colors[3, 3], self.matrix_colors[3, 7]))
        print("{0} {1} {2}|".format(self.matrix_colors[5, 4], self.matrix_colors[5, 0], self.matrix_colors[5, 2]), end='')
        print("{0} {1} {2}|".format(self.matrix_colors[0, 4], self.matrix_colors[0, 0], self.matrix_colors[0, 2]), end='')
        print("{0} {1} {2}|".format(self.matrix_colors[2, 4], self.matrix_colors[2, 0], self.matrix_colors[2, 2]), end='')
        print("{0} {1} {2} ".format(self.matrix_colors[3, 4], self.matrix_colors[3, 0], self.matrix_colors[3, 2]))
        print("{0} {1} {2}|".format(self.matrix_colors[5, 5], self.matrix_colors[5, 1], self.matrix_colors[5, 6]), end='')
        print("{0} {1} {2}|".format(self.matrix_colors[0, 5], self.matrix_colors[0, 1], self.matrix_colors[0, 6]), end='')
        print("{0} {1} {2}|".format(self.matrix_colors[2, 5], self.matrix_colors[2, 1], self.matrix_colors[2, 6]), end='')
        print("{0} {1} {2} ".format(self.matrix_colors[3, 5], self.matrix_colors[3, 1], self.matrix_colors[3, 6]))
        print("      -----")
        print("      {0} {1} {2}".format(self.matrix_colors[1, 8], self.matrix_colors[1, 3], self.matrix_colors[1, 7]))
        print("      {0} {1} {2}".format(self.matrix_colors[1, 4], self.matrix_colors[1, 0], self.matrix_colors[1, 2]))
        print("      {0} {1} {2}".format(self.matrix_colors[1, 5], self.matrix_colors[1, 1], self.matrix_colors[1, 6]))
        print()

    def scramble_cube(self, scramble):
        """
        Scrambles the cube.
        :param scramble: String in official scramble notation.
        :return: None, the cube scrambles inplace.
        """
        turns = [notation[turn] for turn in scramble.split()]
        for turn in turns:
            self.turn_face(turn[0], turn[1])

    def get_matrix(self):
        """
        Returns color matrix.
        :return: Color Matrix
        """
        return self.matrix_colors

    def set_matrix(self, matrix):
        """
        Sets matrix color (Doesn`t check if the matrix is a valid cube,
        if it isn`t you might run into problems if you want it to be solvable."
        :param matrix: Color Matrix in the standard format
        :return: None
        """
        self.matrix_colors = matrix

    def get_binary_matrix(self, one_hot=False):
        """
        Returns the color matrix as a binary matrix for whatever purpose you`d like.
        :param one_hot: True if you want it to be onehot encoded.
        :return: Binary color matrix.
        """
        if one_hot:
            binary_matrix = np.zeros(144)
            for i in range(6):
                for j in range(1, 9):
                    if self.matrix_colors[i][j] == 'w':
                        binary_matrix[(j - 1) * 3 + 2 + i * 24] = 0
                    elif self.matrix_colors[i][j] == 'g':
                        binary_matrix[(j - 1) * 3 + 1 + i * 24] = 1
                    elif self.matrix_colors[i][j] == 'r':
                        binary_matrix[(j - 1) * 3 + 1 + i * 24] = 1
                        binary_matrix[(j - 1) * 3 + 2 + i * 24] = 1
                    elif self.matrix_colors[i][j] == 'y':
                        binary_matrix[(j - 1) * 3 + i * 24] = 1.0
                    elif self.matrix_colors[i][j] == 'b':
                        binary_matrix[(j - 1) * 3 + i * 24] = 1.0
                        binary_matrix[(j - 1) * 3 + 2 + i * 24] = 1.0
                    elif self.matrix_colors[i][j] == 'o':
                        binary_matrix[(j - 1) * 3 + i * 24] = 1.0
                        binary_matrix[(j - 1) * 3 + 1 + i * 24] = 1.0
        else:
            binary_matrix = np.zeros(288)
            for i in range(6):
                for j in range(1, 9):
                    m = 5 if j == 0 else 1
                    if self.matrix_colors[i][j] == 'w':
                        binary_matrix[(j-1)*6+i*48] = 1 * m
                    elif self.matrix_colors[i][j] == 'g':
                        binary_matrix[(j-1)*6+1+i*48]=1 * m
                    elif self.matrix_colors[i][j] == 'r':
                        binary_matrix[(j-1)*6+2+i*48]=1 * m
                    elif self.matrix_colors[i][j] == 'y':
                        binary_matrix[(j-1)*6+3+i*48]=1 * m
                    elif self.matrix_colors[i][j] == 'b':
                        binary_matrix[(j-1)*6+4+i*48]=1 * m
                    elif self.matrix_colors[i][j] == 'o':
                        binary_matrix[(j-1)*6+5+i*48]=1 * m
        return binary_matrix
