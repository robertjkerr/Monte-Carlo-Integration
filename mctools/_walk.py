"""
Created on 23/04/2021

@author: Robert Kerr

Random walk tools
"""

import numpy as _np
import sys

"""
    `_randUnitVect` returns a unit vector in `dimensions` number of dimensions in a random direction
    `walk` returns the end point of a particle of a random walk starting from `start` moving along `iters` number of steps of `delta` length
"""

def _randUnitVect(dimensions):
    vect = _np.random.uniform(-1,1,dimensions)
    norm = _np.linalg.norm(vect)
    if norm==0:
        return _np.zeros(dimensions)
    else:
        return vect/norm

def walk(start,delta,iters):
    newPos = _np.array(start)+delta*_randUnitVect(len(start))
    if iters > 0: 
        return walk(newPos,delta,iters-1)
    else:
        return start