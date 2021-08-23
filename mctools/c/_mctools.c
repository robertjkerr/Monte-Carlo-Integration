#include <Python.h>
#include <time.h>

#include "_functions.h"

//Python methods
static PyMethodDef mctools_methods[] = {
    {"scatter", c_scatter, METH_VARARGS, "Gets scatter within a box."},
    {"getCombinations", c_getCombinations, METH_VARARGS, "Finds combinations of boxes at radius"},
    {NULL, NULL, 0, NULL}
};

//Python module definitions
static struct PyModuleDef mctoolsMethods = {
    PyModuleDef_HEAD_INIT,
    "mctoolsMethods",
    "Scatter tools for robertjkerr/Monte-Carlo-Math-Tools",
    -1,
    mctools_methods
};

//Python init function definition
PyMODINIT_FUNC PyInit_mctoolsScatter(void) {
    return PyModule_Create(&mctoolsMethods);
}