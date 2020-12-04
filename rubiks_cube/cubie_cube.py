import numpy as np
from utils import pieces_ref, int_face, notation, swap4, colors


class CubieCube:
    def __init__(self):
        self.pieces = pieces_ref.copy()

    def swap(self, to_swap, way):
        self.pieces[to_swap[0]], self.pieces[to_swap[1]], self.pieces[to_swap[2]], self.pieces[to_swap[3]] = \
            swap4(self.pieces[to_swap[0]].copy(), self.pieces[to_swap[1]].copy(),
                  self.pieces[to_swap[2]].copy(), self.pieces[to_swap[3]].copy(),
                  way)

    def corner_turn(self, turn, corners_to_swap, way):
        if way != 2:
            for corner in corners_to_swap:
                if turn == 0 or turn == 3:
                    # U or D
                    if self.pieces[corner][1] == 2:
                        self.pieces[corner][1] = 1
                    elif self.pieces[corner][1] == 1:
                        self.pieces[corner][1] = 2
                if turn == 1 or turn == 4:
                    # F or B
                    if self.pieces[corner][1] == 2:
                        self.pieces[corner][1] = 0
                    elif self.pieces[corner][1] == 0:
                        self.pieces[corner][1] = 2
                if turn == 2 or turn == 5:
                    # R or L
                    if self.pieces[corner][1] == 1:
                        self.pieces[corner][1] = 0
                    elif self.pieces[corner][1] == 0:
                        self.pieces[corner][1] = 1
        self.swap(corners_to_swap, way)

    def edges_turn(self, turn, edges_to_swap, way):
        if way != 2:
            for edge in edges_to_swap:
                if turn == 1 or turn == 4:
                    # F or B
                    if self.pieces[edge][1] == 1:
                        self.pieces[edge][1] = 0
                    elif self.pieces[edge][1] == 0:
                        self.pieces[edge][1] = 1
        self.swap(edges_to_swap, way)

    def turn_face(self, face, way=0):
        """
        Makes a turn on the cube.
        :param face: Face to turn (Should be one of [U, R, B, D, F, L]).
        :param way: 0 to clockwise turn, 1 to counterclockwise turn, 2 to double turn.
        :return: No return, the cube gets turned inplace.
        """
        turn = int_face[face]
        # UP
        if turn == 0:
            edges_to_swap = [0, 1, 2, 3]
            corners_to_swap = [12, 13, 14, 15]
        # FRONT
        elif turn == 1:
            edges_to_swap = [8, 5, 0, 4]
            corners_to_swap = [16, 17, 13, 12]
        # RIGHT
        elif turn == 2:
            edges_to_swap = [1, 5, 9, 6]
            corners_to_swap = [17, 18, 14, 13]
        # DOWN
        elif turn == 3:
            edges_to_swap = [11, 10, 9, 8]
            corners_to_swap = [19, 18, 17, 16]
        # BACK
        elif turn == 4:
            edges_to_swap = [2, 6, 10, 7]
            corners_to_swap = [15, 14, 18, 19]
        # LEFT
        elif turn == 5:
            edges_to_swap = [3, 7, 11, 4]
            corners_to_swap = [12, 15, 19, 16]
        else:
            print("Error: Invalid face to turn")
            return

        self.corner_turn(turn, corners_to_swap, way)
        self.edges_turn(turn, edges_to_swap, way)

    def n_pieces_in_place(self):
        """
        Counts how many pieces are in the correct place.
        :return: Number of pieces in the correct place.
        """
        return sum(np.all(self.pieces == pieces_ref, axis=1))

    def print(self):
        """
        Prints the state of the rubiks cube.
        :return: None.
        """
        for piece in self.pieces:
            print(piece)

    def scramble(self, scramble):
        """
        Scrambles the cube.
        :param scramble: String in official scramble notation.
        :return: None, the cube scrambles inplace.
        """
        turns = [notation[turn] for turn in scramble.split()]
        for turn in turns:
            self.turn_face(turn[0], turn[1])

    def get_pieces(self):
        """
        Returns pieces.
        :return: Pieces
        """
        return self.pieces.copy()

    def set_pieces(self, pieces):
        """
        Sets pieces (Doesn't check if the pieces are a valid cube,
        if it isn`t you might run into problems if you want it to be solvable."
        :param pieces: Pieces in the standard format
        :return: None
        """
        self.pieces = pieces

    def get_corners_orientation(self):
        return self.pieces[12:, 1]

    def get_edges_orientation(self):
        return self.pieces[:12, 1]

    def set_edge(self, matrix, facelets, piece_num):
        if matrix[facelets[0]] == colors[0] or matrix[facelets[1]] == colors[0] or \
           matrix[facelets[0]] == colors[3] or matrix[facelets[1]] == colors[3]:
            if matrix[facelets[0]] == colors[0] or matrix[facelets[0]] == colors[3]:
                self.pieces[piece_num][0] = matrix[facelets[0]] + matrix[facelets[1]]
                self.pieces[piece_num][1] = 0
            else:
                self.pieces[piece_num][0] = matrix[facelets[1]] + matrix[facelets[0]]
                self.pieces[piece_num][1] = 1
        else:
            if matrix[facelets[0]] == colors[1] or matrix[facelets[0]] == colors[4]:
                self.pieces[piece_num][0] = matrix[facelets[0]] + matrix[facelets[1]]
                self.pieces[piece_num][1] = 0
            else:
                self.pieces[piece_num][0] = matrix[facelets[1]] + matrix[facelets[0]]
                self.pieces[piece_num][1] = 1

    def set_corner(self, matrix, facelets, piece_num):
        if matrix[facelets[0]] == colors[0] or matrix[facelets[0]] == colors[3]:
            self.pieces[piece_num][1] = 0
            if matrix[facelets[1]] == colors[1] or matrix[facelets[1]] == colors[4]:
                self.pieces[piece_num][0] = matrix[facelets[0]] + matrix[facelets[1]] + matrix[facelets[2]]
            else:
                self.pieces[piece_num][0] = matrix[facelets[0]] + matrix[facelets[2]] + matrix[facelets[1]]
        elif matrix[facelets[1]] == colors[0] or matrix[facelets[1]] == colors[3]:
            self.pieces[piece_num][1] = 1
            if matrix[facelets[0]] == colors[1] or matrix[facelets[0]] == colors[4]:
                self.pieces[piece_num][0] = matrix[facelets[1]] + matrix[facelets[0]] + matrix[facelets[2]]
            else:
                self.pieces[piece_num][0] = matrix[facelets[1]] + matrix[facelets[2]] + matrix[facelets[0]]
        else:
            self.pieces[piece_num][1] = 2
            if matrix[facelets[0]] == colors[1] or matrix[facelets[0]] == colors[4]:
                self.pieces[piece_num][0] = matrix[facelets[2]] + matrix[facelets[0]] + matrix[facelets[1]]
            else:
                self.pieces[piece_num][0] = matrix[facelets[2]] + matrix[facelets[1]] + matrix[facelets[0]]

    def set_pieces_from_matrix(self, matrix):
        # Set edges
        self.set_edge(matrix, [(0, 1), (1, 3)], 0)      # UF
        self.set_edge(matrix, [(0, 2), (2, 4)], 1)      # UR
        self.set_edge(matrix, [(0, 3), (4, 1)], 2)      # UB
        self.set_edge(matrix, [(0, 4), (5, 2)], 3)      # UL
        self.set_edge(matrix, [(1, 4), (5, 1)], 4)      # FL
        self.set_edge(matrix, [(1, 2), (2, 1)], 5)      # FR
        self.set_edge(matrix, [(4, 2), (2, 3)], 6)      # BR
        self.set_edge(matrix, [(4, 4), (5, 3)], 7)      # BL
        self.set_edge(matrix, [(3, 1), (1, 1)], 8)      # DF
        self.set_edge(matrix, [(3, 4), (2, 2)], 9)      # DR
        self.set_edge(matrix, [(3, 3), (4, 3)], 10)     # DB
        self.set_edge(matrix, [(3, 2), (5, 4)], 11)     # DL

        # Set corners
        self.set_corner(matrix, [(0, 5), (1, 8), (5, 6)], 12)       # UFL
        self.set_corner(matrix, [(0, 6), (1, 7), (2, 5)], 13)       # UFR
        self.set_corner(matrix, [(0, 7), (4, 6), (2, 8)], 14)       # UBR
        self.set_corner(matrix, [(0, 8), (4, 5), (5, 7)], 15)       # UBL
        self.set_corner(matrix, [(3, 6), (1, 5), (5, 5)], 16)       # DFL
        self.set_corner(matrix, [(3, 5), (1, 6), (2, 6)], 17)       # DFR
        self.set_corner(matrix, [(3, 8), (4, 7), (2, 7)], 18)       # DBR
        self.set_corner(matrix, [(3, 7), (4, 8), (5, 8)], 19)       # DBL
