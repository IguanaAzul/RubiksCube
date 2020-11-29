from solvers.cfop import cross, assert_cross_solved, f2l, first_pair, second_pair, third_pair, fourth_pair, \
    assert_first_pair, assert_second_pair, assert_third_pair, assert_fourth_pair, assert_first_look_oll, assert_oll, oll
from rubiks_cube.rubiks_cube import Cube
from utils import scramble_generator


cube = Cube()
# # scramble = "R U2 R' U' R U' R' U" # sune
# # scramble = "R U R' U R U2 R'" # anti-sune
# scramble = "F' L' F R' F' L F R"
# cube.scramble(scramble)
# cube.print()
# print(assert_first_look_oll(cube))
# print(assert_oll(cube))
# oll, cube = oll(cube)
# cube.print()
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
    oll_moves, new_cube = oll(new_cube)
    if assert_oll(new_cube):
        print("embaralhamento", scramble)
        print("cruz:", cross_solution)
        print("f2l:", f2l_moves)
        print("oll:", oll_moves)
        new_cube.print()
        k += 1
print(k)
