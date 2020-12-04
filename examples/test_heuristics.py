from solvers.four_phase import four_phase
from rubiks_cube import rubiks_cube

scramble = "R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'"
cube = rubiks_cube.Cube()
print(scramble)
cube.scramble(scramble)
print(four_phase(cube))
