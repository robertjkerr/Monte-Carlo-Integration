#include <stdlib.h>
#include "tools.h"

//Creates array of `dimensions` dimensions of random quantities within box of `boxSize` size at corner
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

//Creates array of throws
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