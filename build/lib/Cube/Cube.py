import numpy as np
from itertools import groupby
import random

def swap3(a, b, c, way):
    if way:
        aux = c
        c = b
        b = a
        a = aux
        if way == 2:
            a, b, c = swap3(a, b, c, 1)
    else:
        aux = a
        a = b
        b = c
        c = aux
    return a, b, c

def swap4(a, b, c, d, way):
    if way:
        aux = d
        d = c
        c = b
        b = a
        a = aux
        if way == 2:
            a, b, c, d = swap4(a, b, c, d, 1)
    else:
        aux = a
        a = b
        b = c
        c = d
        d = aux
    return a, b, c, d

def scrambleGenerator(length):
        intToTurn = {1:'U', 2:'F', 3:'R', 4:'D', 5:'B', 6:'L', 
        7:'U\'', 8:'F\'', 9:'R\'', 10:'D\'', 11:'B\'', 12:'L\'', 
        13:'U2', 14:'F2', 15:'R2', 16:'D2', 17:'B2', 18:'L2'}
        scramble = np.random.randint(6, size=length) + 1
        scramble = [k for k,g in groupby(scramble) if k!=0]
        for idx in range(len(scramble)):
            odds = random.randint(0, 300)
            if odds<100:
                scramble[idx] += 6
            elif odds<200:
                scramble[idx] += 12
        return ' '.join([intToTurn[i] for i in scramble]) + '\n'

