from solvers.cfop import cfop
from rubiks_cube.rubiks_cube import Cube
from utils import fix_scramble, scramble_generator
import numpy as np


n_moves = list()
scrambles = list()
for i in range(10000):
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
