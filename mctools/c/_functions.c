#include <Python.h>

#include "src/scatter.h"
#include "src/allocate.h"

//Converts double matrix into Python tuple
PyObject* build_dtuple(double **mat, int r, int c) {
    Py_ssize_t lenr = r, lenc = c;
    PyObject *tuple_out = PyTuple_New(lenr);
    for (Py_ssize_t row = 0; row < lenr; row++) {
        PyObject *elem = PyTuple_New(c);
        for (Py_ssize_t column = 0; column < lenc; column++) {
            PyTuple_SET_ITEM(elem, column, PyFloat_FromDouble(mat[row][column]));
        }
        PyTuple_SET_ITEM(tuple_out, row, elem);
    }
    return tuple_out;
}

//Converts double matrix into Python tuple
PyObject* build_ituple(int **mat, int r, int c) {
    Py_ssize_t lenr = r, lenc = c;
    PyObject *tuple_out = PyTuple_New(lenr);
    for (Py_ssize_t row = 0; row < lenr; row++) {
        PyObject *elem = PyTuple_New(c);
        for (Py_ssize_t column = 0; column < lenc; column++) {
            PyTuple_SET_ITEM(elem, column, PyLong_FromLong((long) mat[row][column]));
        }
        PyTuple_SET_ITEM(tuple_out, row, elem);
    }
    return tuple_out;
}

//Scatter function wrapper
static PyObject* c_scatter(PyObject *self, PyObject *args) {

    int *corner, dimensions, n, i;
    double boxSize;
    PyObject *cornerList, *cornerItem;
    Py_ssize_t d;

    //Parse args
    if (!PyArg_ParseTuple(args, "O!dii", &PyList_Type, &cornerList, &boxSize, &dimensions, &n)){
        return NULL;
    }

    //Create array from input list
    d = PyList_Size(cornerList);
    corner = (int*) malloc(dimensions * sizeof(int));
    for (i =  0; i < d; i++) {
        cornerItem = PyList_GetItem(cornerList, i);
        corner[i] = (int) PyLong_AsLong(cornerItem);
    }

    //Make scatter
    srand(time(0));
    double **scatter_mat = scatter(corner, boxSize, dimensions, n);
    PyObject *out_tuple = build_dtuple(scatter_mat, n, dimensions);
    free(scatter_mat);
    free(corner);
    return out_tuple;
}

//Get combinations function wrapper
static PyObject* c_getCombinations(PyObject *self, PyObject *args) {

    int *start, r, dimensions, i;
    PyObject *startList, *startItem;
    Py_ssize_t d;

    //Parse args
    if (!PyArg_ParseTuple(args, "O!ii", &PyList_Type, &startList, &r, &dimensions)) {
        return NULL;
    }

    //Create array from input list
    d = PyList_Size(startList);
    start = (int*) malloc(dimensions * sizeof(int));
    for (i = 0; i < d; i++) {
        startItem = PyList_GetItem(startList, i);
        start[i] = (int) PyLong_AsLong(startItem);
    }

    //Find combinations
    int **thisExtrema = extrema(dimensions, r, start);
    int **combinations = getCombinations(thisExtrema, dimensions, r);
    int n = (int) pow(2*r + 1, dimensions);
    PyObject *out_tuple = build_ituple(combinations, n, dimensions);
    free(thisExtrema);
    free(combinations);
    return out_tuple;
}