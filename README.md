# RubiksCube
This library implements a 3x3x3 rubiks cube for general purpose in python.

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

Future implementations:
- NxNxN cubes
- Algorithms to solve the cubes
- Fix scramble generator (It sometimes generates scrambles with less movements than requested)

The file ./examples/example.py contains example usages of the library
