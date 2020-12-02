from rubiks_cube import rubiks_cube
import numpy as np
from utils import edges, corners, colors, edges_dict, fix_scramble, \
    U, F, R, D, B, L, \
    UF, UR, UB, UL, FL, FR, BR, BL, DF, DR, DB, DL, \
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


def assert_first_pair(cube):
    pieces = cube.get_pieces()
    if (assert_cross_solved(cube) and
            edges[int(np.where(pieces[:, 0] == FL)[0])] == FL and
            corners[int(np.where(pieces[:, 0] == DFL)[0]) - 12] == DFL and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == FL)][0, 1]) == 0 and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == DFL)][0, 1]) == 0):
        return True
    else:
        return False


def assert_second_pair(cube):
    pieces = cube.get_pieces()
    if (assert_cross_solved(cube) and assert_first_pair(cube) and
            edges[int(np.where(pieces[:, 0] == FR)[0])] == FR and
            corners[int(np.where(pieces[:, 0] == DFR)[0]) - 12] == DFR and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == FR)][0, 1]) == 0 and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == DFR)][0, 1]) == 0):
        return True
    else:
        return False


def assert_third_pair(cube):
    pieces = cube.get_pieces()
    if (assert_cross_solved(cube) and assert_first_pair(cube) and assert_second_pair(cube) and
            edges[int(np.where(pieces[:, 0] == BR)[0])] == BR and
            corners[int(np.where(pieces[:, 0] == DBR)[0]) - 12] == DBR and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == BR)][0, 1]) == 0 and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == DBR)][0, 1]) == 0):
        return True
    else:
        return False


def assert_fourth_pair(cube):
    pieces = cube.get_pieces()
    if (assert_cross_solved(cube) and assert_first_pair(cube) and
            assert_second_pair(cube) and assert_third_pair(cube) and
            edges[int(np.where(pieces[:, 0] == BL)[0])] == BL and
            corners[int(np.where(pieces[:, 0] == DBL)[0]) - 12] == DBL and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == BL)][0, 1]) == 0 and
            int(cube.get_pieces()[np.where(cube.get_pieces()[:, 0] == DBL)][0, 1]) == 0):
        return True
    else:
        return False


def cross(cube):
    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))
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
    elif DF_position == BR and DF_orientation == 0:
        move = "R D'"
    elif DF_position == BL and DF_orientation == 0:
        move = "L' D"
    elif DF_position == FL and DF_orientation == 1:
        move = "F'"
    elif DF_position == FR and DF_orientation == 1:
        move = "F"
    elif DF_position == BR and DF_orientation == 1:
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
    elif DR_position == BR and DR_orientation == 0:
        move = "R"
    elif DR_position == BL and DR_orientation == 0:
        move = "B2 R"
    elif DR_position == FL and DR_orientation == 1:
        move = "D' F' D"
    elif DR_position == FR and DR_orientation == 1:
        move = "D' F D"
    elif DR_position == BR and DR_orientation == 1:
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
    elif DB_position == BR and DB_orientation == 0:
        move = "D' R D"
    elif DB_position == BL and DB_orientation == 0:
        move = "D L' D'"
    elif DB_position == FL and DB_orientation == 1:
        move = "L2 B"
    elif DB_position == FR and DB_orientation == 1:
        move = "R2 B' R2"
    elif DB_position == BR and DB_orientation == 1:
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
    case = ""
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
    elif DL_position == BR and DL_orientation == 0:
        move = "D2 R D2"
    elif DL_position == BL and DL_orientation == 0:
        move = "L'"
    elif DL_position == FL and DL_orientation == 1:
        move = "D F' D'"
    elif DL_position == FR and DL_orientation == 1:
        move = "D F D'"
    elif DL_position == BR and DL_orientation == 1:
        move = "D' B' D"
    elif DL_position == BL and DL_orientation == 1:
        move = "D' B D"
    else:
        move = ""
    # Place piece DL
    cross_solution.append(move)
    new_cube.scramble(move)

    return " ".join(cross_solution), new_cube


