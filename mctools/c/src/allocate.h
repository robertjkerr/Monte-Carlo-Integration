#ifndef MCTOOLS_ALLOCATE_H
#define MCTOOLS_ALLOCATE_H

int ** extrema(int dimensions, int r, int * start);
int **getCombinations(int ** extrema, int dimensions, int r); 
//int *** allocate(int cores, int r, int dimensions, int * start);

#endif //MCTOOLS_ALLOCATE_H