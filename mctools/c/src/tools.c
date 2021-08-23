//****************************************************
// Useful methods for generic tasks
//****************************************************

#include <stdio.h>
#include <stdlib.h>
#include "types.h"

//Range function similar to that of the Python range function.
int* range(int start, int finish) {
    int i, *ptr;
    const int diff = finish - start;
    ptr = (int*) malloc(diff * sizeof(int));
    for (i = 0; i < diff; i++) {
        ptr[i] = start + i;
    }
    return ptr;

}

//Gets the upper and lower limits in each dimension at a given radius from the start point
int** extrema(int dimensions, int r, int * start)
{
    int d, high, low, **arr = imatrix(dimensions, 2);
    for (d = 0; d < dimensions; d++) {
        arr[d][1] = r + start[d];
        arr[d][0] = -r + start[d];
    } 

   return arr; 
}

//Detemines cartesian product of two sets, where a row of each matrix corresponds to an element
Matrix* product(Matrix *set1, Matrix *set2) {

    int **mat1, **mat2, **out_mat;
    int elems1, elems2, dims1, dims2;
    int rows, columns;
    int elem1, elem2, offset, i;

    //Get input matrix properties
    mat1 = set1->mat;
    mat2 = set2->mat;
    dims1 = set1->columns;
    dims2 = set2->columns;
    elems1 = set1->rows;
    elems2 = set2->rows;

    //Init output matrix
    rows = elems1 * elems2;
    columns = dims1 + dims2;
    out_mat = imatrix(rows, columns); 

    //Construct product
    for (elem1 = 0; elem1 < elems1; elem1++) {
        offset = elem1 * elems2;
        for (elem2 = 0; elem2 < elems2; elem2++) {

            for (i = 0; i < dims1; i++)
                out_mat[offset + elem2][i] = mat1[elem1][i];
            for (i = 0; i < dims2; i++)
                out_mat[offset + elem2][i + dims1] = mat2[elem2][i];
        }
    }

    //Create output matrix
    Matrix* output;
    output->rows = rows;
    output->columns = columns;
    output->mat = out_mat;
    return output;
}


//Counts number of common rows
int countCommonRows(Matrix *m1, Matrix *m2) {

    int **mat1, **mat2;
    int elems1, elems2, row1, row2;
    int columns, column, firstElem, secondElem;
    int runningState, count = 0;

    //Get number of columns and check each matrix has the same
    columns = m1->columns;
    if (columns != m2->columns) {
        printf("Matrices have unequal number of columns.");
        return 0;
    }

    //Get row and pointer data
    mat1 = m1->mat;
    mat2 = m2->mat;
    elems1 = m1->rows;
    elems2 = m2->rows;

    //Check for identical rows
    for (row1 = 0; row1 < elems1; row1++) {
        runningState = 0;
        for (row2 = 0; row2 < elems2; row2++) {
            for (column = 0; column < columns; column++) {
                firstElem = mat1[row1][column];
                secondElem = mat2[row2][column];

                if (firstElem == secondElem)
                    runningState = 1; 
            }
        }

        if (runningState = 1)
            count++;
    }

    return count;
}
