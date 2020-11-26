from solvers.two_phase import phase1
from rubiks_cube import rubiks_cube


cube = rubiks_cube.Cube()
cube.scramble("R U R' U'")

print(phase1(cube))

