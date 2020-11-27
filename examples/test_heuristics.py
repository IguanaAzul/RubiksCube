from solvers.two_phase import ida_star
from rubiks_cube import rubiks_cube
import numpy as np
import time

scramble = "R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'".split(" ")
for i in range(len(scramble)):
    cube = rubiks_cube.Cube()
    t0 = time.time()
    s = " ".join(scramble[:i])
    print(s)
    cube.scramble(s)
    print(ida_star(cube))
    t = time.time()
    print(t-t0)