def first_pair(cube):
    if assert_first_pair(cube):
        return "", cube

    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))

    # find corner DFL
    DFL_position = corners[int(np.where(new_cube.get_pieces()[:, 0] == DFL)[0]) - len(edges)]

    # Move to position corner DFL above its spot (UFL)
    if DFL_position == UFR:
        pre_move_corner = "U"
    elif DFL_position == UBR:
        pre_move_corner = "U2"
    elif DFL_position == UBL:
        pre_move_corner = "U'"
    elif DFL_position == DFL:
        pre_move_corner = "L' U' L U"
    elif DFL_position == DFR:
        pre_move_corner = "R U R'"
    elif DFL_position == DBR:
        pre_move_corner = "R' U2 R"
    elif DFL_position == DBL:
        pre_move_corner = "B' U' B"
    else:
        pre_move_corner = ""

    new_cube.scramble(pre_move_corner)

    # find edge FL, move to be opposite to the corner (UR)
    FL_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == FL)[0])]
    if FL_position == UF:
        pre_move_edge = "L U' L'"
    elif FL_position == UB:
        pre_move_edge = "L U L'"
    elif FL_position == UL:
        pre_move_edge = "F' U2 F"
    elif FL_position == FL:
        pre_move_edge = "U L' U' L U'"
    elif FL_position == FR:
        pre_move_edge = "F' U' F"
    elif FL_position == BR:
        pre_move_edge = "R' U R U'"
    elif FL_position == BL:
        pre_move_edge = "L U2 L'"
    else:
        pre_move_edge = ""

    new_cube.scramble(pre_move_edge)
    FL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == FL)][0, 1])
    DFL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DFL)][0, 1])
    case = ""
    if DFL_orientation == 0 and FL_orientation == 0:
        case = "L' B' U2 B L"
    elif DFL_orientation == 1 and FL_orientation == 0:
        case = "F' U2 F L F' L' F"
    elif DFL_orientation == 2 and FL_orientation == 0:
        case = "L U' L2 U' L"
    elif DFL_orientation == 0 and FL_orientation == 1:
        case = "U F U2 F' U F U' F'"
    elif DFL_orientation == 1 and FL_orientation == 1:
        case = "F U F'"
    elif DFL_orientation == 2 and FL_orientation == 1:
        case = "L U L' F' L F L'"
    new_cube.scramble(case)

    return " ".join((pre_move_corner, pre_move_edge, case)), new_cube


def second_pair(cube):
    if assert_second_pair(cube):
        return "", cube
    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))

    # find corner DFR
    DFR_position = corners[int(np.where(new_cube.get_pieces()[:, 0] == DFR)[0]) - len(edges)]

    # Move to position corner DFR above its spot (UFR)
    if DFR_position == UFL:
        pre_move_corner = "U'"
    elif DFR_position == UBR:
        pre_move_corner = "U"
    elif DFR_position == UBL:
        pre_move_corner = "U2"
    elif DFR_position == DFR:
        pre_move_corner = "R U R' U'"
    elif DFR_position == DBR:
        pre_move_corner = "B U B'"
    elif DFR_position == DBL:
        pre_move_corner = "L U2 L'"
    else:
        pre_move_corner = ""

    new_cube.scramble(pre_move_corner)

    # find edge FR, move to be opposite to the corner (UB)
    FR_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == FR)[0])]
    if FR_position == UF:
        pre_move_edge = "R' U2 R"
    elif FR_position == UR:
        pre_move_edge = "R U2 R' U'"
    elif FR_position == UL:
        pre_move_edge = "R' U R"
    elif FR_position == FR:
        pre_move_edge = "U F' U' F U'"
    elif FR_position == BR:
        pre_move_edge = "R' U' R"
    elif FR_position == BL:
        pre_move_edge = "U' L U L'"
    else:
        pre_move_edge = ""

    new_cube.scramble(pre_move_edge)
    FR_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == FR)][0, 1])
    DFR_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DFR)][0, 1])
    case = ""
    if DFR_orientation == 0 and FR_orientation == 0:
        case = "U R U2 R' U R U' R'"
    elif DFR_orientation == 1 and FR_orientation == 0:
        case = "U' R U R' U2 R U' R'"
    elif DFR_orientation == 2 and FR_orientation == 0:
        case = "R U R'"
    elif DFR_orientation == 0 and FR_orientation == 1:
        case = "F' L' U2 L F"
    elif DFR_orientation == 1 and FR_orientation == 1:
        case = "R' U' R F' U' F"
    elif DFR_orientation == 2 and FR_orientation == 1:
        case = "R' U2 R F R' F' R"

    new_cube.scramble(case)

    return " ".join((pre_move_corner, pre_move_edge, case)), new_cube


