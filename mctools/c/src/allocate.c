#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "tools.h"

/*
struct Boxes {
    int **arr;
    int amount;
};
*/

//Gets all the combinations within some extrema
int ** getCombinations(int ** extrema, int dimensions, int r) {
    const int length = 2*r + 1;
    int **QArr = imatrix(length, dimensions);
    int d, *extremum, *Qs, pos; 
    int **set1 = imatrix(length, 1), **set2 = imatrix(length, 1);
    int **out_set = imatrix((int) pow(length, dimensions), dimensions);
    int **running_set = imatrix(length, 1);
    int i, j;
    
    //Make the sets along each dimension that need a cartesian product
    for (d = 0; d < dimensions; d++) {
        extremum = extrema[d];
        Qs = range(extremum[0], extremum[1]+1);

        for (pos = 0; pos < length; pos++) {
           QArr[pos][d] = Qs[pos]; 
        }
    } 

    //Build cartesian product
    switch (dimensions) {
    case 1: //Single dimension case
        out_set = QArr;
        break;

    case 2: //Two dimension case
        for (i = 0; i < length; i++) {
            set1[i][0] = QArr[i][0];
            set2[i][0] = QArr[i][1];
        }
        out_set = product(set1, length, 1, set2, length, 1);
        break;

    default: //n dimension case
        for (i = 0; i < length; i++) {
            set1[i][0] = QArr[i][0];
            set2[i][0] = QArr[i][1];
        }
        out_set = product(set1, length, 1, set2, length, 1);

        for (d = 2; d < dimensions; d++) {
            for (i = 0; i < length; i++) {
                running_set[i][0] = QArr[i][d];
            }
            out_set = product(out_set, (int) pow(length, d), d, running_set, length, 1);
        }
        break; 
    }

    free(set1);
    free(set2);
    free(Qs);
    free(QArr);
    return out_set;
}

/*
//Returns all the boxes at a certain radius from start
struct Boxes getBoxes(int r0, int dimensions, int * start) {
    int **combinations, **combinationsInner;
    int **extrema1 = extrema(dimensions, r0, start), **extrema2;
    int row1, row2, column, elems1, elems2;
    int count = 0, runningState, firstElem, secondElem;
    int **out_set, index = 0;
    const int length = 2*r0 + 1;
    struct Boxes boxes;

    if (r0 > 0) { //Case beyond origin. Inside combinations found to be removed from output set
        extrema2 = extrema(dimensions, r0-1, start);

        combinations = getCombinations(extrema1, dimensions, r0);
        combinationsInner = getCombinations(extrema2, dimensions, r0-1);

        free(extrema1);
        free(extrema2);
        
        elems1 = (int) pow(length, dimensions);
        elems2 = (int) pow(length - 2, dimensions);
        
        //Number of unique elements now known 
        const int elems = elems1 - elems2;
        out_set = imatrix(elems , dimensions);

        //Add unique elements to output array
        count = 0;
        for (row1 = 0; row1 < elems1; row1++) {
            for (row2 = 0; row2 < elems2; row2++) {
                runningState = 0;
                for (column = 0; column < dimensions; column++) {
                    firstElem = combinations[row1][column];
                    secondElem = combinationsInner[row2][column];
                    if (firstElem == secondElem)
                        runningState = 1;
                }
            }

            if (runningState == 0) {
                index++;
                for (column = 0; column < dimensions; column++) {
                    out_set[index][column] = combinations[row1][column];
                }
            } 
        }
        
        free(combinations);
        free(combinationsInner);
        boxes.arr = out_set;
        boxes.amount = elems;
    }
    else { //Origin case. No inside combinations
        out_set = getCombinations(extrema1, dimensions, 0);
        free(extrema1);
        boxes.arr = out_set;
        boxes.amount = 1;
    }

    return boxes;
}


//Returns boxes at a radius allocated into cores. Indices are {core, box, dimension}
int *** allocate(int cores, int r, int dimensions, int * start) {

}



int main() {
    int dimensions = 2;
    int r = 3;
    int start[] = {1, 5};
    const int length = 2*r+1;
    const int num_combs = (int) pow(length, dimensions);
    int ** thisExtrema = extrema(dimensions,r,start);

    struct Boxes boxes = getBoxes(r, dimensions, start);

    int ** mat = boxes.arr;
    printmat(mat, boxes.amount, dimensions);
    



    
    return 0;

}
*/