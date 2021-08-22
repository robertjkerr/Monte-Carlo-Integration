#include <stdio.h>
#include <stdlib.h>

//Returns pointer for dynamic double array
double ** dmatrix(int r, int c) {
    double *ptr, **arr;
    int len, i;

    len = sizeof(double *) * r + sizeof(double) * c * r;
    arr = (double**) malloc(len);
    ptr = (double *)(arr + r);

    for (i = 0; i < r; i++) {
        arr[i] = (ptr + c * i);
    }

    return arr;
}

//Returns pointer for dynamic int array
int ** imatrix(int r, int c) {
    int *ptr, **arr;
    int len, i;

    len = sizeof(int *) * r + sizeof(int) * c * r;
    arr = (int**) malloc(len);
    ptr = (int*)(arr + r);

    for (i = 0; i < r; i++) {
        arr[i] = (ptr + c * i);
    }

    return arr;
}

//Range function similar to that of the Python range function.
int * range(int start, int finish) {
    int i, *ptr;
    const int diff = finish - start;
    ptr = (int*) malloc(diff * sizeof(int));
    for (i = 0; i < diff; i++) {
        ptr[i] = start + i;
    }
    return ptr;

}

//Cartesian product function. Find cartesian product of set1 and set2
int ** product(int ** set1, int set1_elems, int set1_dims, int ** set2, int set2_elems, int set2_dims) {
    int columns = set1_dims + set2_dims;
    int rows = set1_elems * set2_elems; 
    int i, j, offset, **arr;
    int d1, d2;

    arr = imatrix(rows, columns);

    for (i = 0; i < set1_elems; i++) {
        offset = i * set2_elems;
        for (j = 0; j < set2_elems; j++) {
            for (d1 = 0; d1 < set1_dims; d1++)
                arr[offset + j][d1] = set1[i][d1];
            for (d2 = 0; d2 < set2_dims; d2++)
                arr[offset + j][d2 + set1_dims] = set2[j][d2];
        }
    }

    return arr;
}

//Gets the upper and lower limits in each dimension at a given radius from the start point
int ** extrema(int dimensions, int r, int * start)
{
    int d, high, low, **arr = imatrix(dimensions, 2);
    for (d = 0; d < dimensions; d++) {
        arr[d][1] = r + start[d];
        arr[d][0] = -r + start[d];
    } 

   return arr; 
}

//Debugging tool which prints 2D array
void printmat(int ** mat, int rows, int columns) {
    int r, c;
    for (r = 0; r < rows; r++) {
        for (c = 0; c < columns; c++) {
            printf("%d ", mat[r][c]);
        }
        printf("\n");
    }
}