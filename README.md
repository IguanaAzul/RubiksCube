# RubiksCube
This library implements a 3x3x3 rubiks cube for general purpose in python.

    pip install rubiks_cube


It provides:

- A Rubiks Cube implemented using numpy arrays
- A function to turn the cube faces, as you'd turn a real cube
- A function to apply a scramble as a string in the official WCA format
- Functions to count how many colors or pieces are in the correct place

The following notations apply:

| Symbol | Face  |
|--------|-------|
| U      | Up    |
| R      | Right |
| F      | Front |
| L      | Left  |
| D      | Down  |
| B      | Back  |

| Symbol | Color  |
|--------|--------|
| w      | White  |
| r      | Red    |
| g      | Green  |
| o      | Orange |
| y      | Yellow |
| b      | Blue   |

The color_matrix is indexed like this:


                             --------------------------
                             | [4, 8]  [4, 3]  [4, 7] |
                             | [4, 4]  [4, 0]  [4, 2] |
                             | [4, 5]  [4, 1]  [4, 6] |
    -----------------------------------------------------------------------------------------------------
    | [5, 8]  [5, 3]  [5, 7] | [0, 8]  [0, 3]  [0, 7] | [2, 8]  [2, 3]  [2, 7] | [3, 8]  [3, 3]  [3, 7] |
    | [5, 4]  [5, 0]  [5, 2] | [0, 4]  [0, 0]  [0, 2] | [2, 4]  [2, 0]  [2, 2] | [3, 4]  [3, 0]  [3, 2] |
    | [5, 5]  [5, 1]  [5, 6] | [0, 5]  [0, 1]  [0, 6] | [2, 5]  [2, 1]  [2, 6] | [3, 5]  [3, 1]  [3, 6] |
    -----------------------------------------------------------------------------------------------------
                             | [1, 8]  [1, 3]  [1, 7] |
                             | [1, 4]  [1, 0]  [1, 2] |
                             | [1, 5]  [1, 1]  [1, 6] |
                             --------------------------
By default filled like this:

            ---------
            | b b b |
            | b b b |
            | b b b |
    ---------------------------------
    | o o o | w w w | r r r | y y y |
    | o o o | w w w | r r r | y y y |
    | o o o | w w w | r r r | y y y |
    ---------------------------------
            | g g g |
            | g g g |
            | g g g |
            ---------

Future implementations:
- NxNxN cubes
- Algorithms to solve the cubes
- Fix scramble generator (It sometimes generates scrambles with less movements than requested)

The file ./examples/example.py contains example usages of the library

