from solvers.cfop import cross, assert_cross_solved
from rubiks_cube.rubiks_cube import Cube
from utils import scramble_generator

# cube = Cube()
# scramble = "F R B R2 D2 F2 D2 B' R2 U B R' L2 U L'"
# cube.scramble(scramble)
# cross_solution, new_cube = cross(cube)
# if not assert_cross_solved(new_cube):
#     print("embaralhamento", scramble)
#     print("cruz:", cross_solution)
#     print("scrambled:")
#     cube.print()
#     print("cross:")
#     new_cube.print()

k = 0
for i in range(10000):
    cube = Cube()
    scramble = scramble_generator(20)
    cube.scramble(scramble)
    cross_solution, new_cube = cross(cube)
    if not assert_cross_solved(new_cube):
        print("embaralhamento", scramble)
        print("cruz:", cross_solution)
        print("scrambled:")
        cube.print()
        print("cross:")
        new_cube.print()
        k += 1
print(k)
