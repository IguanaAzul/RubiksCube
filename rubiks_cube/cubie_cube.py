import numpy as np
from utils import pieces_ref, int_face, notation, swap4


class CubieCube:
    def __init__(self):
        self.pieces = pieces_ref.copy()

    def swap(self, to_swap, way):
        self.pieces[to_swap[0]], self.pieces[to_swap[1]], self.pieces[to_swap[2]], self.pieces[to_swap[3]] = \
            swap4(self.pieces[to_swap[0]].copy(), self.pieces[to_swap[1]].copy(),
                  self.pieces[to_swap[2]].copy(), self.pieces[to_swap[3]].copy(),
                  way)

    def corner_turn(self, turn, corners_to_swap, way):
        for corner in corners_to_swap:
            if turn == 0 or turn == 3:
                # U or D
                if self.pieces[corner][1] == 2:
                    self.pieces[corner][1] = 1
                elif self.pieces[corner][1] == 1:
                    self.pieces[corner][1] = 2
            if turn == 1 or turn == 4:
                # F or D
                if self.pieces[corner][1] == 2:
                    self.pieces[corner][1] = 0
                elif self.pieces[corner][1] == 0:
                    self.pieces[corner][1] = 2
            if turn == 2 or turn == 4:
                # R or L
                if self.pieces[corner][1] == 1:
                    self.pieces[corner][1] = 0
                elif self.pieces[corner][1] == 0:
                    self.pieces[corner][1] = 1
        self.swap(corners_to_swap, way)

    def edges_turn(self, turn, edges_to_swap, way):
        for edge in edges_to_swap:
            if turn == 2 or turn == 4:
                # R or L
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
            corners_to_swap = [14, 15, 18, 19]
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
        return self.pieces

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

    def set_pieces_from_matrix(self, matrix):
        # TODO
        return
