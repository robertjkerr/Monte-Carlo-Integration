//***********************************************************
// Memory management methods needed for type defs in types.h
//***********************************************************

#include <stdlib.h>
#include <stdio.h>
#include "types.h"

//Returns pointer for dynamic int array
int** imatrix(int rows, int columns) {
    int *ptr, **arr;
    int len, i;

    len = sizeof(int *) * rows + sizeof(int) * columns * rows;
    arr = (int**) malloc(len);
    ptr = (int*)(arr + rows);

    for (i = 0; i < rows; i++) {
        arr[i] = (ptr + columns * i);
    }

    return arr;
}

//Returns pointer for dynamic double array
double** dmatrix(int rows, int columns) {
    double *ptr, **arr;
    int len, i;

    len = sizeof(double *) * rows + sizeof(double) * columns * rows;
    arr = (double**) malloc(len);
    ptr = (double *)(arr + rows);

    for (i = 0; i < rows; i++) {
        arr[i] = (ptr + columns * i);
    }

    return arr;
}

//Tool which prints 2D array
void printmat(Matrix *m) {

    int **mat;
    int r, c, rows, columns;

    mat = m->mat;
    rows = m->rows;
    columns = m->columns;

    for (r = 0; r < rows; r++) {
        for (c = 0; c < columns; c++) {
            printf("%d ", mat[r][c]);
        }
        printf("\n");
    }
}