def third_pair(cube):
    if assert_third_pair(cube):
        return "", cube

    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))

    # find corner DBR
    DBR_position = corners[int(np.where(new_cube.get_pieces()[:, 0] == DBR)[0]) - len(edges)]

    # Move to position corner DBR above its spot (UBR)
    if DBR_position == UFL:
        pre_move_corner = "U2"
    elif DBR_position == UFR:
        pre_move_corner = "U'"
    elif DBR_position == UBL:
        pre_move_corner = "U"
    elif DBR_position == DBR:
        pre_move_corner = "R' U R"
    elif DBR_position == DBL:
        pre_move_corner = "L U L'"
    else:
        pre_move_corner = ""

    new_cube.scramble(pre_move_corner)

    # find edge BR, move to be opposite to the corner (UL)
    BR_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == BR)[0])]
    if BR_position == UF:
        pre_move_edge = "B' U B"
    elif BR_position == UR:
        pre_move_edge = "B' U2 B"
    elif BR_position == UB:
        pre_move_edge = "U' B U' B' U"
    elif BR_position == BR:
        pre_move_edge = "U R' U' R U'"
    elif BR_position == BL:
        pre_move_edge = "B' U' B"
    else:
        pre_move_edge = ""

    new_cube.scramble(pre_move_edge)
    BR_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == BR)][0, 1])
    DBR_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DBR)][0, 1])
    if DBR_orientation == 0 and BR_orientation == 0:
        case = "R' F' U2 F R"
    elif DBR_orientation == 1 and BR_orientation == 0:
        case = "B' U2 B U' R' U R"
    elif DBR_orientation == 2 and BR_orientation == 0:
        case = "B' U' B R' U' R"
    elif DBR_orientation == 0 and BR_orientation == 1:
        case = "U B U2 B' U B U' B'"
    elif DBR_orientation == 1 and BR_orientation == 1:
        case = "B U B'"
    elif DBR_orientation == 2 and BR_orientation == 1:
        case = "U' B U B' U B' R B R'"

    new_cube.scramble(case)

    return " ".join((pre_move_corner, pre_move_edge, case)), new_cube


def fourth_pair(cube):
    if assert_fourth_pair(cube):
        return "", cube

    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))

    # find corner DBL
    DBL_position = corners[int(np.where(new_cube.get_pieces()[:, 0] == DBL)[0]) - len(edges)]

    # Move to position corner DBL above its spot (UBL)
    if DBL_position == UFL:
        pre_move_corner = "U"
    elif DBL_position == UFR:
        pre_move_corner = "U2"
    elif DBL_position == UBR:
        pre_move_corner = "U'"
    elif DBL_position == DBL:
        pre_move_corner = "L U' L'"
    else:
        pre_move_corner = ""

    new_cube.scramble(pre_move_corner)

    # find edge BL, move to be opposite to the corner (UF)
    BL_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == BL)[0])]
    if BL_position == UL:
        pre_move_edge = "L U2 L' U'"
    elif BL_position == UR:
        pre_move_edge = "U B' U B U'"
    elif BL_position == UB:
        pre_move_edge = "U B' U2 B U'"
    elif BL_position == BL:
        pre_move_edge = "U B' U' B U'"
    else:
        pre_move_edge = ""

    new_cube.scramble(pre_move_edge)
    BL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == BL)][0, 1])
    DBL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == DBL)][0, 1])
    case = ""
    if DBL_orientation == 0 and BL_orientation == 0:
        case = "U L U2 L' U L U' L'"
    elif DBL_orientation == 1 and BL_orientation == 0:
        case = "U' L U L' U2 L U' L'"
    elif DBL_orientation == 2 and BL_orientation == 0:
        case = "L U L'"
    elif DBL_orientation == 0 and BL_orientation == 1:
        case = "B' R' U2 R B"
    elif DBL_orientation == 1 and BL_orientation == 1:
        case = "U' L U' L' U B' U' B"
    elif DBL_orientation == 2 and BL_orientation == 1:
        case = "U B' U2 B U2 B' U B"

    new_cube.scramble(case)

    return " ".join((pre_move_corner, pre_move_edge, case)), new_cube


