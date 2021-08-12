#include <stdio.h>
#include <stdlib.h>

//Returns pointer for dynamic double array
double ** dmatrix(int r, int c)
{
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
int ** imatrix(int r, int c)
{
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
int * range(int start, int finish)
{
    int i, *ptr;
    const int diff = finish - start;
    ptr = (int*) malloc(diff * sizeof(int));
    for (i = 0; i < diff; i++) {
        ptr[i] = start + i;
    }
    return ptr;

}

//Cartesian product function. Find cartesian product of set1 and set2
int ** product(int ** set1, int set1_length, int set1_width, int ** set2, int set2_length, int set2_width)
{
    int r = set1_length * set2_length;
    int c = set1_width + set2_width;
    int i, j, offset, **arr;
    int d1, d2;

    arr = imatrix(r, c);

    for (i = 0; i < set1_length; i++)
    {
        for (j = 0; j < set2_length; j++)
        {
            offset = i * set2_length;
            for (d1 = 0; d1 < set1_width; d1++)
                arr[offset + j][d1] = set1[i][d1];
            for (d2 = set1_width; d2 < set1_width + set2_width; d2++)
                arr[offset + j][d2] = set2[j][d2-set1_width];
        }
    }

    return arr;
}

/*
int ** extrema(int dimensions, int r, int * start)
{
    int len, c = 2, rows = dimensions;
    int *ptr, **arr;
    int i, j;

    len = sizeof(int *) * rows + sizeof(int) * c * rows;
    arr = (int **) malloc(len);
    ptr = (int *)(arr + rows);

    for (i = 0; i < r; i++) {
        arr[i] = (ptr + c * i);
    }
}
*/
