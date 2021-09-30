"""
@author: Robert Kerr

Differentiation functions
"""

import numpy as _np

"""
    `partial_diff` returns partial derivative.
    `grad` returns grad of a function
    `differentiate` returns directional derivative
"""

def partial_diff(f,position,axis,dimensions,delta):
    unit_vect = _np.zeros(dimensions)
    unit_vect[axis] = 1
    return (f(*(position + delta*unit_vect)) - f(*position))/delta
            
def grad(f,position,dimensions,delta):
    grad = []
    for axis in range(dimensions):
        grad.append(partial_diff(f,position,axis,dimensions,delta))
    return _np.array(grad)

def direct_diff(f,position,direction,delta):
    unit_dir = _np.array(direction)/_np.linalg.norm(direction)
    return _np.dot(unit_dir,grad(f,position,len(list(direction)),delta))

def div(F, position, delta):
    divList = []
    for d in range(len(F)):
        divList.append(partial_diff(F[d], position, d, len(F), delta))
    return sum(divList)
        