def f2l(cube):
    first_pair_moves, new_cube = first_pair(cube)
    second_pair_moves, new_cube = second_pair(new_cube)
    third_pair_moves, new_cube = third_pair(new_cube)
    fourth_pair_moves, new_cube = fourth_pair(new_cube)
    return " ".join((first_pair_moves, second_pair_moves, third_pair_moves, fourth_pair_moves)), new_cube


def assert_first_look_oll(cube):
    pieces = cube.get_pieces()
    if (assert_fourth_pair(cube) and
            int(pieces[np.where(pieces[:, 0] == UF)][0, 1]) == 0 and
            int(pieces[np.where(pieces[:, 0] == UR)][0, 1]) == 0 and
            int(pieces[np.where(pieces[:, 0] == UB)][0, 1]) == 0 and
            int(pieces[np.where(pieces[:, 0] == UL)][0, 1]) == 0):
        return True
    else:
        return False


def assert_oll(cube):
    pieces = cube.get_pieces()
    if (assert_fourth_pair(cube) and assert_first_look_oll(cube) and
            int(pieces[np.where(pieces[:, 0] == UBL)][0, 1]) == 0 and
            int(pieces[np.where(pieces[:, 0] == UBR)][0, 1]) == 0 and
            int(pieces[np.where(pieces[:, 0] == UFL)][0, 1]) == 0 and
            int(pieces[np.where(pieces[:, 0] == UFR)][0, 1]) == 0):
        return True
    else:
        return False


def first_look_oll(cube):
    if assert_first_look_oll(cube):
        return "", cube

    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))

    pieces = new_cube.get_pieces()

    if pieces[0][1] == 0:
        if pieces[1][1] == 0:
            if pieces[2][1] == 1:
                # if two first edges are oriented, but the third is not, then is a L case starting with U2
                case = "U2 F U R U' R' F'"
        else:
            if pieces[2][1] == 0:
                # if first and third are oriented, then is a line case starting with U
                case = "U F R U R' U' F'"
            else:
                # if first and fourth are oriented, then is a L case starting with U
                case = "U F U R U' R' F'"
    else:
        if pieces[1][1] == 0:
            if pieces[2][1] == 0:
                # if second and third are oriented, then is a L case starting with U'
                case = "U' F U R U' R' F'"
            else:
                # if second and fourth are oriented, then is a line case
                case = "F R U R' U' F'"
        else:
            if pieces[2][1] == 0:
                # if third and fourth are oriented, then is a L case
                case = "F U R U' R' F'"
            else:
                # if none are oriented, then is a dot case
                case = "R U2 R2 F R F' U2 R' F R F'"

    new_cube.scramble(case)
    return case, new_cube


