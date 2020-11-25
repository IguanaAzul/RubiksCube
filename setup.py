from setuptools import setup

setup(
    name='rubiks_cube',
    version='1.0.6',
    description='A Rubiks Cube Package for Python',
    url='https://github.com/IguanaAzul/RubiksCube.git',
    author='Ramon Griffo',
    author_email='ramon.griffo98@gmail.com',
    license='MIT License',
    packages=['rubiks_cube'],
    install_requires=['numpy', 'kociemba'],
    long_description='This library implements a 3x3x3 rubiks cube for general purpose in python.\n'
                     'It provides Rubiks Cube implemented using numpy arrays with a function to turn the cube faces, '
                     'as you would turn a real cube, '
                     'and a function to apply a scramble as a string in the official WCA format.\n'
                     'https://github.com/IguanaAzul/RubiksCube.git'
)
