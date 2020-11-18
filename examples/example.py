from rubiks_cube import rubiks_cube

# Create new cube object
cube = rubiks_cube.Cube()

# Prints the state of the cube
cube.print_cube()

# Turns the right face of the cube clockwise
cube.turn_face("R")
# Prints the state of the cube
cube.print_cube()

# Turns the right face of the cube counterclockwise
cube.turn_face("R", 1)
# Prints the state of the cube (Should be the same as a new cube)
cube.print_cube()

# Turns the right face of the cube twice
cube.turn_face("R", 2)
# Prints the state of the cube
cube.print_cube()


# Create new cube object
cube = rubiks_cube.Cube()

# Example of scramble
cube.scramble_cube("R B R2 F U' L2 D L' U2 R' D' F2 L F' D2 B2 U B'")
cube.print_cube()

# Example of scramble generation
scramble = rubiks_cube.scramble_generator(18)
print(scramble)

# Count number of colors in the correct place
print(cube.n_colors_in_place())

# Count number of pieces in the correct place
print(cube.n_pieces_in_place())

# Count number of pieces in the correct place and also oriented
print(cube.n_oriented_pieces_in_place())
