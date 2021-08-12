#include <stdlib.h>
#include <stdio.h>
#include "tools.h"

double * throw(int * corner, double boxSize, int dimensions) {
    double elem, adjusted, * throwElems = (double*) malloc(dimensions*sizeof(double));
    int d;
    for (d = 0; d < dimensions; d++) {
        elem = (double) rand() / RAND_MAX;
        adjusted = boxSize * ((double) corner[d] + elem);
        throwElems[d] = adjusted;
    }
    return throwElems;
}

double ** scatter(int * corner, double boxSize, int dimensions, int n) {
    double *thisThrow, **mat = dmatrix(n, dimensions);
    int i, d;
    for (i = 0; i < n; i++) {
        thisThrow = throw(corner, boxSize, dimensions);
        for (d = 0; d < dimensions; d++) {
            mat[i][d] = thisThrow[d];
        }
    }
    return mat;
}