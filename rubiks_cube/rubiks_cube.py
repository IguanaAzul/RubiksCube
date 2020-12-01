import numpy as np
from utils import matrix_ref, pieces_ref, bin_to_color
from rubiks_cube.face_cube import FaceCube
from rubiks_cube.cubie_cube import CubieCube


class Cube:
    """
    Implements a 3x3x3 Rubiks Cube.
    """
    def __init__(self):
        self.face_cube = FaceCube()
        self.cubie_cube = CubieCube()

    def turn_face(self, face, way=0):
        """
        Makes a turn on the cube.
        :param face: Face to turn (Should be one of [U, R, B, D, F, L]).
        :param way: 0 to clockwise turn, 1 to counterclockwise turn, 2 to double turn.
        :return: No return, the cube gets turned inplace.
        """
        self.face_cube.turn_face(face, way)
        self.cubie_cube.turn_face(face, way)

    def is_solved(self):
        """
        Checks if cube is solved.
        :return: True for solved and False for not solved.
        """
        return self.face_cube.is_solved()

    def n_colors_in_place(self):
        """
        Counts how many colors are in the correct place.
        :return: Number of colors in the correct place.
        """
        return self.face_cube.n_colors_in_place()

    def n_pieces_in_place(self):
        """
        Counts how many pieces are in the correct place.
        :return: Number of pieces in the correct place.
        """
        return self.cubie_cube.n_pieces_in_place()

    def print(self):
        """
        Prints the state of the rubiks cube.
        :return: None.
        """
        self.face_cube.print()

    def scramble(self, scramble):
        """
        Scrambles the cube.
        :param scramble: String in official scramble notation.
        :return: None, the cube scrambles inplace.
        """
        if scramble is not None and not scramble == "":
            self.face_cube.scramble(scramble)
            self.cubie_cube.scramble(scramble)

    def get_color_matrix(self):
        """
        Returns color matrix.
        :return: Color Matrix
        """
        return self.face_cube.get_color_matrix()

    def set_cube(self, setter):
        if type(setter) is tuple:
            self.face_cube.set_color_matrix(setter[0])
            self.cubie_cube.set_pieces(setter[1])
        elif isinstance(setter, np.ndarray):
            if setter.shape == matrix_ref.shape:
                self.face_cube.set_color_matrix(setter)
                self.cubie_cube.set_pieces_from_matrix(setter)
            elif setter.shape == pieces_ref.shape:
                self.face_cube.set_matrix_from_pieces(setter)
                self.cubie_cube.set_pieces(setter)
            else:
                print("Error: Format to set cube unknown")
        else:
            print("Error: Format to set cube unknown")

    def get_pieces(self):
        """
        Returns pieces.
        :return: Pieces
        """
        return self.cubie_cube.get_pieces()

    def get_binary_array(self, one_hot=False):
        """
        Returns the color matrix as a binary array for whatever purpose you`d like.
        :param one_hot: True if you want it to be onehot encoded.
        :return: Binary color matrix.
        """
        return self.face_cube.get_binary_array(one_hot)

    def get_corners_orientation(self):
        return self.cubie_cube.get_corners_orientation()

    def get_edges_orientation(self):
        return self.cubie_cube.get_edges_orientation()

    def save_cube(self, path):
        file = open(path, "wb")
        bin_to_save = "".join(self.get_binary_array().astype(str))
        bin_to_save = bin_to_save
        bin_to_save = int(bin_to_save[::-1], base=2).to_bytes(32, "little")
        file.write(bin_to_save)

    def load_cube(self, path):
        file = open(path, "rb")
        binary_array = file.read()
        binary_array = np.array(list("{:0<144}".format(format(int.from_bytes(binary_array, "little"), "032b")[::-1])))
        binary_array = binary_array.reshape(-1, 3).astype(int)
        load_matrix = matrix_ref.copy()
        for i in range(6):
            for j in range(1, 9):
                load_matrix[i][j] = bin_to_color[tuple(binary_array[i*8+(j-1)])]
        self.set_cube(load_matrix)
