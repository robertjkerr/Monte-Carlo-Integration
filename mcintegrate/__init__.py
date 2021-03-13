# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:19:31 2021

@author: Robert Kerr

Python library for Monte Carlo numerical integration

Function `integrate` argument specifications for a d-th integral (1: single, 2: double, 3: triple, ...):
    (Function to be integrated) f must have d arguments. Recommend f = lambda *q: ...
    (Number of iterations) n must be a positive integer.
    (Limits) lims must be a list with d elements. Each element (a pair of limits) must have 2 subelements.
        Limits can be either numbers or functions, but if functions must be ordered in terms of dependencies
        If a function, limit must also have d arguments.
"""

from numpy.random import uniform as __random
from numpy import array as __array
import mcintegrate.limitInit as __limInit


"""
    `__throw` places a point randomly on n-dimensional space within defined limits
    `__scatter` gathers an array of throws onto space within maximum limits i.e. rectangle, cuboid etc
    `__fMap` maps all throws with f(x)
"""

__throw = lambda lims: __array([float(__random(*l,[1])) for l in lims])
__scatter = lambda n,lims : __array([__throw(lims) for i in range(n)])
__fMap = lambda f,throws : __array([f(*p) for p in throws])


"""
    `__filterScatter` filters a scatter onto the real limits e.g. circle
    `__absInt` finds the integral (area, volume etc) of the maximum limits
    `integrate` finds the Monte Carlo integral of a function f within limits (lims) over n iterations
"""

def __filterScatter(throws,lims):
    scatter = []
    for throw in throws:
        if __limInit.throwCheck(throw,lims):
            scatter.append(throw)
    return scatter

def __absInt(absLims):
    out = 1
    for l in absLims:
        out = out*(l[1]-l[0])
    return out

def integrate(f,n,lims):
    absLims = __limInit.getAbsLims(n,lims)
    scatter = __scatter(n,absLims)
    newScatter = __filterScatter(scatter,lims)
    fMapping = __fMap(f, newScatter)
    return __absInt(absLims)*sum(fMapping)/len(scatter)