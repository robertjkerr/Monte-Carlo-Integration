#ifndef MCTOOLS_TOOLS_H
#define MCTOOLS_TOOLS_H

int * range(int start, int finish);
int ** product(int ** set1, int elems1, int dims1, int ** set2, int elems2, int dims2);
double ** dmatrix(int r, int c);
int ** imatrix(int r, int c);
int ** extrema(int dimensions, int r, int * start);
void printmat(int ** mat, int rows, int columns);

#endif //MCTOOLS_TOOLS_H