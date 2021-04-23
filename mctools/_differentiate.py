"""
Forked from 'RobertK20/Monte-Carlo-Integration' on 23/04/2021

@author: Robert Kerr

Differentiation functions
"""

import numpy as _np

"""
    `partialDiff` returns partial derivative.
    `grad` returns grad of a function
    `differentiate` returns directional derivative
"""

def partialDiff(f,position,axis,dimensions,delta):
    unitVect = _np.zeros(dimensions)
    unitVect[axis] = 1
    return (f(*(position + delta*unitVect)) - f(*position))/delta
            
def grad(f,position,dimensions,delta):
    grad = []
    for axis in range(dimensions):
        grad.append(partialDiff(f,position,axis,dimensions,delta))
    return _np.array(grad)

def directDiff(f,position,direction,delta):
    unitDir = _np.array(direction)/_np.linalg.norm(direction)
    return _np.dot(unitDir,grad(f,position,len(list(direction)),delta))