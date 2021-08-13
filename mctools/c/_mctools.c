#include <Python.h>
#include <stdlib.h>
#include <time.h>
#include "src/scatter.h"

//Converts double matrix into Python tuple
PyObject* build_tuple(double **mat, int r, int c) {
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

//Scatter function wrapper
static PyObject* c_scatter(PyObject *self, PyObject *args) {

    int *corner, dimensions, n, i;
    double boxSize;
    PyObject *cornerList, *cornerItem;
    Py_ssize_t d;

    if (!PyArg_ParseTuple(args, "O!dii", &PyList_Type, &cornerList, &boxSize, &dimensions, &n)){
        return NULL;
    }

    d = PyList_Size(cornerList);
    corner = (int*) malloc(dimensions * sizeof(int));
    for (i =  0; i < d; i++) {
        cornerItem = PyList_GetItem(cornerList, i);
        /*if (!PyInt_Check(cornerItem)) {
            PyErr_SetString(PyExc_TypeError, "Corner must be integer list.");
            return NULL;
        }*/
        corner[i] = (int) PyLong_AsLong(cornerItem);
    }

    srand(time(0));
    double **scatter_mat = scatter(corner, boxSize, dimensions, n);
    return build_tuple(scatter_mat, n, dimensions);

} 

//Python methods
static PyMethodDef scatter_methods[] = {
    {"scatter", c_scatter, METH_VARARGS, "Gets scatter within a box."},
    {NULL, NULL, 0, NULL}
};

//Python module definitions
static struct PyModuleDef mctoolsScatter = {
    PyModuleDef_HEAD_INIT,
    "mctoolsScatter",
    "Scatter tools for robertjkerr/mctools",
    -1,
    scatter_methods
};

//Python init function definition
PyMODINIT_FUNC PyInit_mctoolsScatter(void) {
    return PyModule_Create(&mctoolsScatter);
}