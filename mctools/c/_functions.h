#ifndef MCTOOLS__FUNCTIONS_H
#define MCTOOLS__FUNCTIONS_H

#include <Python.h>

PyObject* build_dtuple(double **mat, int r, int c);
PyObject* build_ituple(int **mat, int r, int c);
static PyObject* c_scatter(PyObject *self, PyObject *args);
static PyObject* c_getCombinations(PyObject *self, PyObject *args);

#endif //MCTOOLS__FUNCTIONS_H