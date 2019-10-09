#include "CuboMagico.hpp"
/*
                                -----------------------------------
                                | qeitct(48) aitct(43) qditct(47) |
                                | aetct(44)  ct(40)    adtct(42)  |
                                | qestct(45) astct(41) qdstct(46) |
---------------------------------------------------------------------------------------------------------------------------------------
qeitce(58) aetce(53) qestce(57) | qestcs(08) astcs(03) qdstcs(07) | qdstcd(28) adtcd(23) qditcd(27) | qditci(38) aitci(33) qeitci(37) |
aeice(54)  ce(50)    aesce(52)  | aescs(04)  cs(00)    adscs(02)  | adscd(24)  cd(20)    adicd(22)  | adici(34)  ci(30)    aeici(32)  |
qeifce(55) aefce(51) qesfce(56) | qesfcs(05) asfcs(01) qesfcs(06) | qdsfcd(25) adfcd(21) qdsfcd(26) | qdifci(35) aifci(31) qeifci(36) |
---------------------------------------------------------------------------------------------------------------------------------------
                                | qesfcf(18) asfcf(13) qdsfcf(17) |
                                | aefcf(14)  cf(10)    adfcf(12)  |
                                | qeifcf(15) aifcf(11) qdifcf(16) |
                                -----------------------------------
peca 0 aresta w g peca 1 aresta w r peca 2 aresta w b peca 3 aresta w o
peca 4 aresta g o peca 5 aresta g r peca 6 aresta r b peca 7 aresta b o
peca 8 aresta y g peca 9 aresta y r peca 10 aresta y b peca 11 aresta y o
peca 12 quina w g o peca 13 quina w g r  peca 14 quina w b r peca 15 quina w b o
peca 16 quina y g o peca 17 quina y g r peca 18 quina y b r peca 19 quina y b o
*/

CuboMagico::CuboMagico(int resolvido){
    Set();
}

void CuboMagico::Set(){
    int size[2] = {1, 146};
    binaryMatrix = newMatrix(size);
    matrizCores[0][0]='w'; matrizCores[1][0]='g'; matrizCores[2][0]='r'; matrizCores[3][0]='y'; matrizCores[4][0]='b'; matrizCores[5][0]='o';  //centros
    matrizCores[0][1]='w'; matrizCores[1][1]='g'; matrizCores[2][1]='r'; matrizCores[3][1]='y'; matrizCores[4][1]='b'; matrizCores[5][1]='o';  //aresta 1
    matrizCores[0][2]='w'; matrizCores[1][2]='g'; matrizCores[2][2]='r'; matrizCores[3][2]='y'; matrizCores[4][2]='b'; matrizCores[5][2]='o';  //aresta 2
    matrizCores[0][3]='w'; matrizCores[1][3]='g'; matrizCores[2][3]='r'; matrizCores[3][3]='y'; matrizCores[4][3]='b'; matrizCores[5][3]='o';  //aersta 3
    matrizCores[0][4]='w'; matrizCores[1][4]='g'; matrizCores[2][4]='r'; matrizCores[3][4]='y'; matrizCores[4][4]='b'; matrizCores[5][4]='o';  //aresta 4
    matrizCores[0][5]='w'; matrizCores[1][5]='g'; matrizCores[2][5]='r'; matrizCores[3][5]='y'; matrizCores[4][5]='b'; matrizCores[5][5]='o';  //quina 1
    matrizCores[0][6]='w'; matrizCores[1][6]='g'; matrizCores[2][6]='r'; matrizCores[3][6]='y'; matrizCores[4][6]='b'; matrizCores[5][6]='o';  //quina 2
    matrizCores[0][7]='w'; matrizCores[1][7]='g'; matrizCores[2][7]='r'; matrizCores[3][7]='y'; matrizCores[4][7]='b'; matrizCores[5][7]='o';  //quina 3
    matrizCores[0][8]='w'; matrizCores[1][8]='g'; matrizCores[2][8]='r'; matrizCores[3][8]='y'; matrizCores[4][8]='b'; matrizCores[5][8]='o';  //quina 4
    peca arestaWG; arestaWG.tipo='a'; arestaWG.cor[0]='w'; arestaWG.cor[1]='g';
    pecas[0]=arestaWG;
    peca arestaWR; arestaWR.tipo='a'; arestaWR.cor[0]='w'; arestaWR.cor[1]='r';
    pecas[1]=arestaWR;
    peca arestaWB; arestaWB.tipo='a'; arestaWB.cor[0]='w'; arestaWB.cor[1]='b';
    pecas[2]=arestaWB;
    peca arestaWO; arestaWO.tipo='a'; arestaWO.cor[0]='w'; arestaWO.cor[1]='o';
    pecas[3]=arestaWO;
    peca arestaGO; arestaGO.tipo='a'; arestaGO.cor[0]='g'; arestaGO.cor[1]='o';
    pecas[4]=arestaGO;
    peca arestaGR; arestaGR.tipo='a'; arestaGR.cor[0]='g'; arestaGR.cor[1]='r';
    pecas[5]=arestaGR;
    peca arestaRB; arestaRB.tipo='a'; arestaRB.cor[0]='r'; arestaRB.cor[1]='b';
    pecas[6]=arestaRB;
    peca arestaBO; arestaBO.tipo='a'; arestaBO.cor[0]='b'; arestaBO.cor[1]='o';
    pecas[7]=arestaBO;
    peca arestaYG; arestaYG.tipo='a'; arestaYG.cor[0]='y'; arestaYG.cor[1]='g';
    pecas[8]=arestaYG;
    peca arestaYR; arestaYR.tipo='a'; arestaYR.cor[0]='y'; arestaYR.cor[1]='r';
    pecas[9]=arestaYR;
    peca arestaYB; arestaYB.tipo='a'; arestaYB.cor[0]='y'; arestaYB.cor[1]='b';
    pecas[10]=arestaYB;
    peca arestaYO; arestaYO.tipo='a'; arestaYO.cor[0]='y'; arestaYO.cor[1]='o';
    pecas[11]=arestaYO;
    peca quinaWGO; quinaWGO.tipo='q'; quinaWGO.cor[0]='w'; quinaWGO.cor[1]='g'; quinaWGO.cor[2]='o';
    pecas[12]=quinaWGO;
    peca quinaWGR; quinaWGR.tipo='q'; quinaWGR.cor[0]='w'; quinaWGR.cor[1]='g'; quinaWGR.cor[2]='r';
    pecas[13]=quinaWGR;
    peca quinaWBR; quinaWBR.tipo='q'; quinaWBR.cor[0]='w'; quinaWBR.cor[1]='b'; quinaWBR.cor[2]='r';
    pecas[14]=quinaWBR;
    peca quinaWBO; quinaWBO.tipo='q'; quinaWBO.cor[0]='w'; quinaWBO.cor[1]='b'; quinaWBO.cor[2]='o';
    pecas[15]=quinaWBO;
    peca quinaYGO; quinaYGO.tipo='q'; quinaYGO.cor[0]='y'; quinaYGO.cor[1]='g'; quinaYGO.cor[2]='o';
    pecas[16]=quinaYGO;
    peca quinaYGR; quinaYGR.tipo='q'; quinaYGR.cor[0]='y'; quinaYGR.cor[1]='g'; quinaYGR.cor[2]='r';
    pecas[17]=quinaYGR;
    peca quinaYBR; quinaYBR.tipo='q'; quinaYBR.cor[0]='y'; quinaYBR.cor[1]='b'; quinaYBR.cor[2]='r';
    pecas[18]=quinaYBR;
    peca quinaYBO; quinaYBO.tipo='q'; quinaYBO.cor[0]='y'; quinaYBO.cor[1]='b'; quinaYBO.cor[2]='o';
    pecas[19]=quinaYBO;
}

