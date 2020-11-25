from solvers.use_external_kociemba import external_kociemba
from rubiks_cube import rubiks_cube


cube = rubiks_cube.Cube()
scramble = "R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'"
cube.scramble("R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'")
print("Scrambled Cube:")
cube.print()
solution = external_kociemba(cube)
print("Solution: ", solution)
cube.scramble(solution)
print("Solved Cube:")
cube.print()