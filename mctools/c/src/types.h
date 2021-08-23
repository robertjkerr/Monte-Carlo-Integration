//***************************************************
// Type defs and structs useful in many functions
//***************************************************

#ifndef MCTOOLS_TYPES_H
#define MCTOOLS_TYPES_H


//Type for matrix. Note only applies to integer matrices
typedef struct Matrices {
    int **mat;
    int rows;
    int columns;
} Matrix;

//Structure for boxes allocated each core
struct Boxes {
    int ***boxes;
    int cores;
    int dimensions;
    int *numBoxes; 
};

int** imatrix(int rows, int columns);
double** dmatrix(int rows, int columns);
void printmat(Matrix *mat);

#endif //MCTOOLS_TYPES_H