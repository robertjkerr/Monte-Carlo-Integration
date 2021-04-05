# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 01:05:24 2021

@author: RobertKerr

Numerical multidimensional differentiation tools to supplement Monte-Carlo Integration
"""

import numpy as __np

"""
    `partialDiff` returns partial derivative. 'axis' is the direction and must be a natural number and 'dimensions' is total number of dimensions
    `grad` returns grad of a function
    `differentiate` returns directional derivative
"""

def partialDiff(f,position,axis,dimensions,delta):
    unitVect = __np.zeros(dimensions)
    unitVect[axis] = 1
    return (f(*(position + delta*unitVect)) - f(*position))/delta
            

def grad(f,position,dimensions,delta):
    grad = []
    for axis in range(dimensions):
        grad.append(partialDiff(f,position,axis,dimensions,delta))
    return __np.array(grad)


def differentiate(f,position,direction,delta):
    unitDir = __np.array(direction)/__np.linalg.norm(direction)
    return __np.dot(unitDir,grad(f,position,len(list(direction)),delta))