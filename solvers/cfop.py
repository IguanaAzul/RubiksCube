from rubiks_cube import rubiks_cube


def cross(cube):
    cube = cube.copy()
    # wr, wb, wo, wg
    color_matrix = cube.get_matrix().copy()
    return cube
