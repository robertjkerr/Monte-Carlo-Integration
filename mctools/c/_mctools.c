#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <time.h>
#include "src/scatter.h"

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
}

static PyObject* c_scatter(PyObject *self, PyObject *args) {

    int *corner, dimensions, n;
    double boxSize;

    if (!PyArg_ParseTuple(args, "idii", &corner, &boxSize, &dimensions, &n)){
        return NULL;
    }

    double **scatter_mat = scatter(corner, boxSize, dimensions, n);
    return build_tuple(scatter_mat, n, dimensions);

} 

static PyMethodDef scatter_methods[] = {
    {"scatter", c_scatter, METH_VARARGS, "Gets scatter within a box."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mctoolsScatter = {
    PyModuleDef_HEAD_INIT,
    "mctoolsScatter",
    "Scatter tools for robertjkerr/mctools",
    -1,
    scatter_methods
};

PyMODINIT_FUNC PyInit_mctoolsScatter(void) {
    return PyModule_Create(&mctoolsScatter);
}