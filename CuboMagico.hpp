#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <ctype.h>
#include <string>
#include "MatrixOperations.hpp"
class CuboMagico {
public:
    CuboMagico(int resolvido);
    CuboMagico(std::string scramble);
    CuboMagico(char matriz[6][9]);
    void Set();
    virtual ~CuboMagico();
    void scrambleCube(std::string scramble);
    void turnFace(int sentido, char face);
    void printCube();
    bool isSolved();
    int coresNoLugar();
    int pecasNoLugar();
    int pecasOrientadasNoLugar();
    void printPecas();
    char getCor(int i, int j);
    bool validScramble(std::string scramble);
    double **stateToBinaryMatrix();
    double **oldStateToBinaryMatrix();
private:
    typedef struct peca{
        char tipo; //a para aresta e q para quina
        char cor[3]; //w branco, y amarelo, g verde, b azul, r vermelho, o laranja.
    }peca;
    char matrizCores[6][9];
    double **binaryMatrix;
    int inteiroLado(char face);
    char charLado(int face);
    char charCorLado(int face);
    peca pecas[20]; //arestas de 0 a 11 e quinas de 12 a 19
};