CuboMagico::CuboMagico(char matriz[6][9]){
    int size[2] = {1, 146};
    binaryMatrix = newMatrix(size);
    for(int i=0; i<6; i++){
        for(int j=0; j<9; j++){
            matrizCores[i][j] = matriz[i][j];
        }
    }
}

CuboMagico::CuboMagico(std::string scramble){
    CuboMagico(1);
    scrambleCube(scramble);
}

CuboMagico::~CuboMagico() {}

int CuboMagico::inteiroLado(char face){
    int lado;
    switch(face){
        case 'u'|'U':
            lado=0;
            break;
        case 'f'|'F':
            lado=1;
            break;
        case 'r'|'R':
            lado=2;
            break;
        case 'd'|'D':
            lado=3;
            break;
        case 'b'|'B':
            lado=4;
            break;
        case 'l'|'L':
            lado=5;
            break;
        default:
            return -1;
        }
    return lado;
}

bool validLetter(char letter) {
    if (letter == 'R' || letter == 'L' || letter == 'F' || letter == 'B' || letter == 'D' || letter == 'U') {
        return true;
    }
    return false;
}

bool CuboMagico::validScramble(std::string scramble) {
    int i;
    for (i = 0; scramble[i] != '\0'; i++) {
        switch(scramble[i]) {
            case 'R':
            case 'r':
            case 'L':
            case 'l':
            case 'F':
            case 'f':
            case 'B':
            case 'b':
            case 'D':
            case 'd':
            case 'U':
            case 'u':
                if(i != 0 && scramble[i-1] != ' ') {
                    return false;
                }
                break;
            case '2':
            case '\'':
                if(i == 0 || !validLetter(scramble[i-1])) {
                    return false;
                }
                break;
            case ' ':
            case '\n':
                break;
            default:
                return false;
        }
    }
    return true;
}

void CuboMagico::scrambleCube(std::string scramble) {
    int i;
    for (i = 0; scramble[i] != '\0'; i++) {
        switch(scramble[i]) {
            case 'R':
            case 'r':
            case 'L':
            case 'l':
            case 'F':
            case 'f':
            case 'B':
            case 'b':
            case 'D':
            case 'd':
            case 'U':
            case 'u':
                if(scramble[i+1] == ' ' || scramble[i+1] == '\n' || scramble[i+1] == '\0') {
                    turnFace(0, tolower(scramble[i]));
                }
                else if(scramble[i+1] == '\'') {
                    turnFace(1, tolower(scramble[i]));
                }
                else if(scramble[i+1] == '2') {
                    turnFace(2, tolower(scramble[i]));
                }
                break;
            default:
                break;
        }
    }
}

char CuboMagico::getCor(int i, int j){
    return matrizCores[i][j];
}

char CuboMagico::charLado(int face){
    char lado;
    switch(face){
        case 0:
            lado='U';
            break;
        case 1:
            lado='F';
            break;
        case 2:
            lado='R';
            break;
        case 3:
            lado='D';
            break;
        case 4:
            lado='B';
            break;
        case 5:
            lado='L';
            break;
        default:
            return ' ';
        }
    return lado;
}

