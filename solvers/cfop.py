from rubiks_cube import rubiks_cube
import numpy as np
from utils import edges, corners, \
    U, F, R, D, B, L, \
    UF, UR, UB, UL, FL, FR, RB, BL, DF, DR, DB, DL, \
    UFL, UFR, UBR, UBL, DFL, DFR, DBR, DBL


def assert_cross_solved(cube):
    pieces = cube.get_pieces()
    if (edges[int(np.where(pieces[:, 0] == DF)[0])] == DF and
            int(pieces[np.where(pieces[:, 0] == DF)][0, 1]) == 0 and
            edges[int(np.where(pieces[:, 0] == DR)[0])] == DR and
            int(pieces[np.where(pieces[:, 0] == DR)][0, 1]) == 0 and
            edges[int(np.where(pieces[:, 0] == DB)[0])] == DB and
            int(pieces[np.where(pieces[:, 0] == DB)][0, 1]) == 0 and
            edges[int(np.where(pieces[:, 0] == DL)[0])] == DL and
            int(pieces[np.where(pieces[:, 0] == DL)][0, 1]) == 0):
        return True
    else:
        return False


def cross(cube):
    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_matrix().copy(), cube.get_pieces().copy()))
    cross_solution = list()
    # find piece DF
    DF_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == DF)[0])]
    DF_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DF)][0, 1])
    if DF_position == UF and DF_orientation == 0:
        move = "F2"
    elif DF_position == UR and DF_orientation == 0:
        move = "U F2"
    elif DF_position == UB and DF_orientation == 0:
        move = "U2 F2"
    elif DF_position == UL and DF_orientation == 0:
        move = "U' F2"
    elif DF_position == UF and DF_orientation == 1:
        move = "U' R' F"
    elif DF_position == UR and DF_orientation == 1:
        move = "R' F"
    elif DF_position == UB and DF_orientation == 1:
        move = "U R' F"
    elif DF_position == UL and DF_orientation == 1:
        move = "L F'"
    elif DF_position == DR and DF_orientation == 0:
        move = "D'"
    elif DF_position == DB and DF_orientation == 0:
        move = "D2"
    elif DF_position == DL and DF_orientation == 0:
        move = "D"
    elif DF_position == DF and DF_orientation == 1:
        move = "F' R' D'"
    elif DF_position == DR and DF_orientation == 1:
        move = "R F"
    elif DF_position == DB and DF_orientation == 1:
        move = "D' R F"
    elif DF_position == DL and DF_orientation == 1:
        move = "L' F'"
    elif DF_position == FL and DF_orientation == 0:
        move = "L D"
    elif DF_position == FR and DF_orientation == 0:
        move = "R' D'"
    elif DF_position == RB and DF_orientation == 0:
        move = "R D'"
    elif DF_position == BL and DF_orientation == 0:
        move = "L' D"
    elif DF_position == FL and DF_orientation == 1:
        move = "F'"
    elif DF_position == FR and DF_orientation == 1:
        move = "F"
    elif DF_position == RB and DF_orientation == 1:
        move = "R2 F"
    elif DF_position == BL and DF_orientation == 1:
        move = "L2 F'"
    else:
        move = ""
    # Place piece DF
    cross_solution.append(move)
    new_cube.scramble(move)

    # find piece DR
    DR_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == DR)[0])]
    DR_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DR)][0, 1])
    if DR_position == UF and DR_orientation == 0:
        move = "U' R2"
    elif DR_position == UR and DR_orientation == 0:
        move = "R2"
    elif DR_position == UB and DR_orientation == 0:
        move = "U R2"
    elif DR_position == UL and DR_orientation == 0:
        move = "U2 R2"
    elif DR_position == UF and DR_orientation == 1:
        move = "F R' F'"
    elif DR_position == UR and DR_orientation == 1:
        move = "U' B' R"
    elif DR_position == UB and DR_orientation == 1:
        move = "B' R"
    elif DR_position == UL and DR_orientation == 1:
        move = "U B' R"
    elif DR_position == DB and DR_orientation == 0:
        move = "B2 U R2"
    elif DR_position == DL and DR_orientation == 0:
        move = "L2 U2 R2"
    elif DR_position == DR and DR_orientation == 1:
        move = "R' D B' D'"
    elif DR_position == DB and DR_orientation == 1:
        move = "B R"
    elif DR_position == DL and DR_orientation == 1:
        move = "L' D' F' D"
    elif DR_position == FL and DR_orientation == 0:
        move = "D2 L D2"
    elif DR_position == FR and DR_orientation == 0:
        move = "R'"
    elif DR_position == RB and DR_orientation == 0:
        move = "R"
    elif DR_position == BL and DR_orientation == 0:
        move = "B2 R"
    elif DR_position == FL and DR_orientation == 1:
        move = "D' F' D"
    elif DR_position == FR and DR_orientation == 1:
        move = "D' F D"
    elif DR_position == RB and DR_orientation == 1:
        move = "D B' D'"
    elif DR_position == BL and DR_orientation == 1:
        move = "D B D'"
    else:
        move = ""
    # Place piece DR
    cross_solution.append(move)
    new_cube.scramble(move)

    # find piece DB
    DB_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == DB)[0])]
    DB_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DB)][0, 1])
    if DB_position == UF and DB_orientation == 0:
        move = "U2 B2"
    elif DB_position == UR and DB_orientation == 0:
        move = "U' B2"
    elif DB_position == UB and DB_orientation == 0:
        move = "B2"
    elif DB_position == UL and DB_orientation == 0:
        move = "U B2"
    elif DB_position == UF and DB_orientation == 1:
        move = "U L' B"
    elif DB_position == UR and DB_orientation == 1:
        move = "R B' R'"
    elif DB_position == UB and DB_orientation == 1:
        move = "U' L' B"
    elif DB_position == UL and DB_orientation == 1:
        move = "L' B"
    elif DB_position == DL and DB_orientation == 0:
        move = "L2 U B2"
    elif DB_position == DB and DB_orientation == 1:
        move = "B' D L' D'"
    elif DB_position == DL and DB_orientation == 1:
        move = "L B"
    elif DB_position == FL and DB_orientation == 0:
        move = "D L D'"
    elif DB_position == FR and DB_orientation == 0:
        move = "D' R' D"
    elif DB_position == RB and DB_orientation == 0:
        move = "D' R D"
    elif DB_position == BL and DB_orientation == 0:
        move = "D L' D'"
    elif DB_position == FL and DB_orientation == 1:
        move = "L2 B"
    elif DB_position == FR and DB_orientation == 1:
        move = "R2 B' R2"
    elif DB_position == RB and DB_orientation == 1:
        move = "B'"
    elif DB_position == BL and DB_orientation == 1:
        move = "B"
    else:
        move = ""
    # Place piece DB
    cross_solution.append(move)
    new_cube.scramble(move)

    # find piece DL
    DL_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == DL)[0])]
    DL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DL)][0, 1])
    if DL_position == UF and DL_orientation == 0:
        move = "U L2"
    elif DL_position == UR and DL_orientation == 0:
        move = "U2 L2"
    elif DL_position == UB and DL_orientation == 0:
        move = "U' L2"
    elif DL_position == UL and DL_orientation == 0:
        move = "L2"
    elif DL_position == UF and DL_orientation == 1:
        move = "F' L F"
    elif DL_position == UR and DL_orientation == 1:
        move = "U F' L F"
    elif DL_position == UB and DL_orientation == 1:
        move = "B L' B'"
    elif DL_position == UL and DL_orientation == 1:
        move = "U' F' L F"
    elif DL_position == DL and DL_orientation == 1:
        move = "L' D F' D'"
    elif DL_position == FL and DL_orientation == 0:
        move = "L"
    elif DL_position == FR and DL_orientation == 0:
        move = "D2 R' D2"
    elif DL_position == RB and DL_orientation == 0:
        move = "D2 R D2"
    elif DL_position == BL and DL_orientation == 0:
        move = "L'"
    elif DL_position == FL and DL_orientation == 1:
        move = "D F' D'"
    elif DL_position == FR and DL_orientation == 1:
        move = "D F D'"
    elif DL_position == RB and DL_orientation == 1:
        move = "D' B' D"
    elif DL_position == BL and DL_orientation == 1:
        move = "D' B D"
    else:
        move = ""
    # Place piece DL
    cross_solution.append(move)
    new_cube.scramble(move)

    return " . ".join(cross_solution), new_cube

def f2l(cube):
    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_matrix().copy(), cube.get_pieces().copy()))
    cross_solution = list()
    # find piece UFL
    UFL_position = corners[int(np.where(new_cube.get_pieces()[:, 0] == UFL)[0])]
    UFL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == UFL)][0, 1])
