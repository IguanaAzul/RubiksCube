import numpy as np
from itertools import groupby

U, F, R, D, B, L = ("w", "g", "r", "y", "b", "o")
colors = [U, F, R, D, B, L]
UF, UR, UB, UL, FL, FR, BR, BL, DF, DR, DB, DL = (U + F, U + R, U + B, U + L, F + L, F + R, B + R, B + L, D + F, D + R, D + B, D + L)

edges = [UF, UR, UB, UL, FL, FR, BR, BL, DF, DR, DB, DL]

UFL, UFR, UBR, UBL, DFL, DFR, DBR, DBL = (U+F+L, U+F+R, U+B+R, U+B+L, D+F+L, D+F+R, D+B+R, D+B+L)
corners = UFL, UFR, UBR, UBL, DFL, DFR, DBR, DBL

matrix_ref = np.array([[U, U, U, U, U, U, U, U, U], [F, F, F, F, F, F, F, F, F],
                       [R, R, R, R, R, R, R, R, R], [D, D, D, D, D, D, D, D, D],
                       [B, B, B, B, B, B, B, B, B], [L, L, L, L, L, L, L, L, L]])

pieces_ref = np.array([[UF, 0], [UR, 0], [UB, 0], [UL, 0],
                       [FL, 0], [FR, 0], [BR, 0], [BL, 0],
                       [DF, 0], [DR, 0], [DB, 0], [DL, 0],
                       [UFL, 0], [UFR, 0], [UBR, 0], [UBL, 0],
                       [DFL, 0], [DFR, 0], [DBR, 0], [DBL, 0]], dtype=object)

bin_to_color = {(0, 0, 0): U, (0, 1, 0): F, (0, 1, 1): R, (1, 0, 0): D, (1, 0, 1): B, (1, 1, 0): L}

int_face = {"U": 0, "F": 1, "R": 2, "D": 3, "B": 4, "L": 5, 0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

notation = {"U": [0, 0], "F": [1, 0], "R": [2, 0], "D": [3, 0], "B": [4, 0], "L": [5, 0],
            "U\'": [0, 1], "F\'": [1, 1], "R\'": [2, 1], "D\'": [3, 1], "B\'": [4, 1], "L\'": [5, 1],
            "U2": [0, 2], "F2": [1, 2], "R2": [2, 2], "D2": [3, 2], "B2": [4, 2], "L2": [5, 2]}

int_to_turn = {1: "U", 2: "F", 3: "R", 4: "D", 5: "B", 6: "L",
               7: "U\'", 8: "F\'", 9: "R\'", 10: "D\'", 11: "B\'", 12: "L\'",
               13: "U2", 14: "F2", 15: "R2", 16: "D2", 17: "B2", 18: "L2"}


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
    scramble = np.random.randint(6, size=length) + 1
    scramble = [k for k, g in groupby(scramble) if k != 0]
    for idx in range(len(scramble)):
        odds = np.random.randint(0, 300)
        if odds < 100:
            scramble[idx] += 6
        elif odds < 200:
            scramble[idx] += 12
    return " ".join([int_to_turn[i] for i in scramble])