void CuboMagico::turnFace(int sentido, char face){ //sentido 0 = horario, 1 = anti-horario, 2 = giro duplo.
    //printf("\n%c%d\n", face, sentido);
    int lado = inteiroLado(face);
    char auxa[3];
    char auxq[6];
    peca auxar[3];
    peca auxqu[3];

    if(sentido == 0 | sentido == 2){
        auxa[0] = matrizCores[lado][4];
        auxa[1] = matrizCores[lado][2];
        auxa[2] = matrizCores[lado][3];

        auxq[0] = matrizCores[lado][8];
        auxq[1] = matrizCores[lado][6];
        auxq[2] = matrizCores[lado][7];

        matrizCores[lado][4]=matrizCores[lado][1];
        matrizCores[lado][8]=matrizCores[lado][5];

        matrizCores[lado][1]=auxa[1];
        matrizCores[lado][2]=auxa[2];
        matrizCores[lado][3]=auxa[0];

        matrizCores[lado][5]=auxq[1];
        matrizCores[lado][6]=auxq[2];
        matrizCores[lado][7]=auxq[0];
        switch(lado){
            case 0:
                auxar[0] = pecas[3];
                auxar[1] = pecas[2];
                auxar[2] = pecas[1];

                pecas[3]=pecas[0];
                pecas[2]=auxar[0];
                pecas[1]=auxar[1];
                pecas[0]=auxar[2];

                auxqu[0] = pecas[12];
                auxqu[1] = pecas[15];
                auxqu[2] = pecas[14];

                pecas[12]=pecas[13];
                pecas[15]=auxqu[0];
                pecas[14]=auxqu[1];
                pecas[13]=auxqu[2];

                auxa[0] = matrizCores[4][1];
                auxa[1] = matrizCores[2][4];
                auxa[2] = matrizCores[1][3];

                auxq[0] = matrizCores[4][5];
                auxq[1] = matrizCores[2][8];
                auxq[2] = matrizCores[1][7];

                auxq[3] = matrizCores[4][6];
                auxq[4] = matrizCores[2][5];
                auxq[5] = matrizCores[1][8];

                matrizCores[4][1] = matrizCores[5][2];
                matrizCores[4][5] = matrizCores[5][6];
                matrizCores[4][6] = matrizCores[5][7];

                matrizCores[2][4] = auxa[0];
                matrizCores[1][3] = auxa[1];
                matrizCores[5][2] = auxa[2];

                matrizCores[2][8] = auxq[0];
                matrizCores[1][7] = auxq[1];
                matrizCores[5][6] = auxq[2];

                matrizCores[2][5] = auxq[3];
                matrizCores[1][8] = auxq[4];
                matrizCores[5][7] = auxq[5];
            break;
            case 1:
                auxar[0] = pecas[0];
                auxar[1] = pecas[5];
                auxar[2] = pecas[8];

                pecas[0]=pecas[4];
                pecas[5]=auxar[0];
                pecas[8]=auxar[1];
                pecas[4]=auxar[2];

                auxqu[0] = pecas[12];
                auxqu[1] = pecas[13];
                auxqu[2] = pecas[17];

                pecas[12]=pecas[16];
                pecas[13]=auxqu[0];
                pecas[17]=auxqu[1];
                pecas[16]=auxqu[2];

                auxa[0] = matrizCores[0][1];
                auxa[1] = matrizCores[2][1];
                auxa[2] = matrizCores[3][1];

                auxq[0] = matrizCores[0][5];
                auxq[1] = matrizCores[2][5];
                auxq[2] = matrizCores[3][5];

                auxq[3] = matrizCores[0][6];
                auxq[4] = matrizCores[2][6];
                auxq[5] = matrizCores[3][6];

                matrizCores[0][1] = matrizCores[5][1];
                matrizCores[0][5] = matrizCores[5][5];
                matrizCores[0][6] = matrizCores[5][6];

                matrizCores[2][1] = auxa[0];
                matrizCores[3][1] = auxa[1];
                matrizCores[5][1] = auxa[2];

                matrizCores[2][5] = auxq[0];
                matrizCores[3][5] = auxq[1];
                matrizCores[5][5] = auxq[2];

                matrizCores[2][6] = auxq[3];
                matrizCores[3][6] = auxq[4];
                matrizCores[5][6] = auxq[5];
            break;
            case 2:
                auxar[0] = pecas[1];
                auxar[1] = pecas[6];
                auxar[2] = pecas[9];

                pecas[1]=pecas[5];
                pecas[6]=auxar[0];
                pecas[9]=auxar[1];
                pecas[5]=auxar[2];

                auxqu[0] = pecas[13];
                auxqu[1] = pecas[14];
                auxqu[2] = pecas[18];

                pecas[13]=pecas[17];
                pecas[14]=auxqu[0];
                pecas[18]=auxqu[1];
                pecas[17]=auxqu[2];

                auxa[0] = matrizCores[1][2];
                auxa[1] = matrizCores[0][2];
                auxa[2] = matrizCores[4][2];

                auxq[0] = matrizCores[1][7];
                auxq[1] = matrizCores[0][7];
                auxq[2] = matrizCores[4][7];

                auxq[3] = matrizCores[1][6];
                auxq[4] = matrizCores[0][6];
                auxq[5] = matrizCores[4][6];

                matrizCores[1][2] = matrizCores[3][4];
                matrizCores[1][7] = matrizCores[3][5];
                matrizCores[1][6] = matrizCores[3][8];

                matrizCores[0][2] = auxa[0];
                matrizCores[4][2] = auxa[1];
                matrizCores[3][4] = auxa[2];

                matrizCores[0][7] = auxq[0];
                matrizCores[4][7] = auxq[1];
                matrizCores[3][5] = auxq[2];

                matrizCores[0][6] = auxq[3];
                matrizCores[4][6] = auxq[4];
                matrizCores[3][8] = auxq[5];
            break;
            case 3:
                auxar[0] = pecas[8];
                auxar[1] = pecas[9];
                auxar[2] = pecas[10];

                pecas[8]=pecas[11];
                pecas[9]=auxar[0];
                pecas[10]=auxar[1];
                pecas[11]=auxar[2];

                auxqu[0] = pecas[16];
                auxqu[1] = pecas[17];
                auxqu[2] = pecas[18];

                pecas[16]=pecas[19];
                pecas[17]=auxqu[0];
                pecas[18]=auxqu[1];
                pecas[19]=auxqu[2];

                auxa[0] = matrizCores[1][1];
                auxa[1] = matrizCores[2][2];
                auxa[2] = matrizCores[4][3];

                auxq[0] = matrizCores[1][5];
                auxq[1] = matrizCores[2][6];
                auxq[2] = matrizCores[4][7];

                auxq[3] = matrizCores[1][6];
                auxq[4] = matrizCores[2][7];
                auxq[5] = matrizCores[4][8];

                matrizCores[1][1] = matrizCores[5][4];
                matrizCores[1][5] = matrizCores[5][8];
                matrizCores[1][6] = matrizCores[5][5];

                matrizCores[2][2] = auxa[0];
                matrizCores[4][3] = auxa[1];
                matrizCores[5][4] = auxa[2];

                matrizCores[2][6] = auxq[0];
                matrizCores[4][7] = auxq[1];
                matrizCores[5][8] = auxq[2];

                matrizCores[2][7] = auxq[3];
                matrizCores[4][8] = auxq[4];
                matrizCores[5][5] = auxq[5];
            break;
            case 4:
                auxar[0] = pecas[2];
                auxar[1] = pecas[6];
                auxar[2] = pecas[7];

                pecas[6]=pecas[10];
                pecas[7]=auxar[0];
                pecas[2]=auxar[1];
                pecas[10]=auxar[2];

                auxqu[0] = pecas[14];
                auxqu[1] = pecas[15];
                auxqu[2] = pecas[18];

                pecas[18]=pecas[19];
                pecas[19]=auxqu[0];
                pecas[14]=auxqu[1];
                pecas[15]=auxqu[2];

                auxa[0] = matrizCores[3][3];
                auxa[1] = matrizCores[5][3];
                auxa[2] = matrizCores[0][3];

                auxq[0] = matrizCores[3][8];
                auxq[1] = matrizCores[5][8];
                auxq[2] = matrizCores[0][8];

                auxq[3] = matrizCores[3][7];
                auxq[4] = matrizCores[5][7];
                auxq[5] = matrizCores[0][7];

                matrizCores[0][3] = matrizCores[2][3];
                matrizCores[0][8] = matrizCores[2][8];
                matrizCores[0][7] = matrizCores[2][7];

                matrizCores[2][3] = auxa[0];
                matrizCores[3][3] = auxa[1];
                matrizCores[5][3] = auxa[2];

                matrizCores[2][8] = auxq[0];
                matrizCores[3][8] = auxq[1];
                matrizCores[5][8] = auxq[2];

                matrizCores[2][7] = auxq[3];
                matrizCores[3][7] = auxq[4];
                matrizCores[5][7] = auxq[5];
            break;
            case 5:
                auxar[0] = pecas[3];
                auxar[1] = pecas[4];
                auxar[2] = pecas[11];

                pecas[3]=pecas[7];
                pecas[4]=auxar[0];
                pecas[11]=auxar[1];
                pecas[7]=auxar[2];

                auxqu[0] = pecas[12];
                auxqu[1] = pecas[16];
                auxqu[2] = pecas[19];

                pecas[12]=pecas[15];
                pecas[16]=auxqu[0];
                pecas[19]=auxqu[1];
                pecas[15]=auxqu[2];

                auxa[0] = matrizCores[4][4];
                auxa[1] = matrizCores[0][4];
                auxa[2] = matrizCores[1][4];

                auxq[0] = matrizCores[4][5];
                auxq[1] = matrizCores[0][5];
                auxq[2] = matrizCores[1][5];

                auxq[3] = matrizCores[4][8];
                auxq[4] = matrizCores[0][8];
                auxq[5] = matrizCores[1][8];

                matrizCores[4][4] = matrizCores[3][2];
                matrizCores[4][5] = matrizCores[3][7];
                matrizCores[4][8] = matrizCores[3][6];

                matrizCores[0][4] = auxa[0];
                matrizCores[1][4] = auxa[1];
                matrizCores[3][2] = auxa[2];

                matrizCores[0][5] = auxq[0];
                matrizCores[1][5] = auxq[1];
                matrizCores[3][7] = auxq[2];

                matrizCores[0][8] = auxq[3];
                matrizCores[1][8] = auxq[4];
                matrizCores[3][6] = auxq[5];
            break;
            default:
            break;
        }
    }
    else if(sentido == 1){
        auxa[0] = matrizCores[lado][1];
        auxa[1] = matrizCores[lado][2];
        auxa[2] = matrizCores[lado][3];

        auxq[0] = matrizCores[lado][5];
        auxq[1] = matrizCores[lado][6];
        auxq[2] = matrizCores[lado][7];

        matrizCores[lado][1]=matrizCores[lado][4];
        matrizCores[lado][5]=matrizCores[lado][8];

        matrizCores[lado][2]=auxa[0];
        matrizCores[lado][3]=auxa[1];
        matrizCores[lado][4]=auxa[2];

        matrizCores[lado][6]=auxq[0];
        matrizCores[lado][7]=auxq[1];
        matrizCores[lado][8]=auxq[2];
        switch(lado){
            case 0:
                auxar[0] = pecas[0];
                auxar[1] = pecas[1];
                auxar[2] = pecas[2];

                pecas[0]=pecas[3];
                pecas[1]=auxar[0];
                pecas[2]=auxar[1];
                pecas[3]=auxar[2];

                auxqu[0] = pecas[12];
                auxqu[1] = pecas[13];
                auxqu[2] = pecas[14];

                pecas[12]=pecas[15];
                pecas[13]=auxqu[0];
                pecas[14]=auxqu[1];
                pecas[15]=auxqu[2];

                auxa[0] = matrizCores[1][3];
                auxa[1] = matrizCores[5][2];
                auxa[2] = matrizCores[4][1];

                auxq[0] = matrizCores[1][7];
                auxq[1] = matrizCores[5][6];
                auxq[2] = matrizCores[4][5];

                auxq[3] = matrizCores[1][8];
                auxq[4] = matrizCores[5][7];
                auxq[5] = matrizCores[4][6];

                matrizCores[4][1] = matrizCores[2][4];
                matrizCores[4][5] = matrizCores[2][8];
                matrizCores[4][6] = matrizCores[2][5];

                matrizCores[2][4] = auxa[0];
                matrizCores[1][3] = auxa[1];
                matrizCores[5][2] = auxa[2];

                matrizCores[2][8] = auxq[0];
                matrizCores[1][7] = auxq[1];
                matrizCores[5][6] = auxq[2];

                matrizCores[2][5] = auxq[3];
                matrizCores[1][8] = auxq[4];
                matrizCores[5][7] = auxq[5];
            break;
            case 1:
                auxar[0] = pecas[0];
                auxar[1] = pecas[4];
                auxar[2] = pecas[8];

                pecas[0]=pecas[5];
                pecas[4]=auxar[0];
                pecas[8]=auxar[1];
                pecas[5]=auxar[2];

                auxqu[0] = pecas[12];
                auxqu[1] = pecas[16];
                auxqu[2] = pecas[17];

                pecas[12]=pecas[13];
                pecas[16]=auxqu[0];
                pecas[17]=auxqu[1];
                pecas[13]=auxqu[2];

                auxa[0] = matrizCores[3][1];
                auxa[1] = matrizCores[5][1];
                auxa[2] = matrizCores[0][1];

                auxq[0] = matrizCores[3][5];
                auxq[1] = matrizCores[5][5];
                auxq[2] = matrizCores[0][5];

                auxq[3] = matrizCores[3][6];
                auxq[4] = matrizCores[5][6];
                auxq[5] = matrizCores[0][6];

                matrizCores[0][1] = matrizCores[2][1];
                matrizCores[0][5] = matrizCores[2][5];
                matrizCores[0][6] = matrizCores[2][6];

                matrizCores[2][1] = auxa[0];
                matrizCores[3][1] = auxa[1];
                matrizCores[5][1] = auxa[2];

                matrizCores[2][5] = auxq[0];
                matrizCores[3][5] = auxq[1];
                matrizCores[5][5] = auxq[2];

                matrizCores[2][6] = auxq[3];
                matrizCores[3][6] = auxq[4];
                matrizCores[5][6] = auxq[5];
            break;
            case 2:
                auxar[0] = pecas[1];
                auxar[1] = pecas[5];
                auxar[2] = pecas[9];

                pecas[1]=pecas[6];
                pecas[5]=auxar[0];
                pecas[9]=auxar[1];
                pecas[6]=auxar[2];
                
                auxqu[0] = pecas[13];
                auxqu[1] = pecas[17];
                auxqu[2] = pecas[18];

                pecas[13]=pecas[14];
                pecas[17]=auxqu[0];
                pecas[18]=auxqu[1];
                pecas[14]=auxqu[2];

                auxa[0] = matrizCores[4][2];
                auxa[1] = matrizCores[3][4];
                auxa[2] = matrizCores[1][2];

                auxq[0] = matrizCores[4][7];
                auxq[1] = matrizCores[3][5];
                auxq[2] = matrizCores[1][7];

                auxq[3] = matrizCores[4][6];
                auxq[4] = matrizCores[3][8];
                auxq[5] = matrizCores[1][6];

                matrizCores[1][2] = matrizCores[0][2];
                matrizCores[1][7] = matrizCores[0][7];
                matrizCores[1][6] = matrizCores[0][6];

                matrizCores[0][2] = auxa[0];
                matrizCores[4][2] = auxa[1];
                matrizCores[3][4] = auxa[2];

                matrizCores[0][7] = auxq[0];
                matrizCores[4][7] = auxq[1];
                matrizCores[3][5] = auxq[2];

                matrizCores[0][6] = auxq[3];
                matrizCores[4][6] = auxq[4];
                matrizCores[3][8] = auxq[5];
            break;
            case 3:
                auxar[0] = pecas[8];
                auxar[1] = pecas[9];
                auxar[2] = pecas[10];

                pecas[10]=pecas[11];
                pecas[11]=auxar[0];
                pecas[8]=auxar[1];
                pecas[9]=auxar[2];

                auxqu[0] = pecas[16];
                auxqu[1] = pecas[17];
                auxqu[2] = pecas[18];

                pecas[18]=pecas[19];
                pecas[19]=auxqu[0];
                pecas[16]=auxqu[1];
                pecas[17]=auxqu[2];

                auxa[0] = matrizCores[4][3];
                auxa[1] = matrizCores[5][4];
                auxa[2] = matrizCores[1][1];

                auxq[0] = matrizCores[5][8];
                auxq[1] = matrizCores[1][5];
                auxq[2] = matrizCores[2][6];

                auxq[3] = matrizCores[4][8];
                auxq[4] = matrizCores[5][5];
                auxq[5] = matrizCores[1][6];

                matrizCores[1][1] = matrizCores[2][2];
                matrizCores[2][6] = matrizCores[4][7];
                matrizCores[1][6] = matrizCores[2][7];

                matrizCores[2][2] = auxa[0];
                matrizCores[4][3] = auxa[1];
                matrizCores[5][4] = auxa[2];

                matrizCores[4][7] = auxq[0];
                matrizCores[5][8] = auxq[1];
                matrizCores[1][5] = auxq[2];

                matrizCores[2][7] = auxq[3];
                matrizCores[4][8] = auxq[4];
                matrizCores[5][5] = auxq[5];
            break;
            case 4:
                auxar[0] = pecas[2];
                auxar[1] = pecas[6];
                auxar[2] = pecas[10];

                pecas[2]=pecas[7];
                pecas[6]=auxar[0];
                pecas[10]=auxar[1];
                pecas[7]=auxar[2];

                auxqu[0] = pecas[14];
                auxqu[1] = pecas[15];
                auxqu[2] = pecas[18];

                pecas[14]=pecas[19];
                pecas[15]=auxqu[0];
                pecas[18]=auxqu[1];
                pecas[19]=auxqu[1];

                auxa[0] = matrizCores[0][3];
                auxa[1] = matrizCores[2][3];
                auxa[2] = matrizCores[3][3];

                auxq[0] = matrizCores[0][8];
                auxq[1] = matrizCores[2][8];
                auxq[2] = matrizCores[3][8];

                auxq[3] = matrizCores[0][7];
                auxq[4] = matrizCores[2][7];
                auxq[5] = matrizCores[3][7];

                matrizCores[0][3] = matrizCores[5][3];
                matrizCores[0][8] = matrizCores[5][8];
                matrizCores[0][7] = matrizCores[5][7];

                matrizCores[2][3] = auxa[0];
                matrizCores[3][3] = auxa[1];
                matrizCores[5][3] = auxa[2];

                matrizCores[2][8] = auxq[0];
                matrizCores[3][8] = auxq[1];
                matrizCores[5][8] = auxq[2];

                matrizCores[2][7] = auxq[3];
                matrizCores[3][7] = auxq[4];
                matrizCores[5][7] = auxq[5];
            break;
            case 5:
                auxar[0] = pecas[3];
                auxar[1] = pecas[7];
                auxar[2] = pecas[11];

                pecas[3]=pecas[4];
                pecas[7]=auxar[0];
                pecas[11]=auxar[1];
                pecas[4]=auxar[2];

                auxqu[0] = pecas[12];
                auxqu[1] = pecas[15];
                auxqu[2] = pecas[19];

                pecas[12]=pecas[16];
                pecas[15]=auxqu[0];
                pecas[19]=auxqu[1];
                pecas[16]=auxqu[2];

                auxa[0] = matrizCores[1][4];
                auxa[1] = matrizCores[3][2];
                auxa[2] = matrizCores[4][4];

                auxq[0] = matrizCores[1][5];
                auxq[1] = matrizCores[3][7];
                auxq[2] = matrizCores[4][5];

                auxq[3] = matrizCores[1][8];
                auxq[4] = matrizCores[3][6];
                auxq[5] = matrizCores[4][8];

                matrizCores[4][4] = matrizCores[0][4];
                matrizCores[4][5] = matrizCores[0][5];
                matrizCores[4][8] = matrizCores[0][8];

                matrizCores[0][4] = auxa[0];
                matrizCores[1][4] = auxa[1];
                matrizCores[3][2] = auxa[2];

                matrizCores[0][5] = auxq[0];
                matrizCores[1][5] = auxq[1];
                matrizCores[3][7] = auxq[2];

                matrizCores[0][8] = auxq[3];
                matrizCores[1][8] = auxq[4];
                matrizCores[3][6] = auxq[5];
            break;
            default:
            break;
        }
    }
    if(sentido==2) turnFace(0, face);
    //printCube();
}
char CuboMagico::charCorLado(int face){
    char lado;
    switch(face){
        case 0:
            lado='w';
            break;
        case 1:
            lado='g';
            break;
        case 2:
            lado='r';
            break;
        case 3:
            lado='y';
            break;
        case 4:
            lado='b';
            break;
        case 5:
            lado='o';
            break;
        default:
            return ' ';
        }
    return lado;
}
bool CuboMagico::isSolved(){
    for(int i=0; i<6; i++){
        for(int j=0; j<9; j++){
            if(matrizCores[i][j]!=charCorLado(i)) return false;
        }
    }
    return true;
}
int CuboMagico::coresNoLugar(){
    int k = 0;
    for(int i=0; i<6; i++){
        for(int j=0; j<9; j++){
            if(matrizCores[i][j]==charCorLado(i)) k++;
        }
    }
    return k;
}

