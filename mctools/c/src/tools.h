#ifndef MCTOOLS_TOOLS_H
#define MCTOOLS_TOOLS_H

#include "types.h"

int* range(int start, int finish);
int** extrema(int dimensions, int r, int * start);
Matrix* product(Matrix *set1, Matrix *set2);

#endif //MCTOOLS_TOOLS_H