from solvers.cfop import cross, assert_cross_solved, f2l, first_pair, second_pair, third_pair, fourth_pair, \
    assert_first_pair, assert_second_pair, assert_third_pair, assert_fourth_pair
from rubiks_cube.rubiks_cube import Cube
from utils import scramble_generator


# cube = Cube()
# scramble = "D' B2 L D L' R U B U2 B' F U F' U F2 U2 R'"
# cube.scramble(scramble)
# cross_moves, new_cube = cross(cube)
# print("cross moves", cross_moves)
# f2l_moves, new_cube = f2l(new_cube)
# print("f2l moves", f2l_moves)
# print("f2l", assert_fourth_pair(new_cube))
# new_cube.print()
# print(new_cube.get_pieces())

k = 0
for i in range(1000):
    cube = Cube()
    scramble = scramble_generator(20)
    cube.scramble(scramble)
    cross_solution, new_cube = cross(cube)
    f2l_moves, new_cube = f2l(new_cube)
    if not assert_fourth_pair(new_cube):
        print("embaralhamento", scramble)
        print("cruz:", cross_solution)
        print("f2l:", f2l_moves)
        new_cube.print()
        k += 1
print(k)