int CuboMagico::pecasNoLugar(){
    int k = 0;
    if(pecas[0].cor[0]=='w' && pecas[0].cor[1]=='g') k++;
    if(pecas[1].cor[0]=='w' && pecas[1].cor[1]=='r') k++;
    if(pecas[2].cor[0]=='w' && pecas[2].cor[1]=='b') k++;
    if(pecas[3].cor[0]=='w' && pecas[3].cor[1]=='o') k++;
    if(pecas[4].cor[0]=='g' && pecas[4].cor[1]=='o') k++;
    if(pecas[5].cor[0]=='g' && pecas[5].cor[1]=='r') k++;
    if(pecas[6].cor[0]=='r' && pecas[6].cor[1]=='b') k++;
    if(pecas[7].cor[0]=='b' && pecas[7].cor[1]=='o') k++;
    if(pecas[8].cor[0]=='y' && pecas[8].cor[1]=='g') k++;
    if(pecas[9].cor[0]=='y' && pecas[9].cor[1]=='r') k++;
    if(pecas[10].cor[0]=='y' && pecas[10].cor[1]=='b') k++;
    if(pecas[11].cor[0]=='y' && pecas[11].cor[1]=='o') k++;
    if(pecas[12].cor[0]=='w' && pecas[12].cor[1]=='g' && pecas[12].cor[2]=='o') k++;
    if(pecas[13].cor[0]=='w' && pecas[13].cor[1]=='g' && pecas[13].cor[2]=='r') k++;
    if(pecas[14].cor[0]=='w' && pecas[14].cor[1]=='b' && pecas[14].cor[2]=='r') k++;
    if(pecas[15].cor[0]=='w' && pecas[15].cor[1]=='b' && pecas[15].cor[2]=='o') k++;
    if(pecas[16].cor[0]=='y' && pecas[16].cor[1]=='g' && pecas[16].cor[2]=='o') k++;
    if(pecas[17].cor[0]=='y' && pecas[17].cor[1]=='g' && pecas[17].cor[2]=='r') k++;
    if(pecas[18].cor[0]=='y' && pecas[18].cor[1]=='b' && pecas[18].cor[2]=='r') k++;
    if(pecas[19].cor[0]=='y' && pecas[19].cor[1]=='b' && pecas[19].cor[2]=='o') k++;
    return k;
}

