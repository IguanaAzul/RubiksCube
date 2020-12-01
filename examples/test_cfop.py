from solvers.cfop import cross, assert_cross_solved, f2l, first_pair, second_pair, third_pair, fourth_pair, \
    assert_first_pair, assert_second_pair, assert_third_pair, assert_fourth_pair, assert_first_look_oll, assert_oll, oll
from rubiks_cube.rubiks_cube import Cube
from utils import scramble_generator


cube = Cube()
scramble = "D B' U L' B' F2 D L2 R U' R2 D F R2 B2 R' D"
print("Scramble: ", scramble)
cube.scramble(scramble)
cross_moves, new_cube = cross(cube)
f2l_moves, new_cube = f2l(new_cube)
oll, new_cube = oll(new_cube)
print("cross moves", cross_moves)
print("f2l moves", f2l_moves)
print("oll moves", oll)
print("oll worked: ", assert_oll(new_cube))
new_cube.print()
print(new_cube.get_pieces())
