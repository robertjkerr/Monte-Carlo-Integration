#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "tools.h"

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
            set1[i][1] = QArr[i][0];
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

    return out_set;
}


int main() {
    int dimensions = 3;
    int r = 3;
    int start[] = {1, 5, -1};
    int **extremaArr = extrema(dimensions, r, start);
    const int length = 2*r+1;
    const int num_combs = (int) pow(length, dimensions); 

    int **combs = getCombinations(extremaArr, dimensions, r);

    printmat(combs, num_combs, dimensions); 

    
    return 0;

}