int CuboMagico::pecasOrientadasNoLugar(){
    int k = 0;
    if(pecas[0].cor[0]=='w' && pecas[0].cor[1]=='g' && matrizCores[0][1]=='w') k++;
    if(pecas[1].cor[0]=='w' && pecas[1].cor[1]=='r' && matrizCores[0][2]=='w') k++;
    if(pecas[2].cor[0]=='w' && pecas[2].cor[1]=='b' && matrizCores[0][3]=='w') k++;
    if(pecas[3].cor[0]=='w' && pecas[3].cor[1]=='o' && matrizCores[0][4]=='w') k++;
    if(pecas[4].cor[0]=='g' && pecas[4].cor[1]=='o' && matrizCores[1][4]=='g') k++;
    if(pecas[5].cor[0]=='g' && pecas[5].cor[1]=='r' && matrizCores[1][2]=='g') k++;
    if(pecas[6].cor[0]=='r' && pecas[6].cor[1]=='b' && matrizCores[2][3]=='r') k++;
    if(pecas[7].cor[0]=='b' && pecas[7].cor[1]=='o' && matrizCores[4][4]=='b') k++;
    if(pecas[8].cor[0]=='y' && pecas[8].cor[1]=='g' && matrizCores[3][1]=='y') k++;
    if(pecas[9].cor[0]=='y' && pecas[9].cor[1]=='r' && matrizCores[3][4]=='y') k++;
    if(pecas[10].cor[0]=='y' && pecas[10].cor[1]=='b' && matrizCores[3][3]=='y') k++;
    if(pecas[11].cor[0]=='y' && pecas[11].cor[1]=='o' && matrizCores[3][2]=='y') k++;
    if(pecas[12].cor[0]=='w' && pecas[12].cor[1]=='g' && pecas[12].cor[2]=='o' && matrizCores[0][5]=='w') k++;
    if(pecas[13].cor[0]=='w' && pecas[13].cor[1]=='g' && pecas[13].cor[2]=='r' && matrizCores[0][6]=='w') k++;
    if(pecas[14].cor[0]=='w' && pecas[14].cor[1]=='b' && pecas[14].cor[2]=='r' && matrizCores[0][7]=='w') k++;
    if(pecas[15].cor[0]=='w' && pecas[15].cor[1]=='b' && pecas[15].cor[2]=='o' && matrizCores[0][8]=='w') k++;
    if(pecas[16].cor[0]=='y' && pecas[16].cor[1]=='g' && pecas[16].cor[2]=='o' && matrizCores[3][6]=='y') k++;
    if(pecas[17].cor[0]=='y' && pecas[17].cor[1]=='g' && pecas[17].cor[2]=='r' && matrizCores[3][5]=='y') k++;
    if(pecas[18].cor[0]=='y' && pecas[18].cor[1]=='b' && pecas[18].cor[2]=='r' && matrizCores[3][8]=='y') k++;
    if(pecas[19].cor[0]=='y' && pecas[19].cor[1]=='b' && pecas[19].cor[2]=='o' && matrizCores[3][7]=='y') k++;
    return k;
}

