from solvers.cfop import cfop
from rubiks_cube.rubiks_cube import Cube
from utils import scramble_generator
import numpy as np


# Create new cube object
cube = Cube()
# Example of scramble
cube.scramble("R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'")
cube.print()
solution, new_cube = cfop(cube)
new_cube.print()

n_moves = list()
scrambles = list()
for i in range(1000):
    cube = Cube()
    scramble = scramble_generator(20)
    cube.scramble(scramble)
    solution, new_cube = cfop(cube)
    n_moves.append(len(solution.split()))
    scrambles.append(scramble)
print(np.array(n_moves).mean())
print(np.array(n_moves).std())
print(np.array(n_moves).min())
print(scrambles[np.array(n_moves).argmin()])
print(np.array(n_moves).max())