matrixRef = np.array([['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], 
                          ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], 
                          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']])
    
piecesRef = np.array([[1, 'w', 'g', None], [1, 'w', 'r', None], [1, 'w', 'b', None], [1, 'w', 'o', None], 
                    [1, 'g', 'o', None], [1, 'g', 'r', None], [1, 'r', 'b', None], [1, 'b', 'o', None], 
                    [1, 'y', 'g', None], [1, 'y', 'r', None], [1, 'y', 'b', None], [1, 'y', 'o', None],
                    [2, 'w', 'g', 'o'], [2, 'w', 'g', 'r'], [2, 'w', 'b', 'r'], [2, 'w', 'b', 'o'], 
                    [2, 'y', 'g', 'o'], [2, 'y', 'g', 'r'], [2, 'y', 'b', 'r'], [2, 'y', 'b', 'o']])

toInt = {'w':0, 'g':1, 'r':2, 'y':3, 'b':4, 'o':5, 
         0:0, 1:1, 2:2, 3:3, 4:4, 5:5}

toColor = {0:'w', 1:'g', 2:'r', 3:'y', 4:'b', 5:'o',
           'w':'w', 'g':'g', 'r':'r', 'y':'y', 'b':'b', 'o':'o'}

charFace = {0:'U', 1:'F', 2:'R', 3:'D', 4:'B', 5:'L',
            'U':'U', 'F':'F', 'R':'R', 'D':'D', 'B':'B', 'L':'L'}

intFace = {'U':0, 'F':1, 'R':2, 'D':3, 'B':4, 'L':5,
            0:0, 1:1, 2:2, 3:3, 4:4, 5:5}

notation = {'U':[0, 0], 'F':[1, 0], 'R':[2, 0], 'D':[3, 0], 'B':[4, 0], 'L':[5, 0],
            'U\'':[0, 1], 'F\'':[1, 1], 'R\'':[2, 1], 'D\'':[3, 1], 'B\'':[4, 1], 'L\'':[5, 1],
            'U2':[0, 2], 'F2':[1, 2], 'R2':[2, 2], 'D2':[3, 2], 'B2':[4, 2], 'L2':[5, 2]}

class Cube:
    def __init__(self):
        self.setCube()

    def setCube(self):
        self.matrixColors = matrixRef.copy()
        self.pieces = piecesRef.copy()

    def turnFace(self, face, way=0):
        turn = intFace[face]
        self.matrixColors[turn, 1], self.matrixColors[turn, 2], self.matrixColors[turn, 3], self.matrixColors[turn, 4] = swap4(self.matrixColors[turn, 1], 
        self.matrixColors[turn, 2], self.matrixColors[turn, 3], self.matrixColors[turn, 4], way)

        self.matrixColors[turn, 5], self.matrixColors[turn, 6], self.matrixColors[turn, 7], self.matrixColors[turn, 8] = swap4(self.matrixColors[turn, 5], 
        self.matrixColors[turn, 6], self.matrixColors[turn, 7], self.matrixColors[turn, 8], way)
        #UP
        if turn == 0:
            self.pieces[0], self.pieces[1], self.pieces[2], self.pieces[3] = swap4(self.pieces[0], self.pieces[1], 
                                                                               self.pieces[2], self.pieces[3], way)

            self.pieces[12], self.pieces[13], self.pieces[14], self.pieces[15] = swap4(self.pieces[12], self.pieces[13], 
                                                                                   self.pieces[14], self.pieces[15], way)

            self.matrixColors[1, 3], self.matrixColors[2, 4], self.matrixColors[4, 1], self.matrixColors[5, 2] = swap4(self.matrixColors[1, 3], 
            self.matrixColors[2, 4], self.matrixColors[4, 1], self.matrixColors[5, 2], way)

            self.matrixColors[1, 7], self.matrixColors[2, 8], self.matrixColors[4, 5], self.matrixColors[5, 6] = swap4(self.matrixColors[1, 7], 
            self.matrixColors[2, 8], self.matrixColors[4, 5], self.matrixColors[5, 6], way)

            self.matrixColors[1, 8], self.matrixColors[2, 5], self.matrixColors[4, 6], self.matrixColors[5, 7] = swap4(self.matrixColors[1, 8], 
            self.matrixColors[2, 5], self.matrixColors[4, 6], self.matrixColors[5, 7], way)
        #FRONT
        elif turn == 1:
            self.pieces[8], self.pieces[5], self.pieces[0], self.pieces[4] = swap4(self.pieces[8], self.pieces[5], 
                                                                               self.pieces[0], self.pieces[4], way)

            self.pieces[16], self.pieces[17], self.pieces[13], self.pieces[12] = swap4(self.pieces[16], self.pieces[17], 
                                                                                   self.pieces[13], self.pieces[12], way)

            self.matrixColors[3, 1], self.matrixColors[2, 1], self.matrixColors[0, 1], self.matrixColors[5, 1] = swap4(self.matrixColors[3, 1], 
            self.matrixColors[2, 1], self.matrixColors[0, 1], self.matrixColors[5, 1], way)

            self.matrixColors[3, 5], self.matrixColors[2, 5], self.matrixColors[0, 5], self.matrixColors[5, 5] = swap4(self.matrixColors[3, 5], 
            self.matrixColors[2, 5], self.matrixColors[0, 5], self.matrixColors[5, 5], way)

            self.matrixColors[3, 6], self.matrixColors[2, 6], self.matrixColors[0, 6], self.matrixColors[5, 6] = swap4(self.matrixColors[3, 6], 
            self.matrixColors[2, 6], self.matrixColors[0, 6], self.matrixColors[5, 6], way)
        #RIGHT
        elif turn == 2:
            self.pieces[1], self.pieces[5], self.pieces[9], self.pieces[6] = swap4(self.pieces[1], self.pieces[5], 
                                                                               self.pieces[9], self.pieces[6], way)

            self.pieces[17], self.pieces[18], self.pieces[14], self.pieces[13] = swap4(self.pieces[17], self.pieces[18], 
                                                                                   self.pieces[14], self.pieces[13], way)

            self.matrixColors[0, 2], self.matrixColors[1, 2], self.matrixColors[3, 4], self.matrixColors[4, 2] = swap4(self.matrixColors[0, 2], 
            self.matrixColors[1, 2], self.matrixColors[3, 4], self.matrixColors[4, 2], way)

            self.matrixColors[0, 6], self.matrixColors[1, 6], self.matrixColors[3, 8], self.matrixColors[4, 6] = swap4(self.matrixColors[0, 6], 
            self.matrixColors[1, 6], self.matrixColors[3, 8], self.matrixColors[4, 6], way)

            self.matrixColors[0, 7], self.matrixColors[1, 7], self.matrixColors[3, 5], self.matrixColors[4, 7] = swap4(self.matrixColors[0, 7], 
            self.matrixColors[1, 7], self.matrixColors[3, 5], self.matrixColors[4, 7], way)
        #DOWN
        elif turn == 3:
            self.pieces[11], self.pieces[10], self.pieces[9], self.pieces[8] = swap4(self.pieces[11], self.pieces[10], 
                                                                                 self.pieces[9], self.pieces[8], way)

            self.pieces[19], self.pieces[18], self.pieces[17], self.pieces[16] = swap4(self.pieces[19], self.pieces[18], 
                                                                                   self.pieces[17], self.pieces[16], way)

            self.matrixColors[1, 1], self.matrixColors[5, 4], self.matrixColors[4, 3], self.matrixColors[2, 2] = swap4(self.matrixColors[1, 1], 
            self.matrixColors[5, 4], self.matrixColors[4, 3], self.matrixColors[2, 2], way)

            self.matrixColors[5, 8], self.matrixColors[4, 7], self.matrixColors[2, 6], self.matrixColors[1, 5] = swap4(self.matrixColors[5, 8], 
            self.matrixColors[4, 7], self.matrixColors[2, 6], self.matrixColors[1, 5], way)

            self.matrixColors[5, 5], self.matrixColors[4, 8], self.matrixColors[2, 7], self.matrixColors[1, 6] = swap4(self.matrixColors[5, 5], 
            self.matrixColors[4, 8], self.matrixColors[2, 7], self.matrixColors[1, 6], way)
        #BACK
        elif turn == 4:
            self.pieces[2], self.pieces[6], self.pieces[10], self.pieces[7] = swap4(self.pieces[2], self.pieces[6], 
                                                                                self.pieces[10], self.pieces[7], way)

            self.pieces[14], self.pieces[15], self.pieces[18], self.pieces[19] = swap4(self.pieces[14], self.pieces[15], 
                                                                                   self.pieces[18], self.pieces[19], way)

            self.matrixColors[0, 3], self.matrixColors[2, 3], self.matrixColors[3, 3], self.matrixColors[5, 3] = swap4(self.matrixColors[0, 3], 
            self.matrixColors[2, 3], self.matrixColors[3, 3], self.matrixColors[5, 3], way)

            self.matrixColors[0, 8], self.matrixColors[2, 8], self.matrixColors[3, 8], self.matrixColors[5, 8] = swap4(self.matrixColors[0, 8], 
            self.matrixColors[2, 8], self.matrixColors[3, 8], self.matrixColors[5, 8], way)

            self.matrixColors[0, 7], self.matrixColors[2, 7], self.matrixColors[3, 7], self.matrixColors[5, 7] = swap4(self.matrixColors[0, 7], 
            self.matrixColors[2, 7], self.matrixColors[3, 7], self.matrixColors[5, 7], way)
        #LEFT
        elif turn == 5:
            self.pieces[3], self.pieces[7], self.pieces[11], self.pieces[4] = swap4(self.pieces[3], self.pieces[7], 
                                                                                self.pieces[11], self.pieces[4], way)

            self.pieces[12], self.pieces[15], self.pieces[19], self.pieces[16] = swap4(self.pieces[12], self.pieces[15], 
                                                                                   self.pieces[19], self.pieces[16], way)

            self.matrixColors[0, 4], self.matrixColors[4, 4], self.matrixColors[3, 2], self.matrixColors[1, 4] = swap4(self.matrixColors[0, 4], 
            self.matrixColors[4, 4], self.matrixColors[3, 2], self.matrixColors[1, 4], way)

            self.matrixColors[1, 8], self.matrixColors[0, 8], self.matrixColors[4, 8], self.matrixColors[3, 6] = swap4(self.matrixColors[1, 8], 
            self.matrixColors[0, 8], self.matrixColors[4, 8], self.matrixColors[3, 6], way)

            self.matrixColors[1, 5], self.matrixColors[0, 5], self.matrixColors[4, 5], self.matrixColors[3, 7] = swap4(self.matrixColors[1, 5], 
            self.matrixColors[0, 5], self.matrixColors[4, 5], self.matrixColors[3, 7], way)

    def isSolved(self):
        return np.array_equal(self.matrixColors, matrixRef)

    def colorsInPlace(self):
        return np.sum(self.matrixColors == matrixRef)

    def piecesInPlace(self):
        return sum(np.all(self.pieces == piecesRef, axis=1))

    def orientedPiecesInPlace(self):
        k=0
        for idx, i in enumerate(np.all(self.pieces == piecesRef, axis=1)):
            if i:
                if idx == 0 and self.matrixColors[0, 1] == 'w':
                    k+=1
                elif idx == 1 and self.matrixColors[0, 2] == 'w':
                    k+=1
                elif idx == 2 and self.matrixColors[0, 3] == 'w':
                    k+=1
                elif idx == 3 and self.matrixColors[0, 4] == 'w':
                    k+=1
                elif idx == 4 and self.matrixColors[1, 4] == 'g':
                    k+=1
                elif idx == 5 and self.matrixColors[1, 2] == 'g':
                    k+=1
                elif idx == 6 and self.matrixColors[2, 3] == 'r':
                    k+=1
                elif idx == 7 and self.matrixColors[5, 3] == 'o':
                    k+=1
                elif idx == 8 and self.matrixColors[1, 1] == 'g':
                    k+=1
                elif idx == 9 and self.matrixColors[2, 2] == 'r':
                    k+=1
                elif idx == 10 and self.matrixColors[4, 3] == 'b':
                    k+=1
                elif idx == 11 and self.matrixColors[5, 4] == 'o':
                    k+=1
                elif idx == 12 and self.matrixColors[0, 5] == 'w':
                    k+=1
                elif idx == 13 and self.matrixColors[0, 6] == 'w':
                    k+=1
                elif idx == 14 and self.matrixColors[0, 7] == 'w':
                    k+=1
                elif idx == 15 and self.matrixColors[0, 8] == 'w':
                    k+=1
                elif idx == 16 and self.matrixColors[3, 6] == 'y':
                    k+=1
                elif idx == 17 and self.matrixColors[3, 5] == 'y':
                    k+=1
                elif idx == 18 and self.matrixColors[3, 8] == 'y':
                    k+=1
                elif idx == 19 and self.matrixColors[3, 7] == 'y':
                    k+=1
        return k
    
    def printCube(self):
        print("rubiks_cube: \n")
        print("      {0} {1} {2}".format(self.matrixColors[4, 8], self.matrixColors[4, 3], self.matrixColors[4, 7]))
        print("      {0} {1} {2}".format(self.matrixColors[4, 4], self.matrixColors[4, 0], self.matrixColors[4, 2]))
        print("      {0} {1} {2}".format(self.matrixColors[4, 5], self.matrixColors[4, 1], self.matrixColors[4, 6]))
        print("      -----")
        print("{0} {1} {2}|".format(self.matrixColors[5, 8], self.matrixColors[5, 3], self.matrixColors[5, 7]), end='')
        print("{0} {1} {2}|".format(self.matrixColors[0, 8], self.matrixColors[0, 3], self.matrixColors[0, 7]), end='')
        print("{0} {1} {2}|".format(self.matrixColors[2, 8], self.matrixColors[2, 3], self.matrixColors[2, 7]), end='')
        print("{0} {1} {2}".format(self.matrixColors[3, 8], self.matrixColors[3, 3], self.matrixColors[3, 7]))
        print("{0} {1} {2}|".format(self.matrixColors[5, 4], self.matrixColors[5, 0], self.matrixColors[5, 2]), end='')
        print("{0} {1} {2}|".format(self.matrixColors[0, 4], self.matrixColors[0, 0], self.matrixColors[0, 2]), end='')
        print("{0} {1} {2}|".format(self.matrixColors[2, 4], self.matrixColors[2, 0], self.matrixColors[2, 2]), end='')
        print("{0} {1} {2} ".format(self.matrixColors[3, 4], self.matrixColors[3, 0], self.matrixColors[3, 2]))
        print("{0} {1} {2}|".format(self.matrixColors[5, 5], self.matrixColors[5, 1], self.matrixColors[5, 6]), end='')
        print("{0} {1} {2}|".format(self.matrixColors[0, 5], self.matrixColors[0, 1], self.matrixColors[0, 6]), end='')
        print("{0} {1} {2}|".format(self.matrixColors[2, 5], self.matrixColors[2, 1], self.matrixColors[2, 6]), end='')
        print("{0} {1} {2} ".format(self.matrixColors[3, 5], self.matrixColors[3, 1], self.matrixColors[3, 6]))
        print("      -----")
        print("      {0} {1} {2}".format(self.matrixColors[1, 8], self.matrixColors[1, 3], self.matrixColors[1, 7]))
        print("      {0} {1} {2}".format(self.matrixColors[1, 4], self.matrixColors[1, 0], self.matrixColors[1, 2]))
        print("      {0} {1} {2}".format(self.matrixColors[1, 5], self.matrixColors[1, 1], self.matrixColors[1, 6]))
        print()

    def scrambleCube(self, scramble):
        turns = [notation[turn] for turn in scramble.split()]
        for turn in turns:
            self.turnFace(turn[0], turn[1])

    def getMatrix(self):
        return self.matrixColors

    def setMatrix(self, matrix):
        self.matrixColors = matrix

    def getBinaryMatrix(self):
        binaryMatrix = np.zeros(288)
        for i in range(6):
            for j in range(1, 9):
                m = 5 if j == 0 else 1
                if self.matrixColors[i][j] == 'w':
                    binaryMatrix[(j-1)*6+i*48] = 1 * m
                elif self.matrixColors[i][j] == 'g':
                    binaryMatrix[(j-1)*6+1+i*48]=1 * m
                elif self.matrixColors[i][j] == 'r':
                    binaryMatrix[(j-1)*6+2+i*48]=1 * m
                elif self.matrixColors[i][j] == 'y':
                    binaryMatrix[(j-1)*6+3+i*48]=1 * m
                elif self.matrixColors[i][j] == 'b':
                    binaryMatrix[(j-1)*6+4+i*48]=1 * m
                elif self.matrixColors[i][j] == 'o':
                    binaryMatrix[(j-1)*6+5+i*48]=1 * m
        return binaryMatrix

    def getBinaryMatrix2(self):
        binaryMatrix = np.zeros(144)
        for i in range(6):
            for j in range(1, 9):
                if self.matrixColors[i][j] == 'w':
                    binaryMatrix[(j-1)*3+2+i*24]=0
                elif self.matrixColors[i][j] == 'g':
                    binaryMatrix[(j-1)*3+1+i*24]=1
                elif self.matrixColors[i][j] == 'r':
                    binaryMatrix[(j-1)*3+1+i*24]=1
                    binaryMatrix[(j-1)*3+2+i*24]=1
                elif self.matrixColors[i][j] == 'y':
                    binaryMatrix[(j-1)*3+i*24]=1.0
                elif self.matrixColors[i][j] == 'b':
                    binaryMatrix[(j-1)*3+i*24]=1.0
                    binaryMatrix[(j-1)*3+2+i*24]=1.0
                elif self.matrixColors[i][j] == 'o':
                    binaryMatrix[(j-1)*3+i*24]=1.0
                    binaryMatrix[(j-1)*3+1+i*24]=1.0
        return binaryMatrix