void CuboMagico::printCube(){
    printf("Estado atual do cubo: \n\n");
    printf("      %c %c %c\n", matrizCores[4][8], matrizCores[4][3], matrizCores[4][7]);
    printf("      %c %c %c\n", matrizCores[4][4], matrizCores[4][0], matrizCores[4][2]);
    printf("      %c %c %c\n", matrizCores[4][5], matrizCores[4][1], matrizCores[4][6]);
    printf("      -----\n");
    printf("%c %c %c|", matrizCores[5][8], matrizCores[5][3], matrizCores[5][7]);
    printf("%c %c %c|", matrizCores[0][8], matrizCores[0][3], matrizCores[0][7]);
    printf("%c %c %c|", matrizCores[2][8], matrizCores[2][3], matrizCores[2][7]);
    printf("%c %c %c\n", matrizCores[3][8], matrizCores[3][3], matrizCores[3][7]);
    printf("%c %c %c|", matrizCores[5][4], matrizCores[5][0], matrizCores[5][2]);
    printf("%c %c %c|", matrizCores[0][4], matrizCores[0][0], matrizCores[0][2]);
    printf("%c %c %c|", matrizCores[2][4], matrizCores[2][0], matrizCores[2][2]);
    printf("%c %c %c \n", matrizCores[3][4], matrizCores[3][0], matrizCores[3][2]);
    printf("%c %c %c|", matrizCores[5][5], matrizCores[5][1], matrizCores[5][6]);
    printf("%c %c %c|", matrizCores[0][5], matrizCores[0][1], matrizCores[0][6]);
    printf("%c %c %c|", matrizCores[2][5], matrizCores[2][1], matrizCores[2][6]);
    printf("%c %c %c \n", matrizCores[3][5], matrizCores[3][1], matrizCores[3][6]);
    printf("      -----\n");
    printf("      %c %c %c\n", matrizCores[1][8], matrizCores[1][3], matrizCores[1][7]);
    printf("      %c %c %c\n", matrizCores[1][4], matrizCores[1][0], matrizCores[1][2]);
    printf("      %c %c %c\n", matrizCores[1][5], matrizCores[1][1], matrizCores[1][6]);
    printf("\n");
}

