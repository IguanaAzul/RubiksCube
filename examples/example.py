from rubiks_cube import rubiks_cube
from utils import scramble_generator


# Create new cube object
cube = rubiks_cube.Cube()
# Prints the state of the cube
cube.print()
# Example of scramble generation
scramble = scramble_generator(18)
print(scramble)
# Example of scramble
cube.scramble("R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'")
cube.print()