def second_look_oll(cube):
    if assert_oll(cube):
        return "", cube

    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix().copy(), cube.get_pieces().copy()))

    pieces = new_cube.get_pieces()

    pieces_orientation_array = [i if i == 0 else 1
                                for i in [pieces[12][1], pieces[13][1], pieces[14][1], pieces[15][1]]]

    if "0 1 1 1" in " ".join(str(i) for i in (pieces_orientation_array * 2)):
        # sune or antisune, let's find the right orientation
        if pieces_orientation_array == [0, 1, 1, 1]:
            if pieces[13][1] == 1:
                setup = ""
                case = "sune"
            else:
                setup = "U2"
                case = "antisune"
        elif pieces_orientation_array == [1, 0, 1, 1]:
            if pieces[12][1] == 2:
                setup = "U"
                case = "sune"
            else:
                setup = "U'"
                case = "antisune"
        elif pieces_orientation_array == [1, 1, 0, 1]:
            if pieces[12][1] == 2:
                setup = "U2"
                case = "sune"
            else:
                setup = ""
                case = "antisune"
        else:
            if pieces[12][1] == 2:
                setup = "U'"
                case = "sune"
            else:
                setup = "U"
                case = "antisune"

        if case == "sune":
            case = setup + " R U R' U R U2 R'"
        else:
            case = setup + " R U2 R' U' R U' R'"

    elif "0 0 1 1" in " ".join(str(i) for i in (pieces_orientation_array * 2)):
        # T or superman, let's find the right orientation
        if pieces_orientation_array == [0, 0, 1, 1]:
            if pieces[14][1] == 2:
                setup = "U'"
                case = "T"
            else:
                setup = ""
                case = "superman"
        elif pieces_orientation_array == [1, 0, 0, 1]:
            if pieces[12][1] == 1:
                setup = ""
                case = "T"
            else:
                setup = "U"
                case = "superman"
        elif pieces_orientation_array == [1, 1, 0, 0]:
            if pieces[12][1] == 2:
                setup = "U"
                case = "T"
            else:
                setup = "U2"
                case = "superman"
        else:
            if pieces[13][1] == 1:
                setup = "U2"
                case = "T"
            else:
                setup = "U'"
                case = "superman"

        if case == "T":
            case = setup + " L F R' F' L' F R F'"
        else:
            case = setup + " R2 D' R U2 R' D R U2 R"
    elif "0 1 0 1" in " ".join(str(i) for i in (pieces_orientation_array * 2)):
        # L, let's find the right orientation
        if pieces_orientation_array == [0, 1, 0, 1]:
            if pieces[13][1] == 2:
                setup = "U'"
            else:
                setup = "U"
        else:
            if pieces[12][1] == 2:
                setup = ""
            else:
                setup = "U2"
        case = setup + " R' F' L' F R F' L F"

    else:
        # cross, let's find the right orientation
        pieces_orientation_array = [pieces[12][1], pieces[13][1], pieces[14][1], pieces[15][1]]
        if pieces_orientation_array == [2, 2, 2, 2]:
            setup = ""
            case = "doublesune"
        elif pieces_orientation_array == [1, 1, 1, 1]:
            setup = "U"
            case = "doublesune"
        elif pieces_orientation_array == [2, 1, 1, 2]:
            setup = ""
            case = "pi"
        elif pieces_orientation_array == [1, 1, 2, 2]:
            setup = "U"
            case = "pi"
        elif pieces_orientation_array == [1, 2, 2, 1]:
            setup = "U2"
            case = "pi"
        else:
            setup = "U'"
            case = "pi"

        if case == "doublesune":
            case = setup + " R U R' U R U' R' U R U2 R'"
        else:
            case = setup + " R U2 R2 U' R2 U' R2 U2 R"

    new_cube.scramble(case)
    return case, new_cube


#     BL_orientation = int(new_cube.get_pieces()[np.where(new_cube.get_pieces()[:, 0] == BL)][0, 1])
#     DBR_position = corners[int(np.where(new_cube.get_pieces()[:, 0] == DBR)[0]) - len(edges)]
#     UD_position = edges[int(np.where(new_cube.get_pieces()[:, 0] == UD)[0])]
def oll(cube):
    first_look, new_cube = first_look_oll(cube)
    second_look, new_cube = second_look_oll(new_cube)
    return " ".join((first_look, second_look)), new_cube