void CuboMagico::printPecas(){
    int i;
    for(i=0; i<12; i++) printf("aresta %d: %c %c\n", i, pecas[i].cor[0], pecas[i].cor[1]);
    for(; i<20; i++) printf("quina %d (peça %d): %c %c %c\n", i-11, i, pecas[i].cor[0], pecas[i].cor[1], pecas[i].cor[2]);
}

double **CuboMagico::oldStateToBinaryMatrix(){
    for(int i=0; i<6; i++){
        for(int j=1; j<9; j++){
            // printf("%c %d %d\t", matrizCores[i][j], i, j);
            switch (matrizCores[i][j]){
                case 'w':
                    binaryMatrix[0][(j-1)*6+i*48]=1.0;
                    binaryMatrix[0][(j-1)*6+1+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+2+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+3+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+4+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+5+i*48]=0.0;
                    break;
                case 'g':
                    binaryMatrix[0][(j-1)*6+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+1+i*48]=1.0;
                    binaryMatrix[0][(j-1)*6+2+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+3+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+4+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+5+i*48]=0.0;
                    break;
                case 'r':
                    binaryMatrix[0][(j-1)*6+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+1+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+2+i*48]=1.0;
                    binaryMatrix[0][(j-1)*6+3+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+4+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+5+i*48]=0.0;
                    break;
                case 'y':
                    binaryMatrix[0][(j-1)*6+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+1+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+2+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+3+i*48]=1.0;
                    binaryMatrix[0][(j-1)*6+4+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+5+i*48]=0.0;
                    break;
                case 'b':
                    binaryMatrix[0][(j-1)*6+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+1+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+2+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+3+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+4+i*48]=1.0;
                    binaryMatrix[0][(j-1)*6+5+i*48]=0.0;
                    break;
                case 'o':
                    binaryMatrix[0][(j-1)*6+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+1+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+2+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+3+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+4+i*48]=0.0;
                    binaryMatrix[0][(j-1)*6+5+i*48]=1.0;
                    break;
                default:
                    break;
            }
        }
    }
    return binaryMatrix;
}

double **CuboMagico::stateToBinaryMatrix(){
    for(int i=0; i<6; i++){
        for(int j=1; j<9; j++){
            // printf("%c %d %d\t", matrizCores[i][j], i, j);
            switch (matrizCores[i][j]){
                case 'w':
                    binaryMatrix[0][(j-1)*3+i*24]=0.0;
                    binaryMatrix[0][(j-1)*3+1+i*24]=0.0;
                    binaryMatrix[0][(j-1)*3+2+i*24]=0.1;
                    break;
                case 'g':
                    binaryMatrix[0][(j-1)*3+i*24]=0.0;
                    binaryMatrix[0][(j-1)*3+1+i*24]=1.0;
                    binaryMatrix[0][(j-1)*3+2+i*24]=0.0;
                    break;
                case 'r':
                    binaryMatrix[0][(j-1)*3+i*24]=0.0;
                    binaryMatrix[0][(j-1)*3+1+i*24]=1.0;
                    binaryMatrix[0][(j-1)*3+2+i*24]=1.0;
                    break;
                case 'y':
                    binaryMatrix[0][(j-1)*3+i*24]=1.0;
                    binaryMatrix[0][(j-1)*3+1+i*24]=0.0;
                    binaryMatrix[0][(j-1)*3+2+i*24]=0.0;
                    break;
                case 'b':
                    binaryMatrix[0][(j-1)*3+i*24]=1.0;
                    binaryMatrix[0][(j-1)*3+1+i*24]=0.0;
                    binaryMatrix[0][(j-1)*3+2+i*24]=1.0;
                    break;
                case 'o':
                    binaryMatrix[0][(j-1)*3+i*24]=1.0;
                    binaryMatrix[0][(j-1)*3+1+i*24]=1.0;
                    binaryMatrix[0][(j-1)*3+2+i*24]=0.0;
                    break;
                default:
                    break;
            }
        }
    }
    binaryMatrix[0][144] = (double)pecasNoLugar();
    binaryMatrix[0][145] = (double)pecasOrientadasNoLugar();
    return binaryMatrix;
}