def assert_pll_corners(cube):
    colors = cube.get_color_matrix()
    return ((colors[1, 8] == colors[1, 7]) and
            (colors[2, 5] == colors[2, 8]) and
            (colors[4, 5] == colors[4, 6]) and
            (colors[5, 7] == colors[5, 6]))

def pll(cube):
    pll_a = "R' F R' B2 R F' R' B2 R2"
    pll_y = "F2 D R2 U R2 D' R' U' R F2 R' U R"
    look_1 = ""
    new_cube = rubiks_cube.Cube()
    new_cube.set_cube((cube.get_color_matrix(), cube.get_pieces()))
    color_matrix = new_cube.get_color_matrix()
    post_look_1 = ""
    if not assert_pll_corners(new_cube):
        if color_matrix[1, 8] == color_matrix[1, 7]:
            look_1 += "U2 " + pll_a
        elif color_matrix[2, 5] == color_matrix[2, 8]:
            look_1 += "U' " + pll_a
        elif color_matrix[4, 5] == color_matrix[4, 6]:
            look_1 += "" + pll_a
        elif color_matrix[5, 7] == color_matrix[5, 6]:
            look_1 += "U " + pll_a
        else:
            look_1 += pll_y

    new_cube.scramble(look_1)

    if color_matrix[1, 8] == colors[2]:
        post_look_1 += " U'"
    elif color_matrix[1, 8] == colors[4]:
        post_look_1 += " U2"
    elif color_matrix[1, 8] == colors[5]:
        post_look_1 += " U"

    new_cube.scramble(post_look_1)

    pll_ua = "R2 U' R' U' R U R U R U' R"
    pll_ub = "R' U R' U' R' U' R' U R U R2"
    pll_h = "R2 U2 R U2 R2 U2 R2 U2 R U2 R2"
    pll_z = "R2 U' R2 U R2 B2 R2 U B2 U' R2 B2"

    facelets = {0: (1, 3), 1: (2, 4), 2: (4, 1), 3: (5, 2)}
    cases = {"uas": [(0, 2, 3, 1), (2, 1, 3, 0), (1, 3, 2, 0), (1, 2, 0, 3)],
             "ubs": [(0, 3, 1, 2), (3, 1, 0, 2), (3, 0, 2, 1), (2, 0, 1, 3)],
             "zs": [(1, 0, 3, 2), (3, 2, 1, 0)]}
    pre_move = ""
    look_2 = ""
    if not new_cube.is_solved():
        pieces = new_cube.get_pieces()
        top_edges = pieces[:4, 0]
        case = tuple([edges_dict[edge] for edge in top_edges])
        if case in cases["uas"]:
            if case == cases["uas"][1]:
                pre_move = "U"
            elif case == cases["uas"][2]:
                pre_move = "U2"
            elif case == cases["uas"][3]:
                pre_move = "U'"
            look_2 = pll_ua
        elif case in cases["ubs"]:
            if case == cases["ubs"][1]:
                pre_move = "U"
            elif case == cases["ubs"][2]:
                pre_move = "U2"
            elif case == cases["ubs"][3]:
                pre_move = "U'"
            look_2 = pll_ub
        elif case in cases["zs"]:
            if case == cases["zs"][1]:
                pre_move = "U'"
            look_2 = pll_z
        else:
            look_2 = pll_h
    post_move = ""
    if pre_move == "U":
        post_move = "U'"
    elif pre_move == "U'":
        post_move = "U"
    else:
        post_move = pre_move

    look_2 = " ".join((pre_move, look_2, post_move))
    new_cube.scramble(look_2)
    return " ".join((look_1, post_look_1, look_2)), new_cube


def cfop(cube):
    cross_moves, new_cube = cross(cube)
    f2l_moves, new_cube = f2l(new_cube)
    oll_moves, new_cube = oll(new_cube)
    pll_moves, new_cube = pll(new_cube)
    return fix_scramble(" ".join((cross_moves, f2l_moves, oll_moves, pll_moves))), new_cube
