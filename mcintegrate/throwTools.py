# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:21:58 2021

@author: RobertKerr
"""

from numpy.random import uniform as __random
import numpy as np

"""
    `__testType` checks if input is a number or (by assumption) a function
    `__throwCheck` checks if throw is within limits
    `__throw` throws point randomly onto space of size boxSize^d
    `__scatter` throws n throws into the same space
    `__filterScatter` filters out all throws in scatter not within limits
    `__fMap` applies function f to all points in scatter
    `boxSample` returns a scatter and its f mapping
"""

def __testType(l):
    return isinstance(l,int) or isinstance(l,float)

def __throwCheck(throw,lims):
    d = len(lims)
    for i in range(d):#Check each dimension
        l = lims[i]
        if __testType(l[0]):#Find lower limit
            a = l[0]
        else:
            a = l[0](*throw)
        
        if __testType(l[1]):#Find upper limit
            b = l[1]
        else:
            b = l[1](*throw)
        
        if throw[i]>=b or throw[i]<=a:#Check limits
            return False
    return True

def __throw(corner, boxSize, dimensions):
    throw = [float(__random(corner[d]*boxSize, (corner[d]+1)*boxSize)) for d in range(dimensions)]
    return np.array(throw)

def __scatter(corner, boxSize, dimensions, n):
    scatter = [__throw(corner,boxSize,dimensions) for i in range(n)]
    return np.array(scatter)

def __filterScatter(scatter,lims):
    outScatter = []
    for throw in scatter:
        if __throwCheck(throw,lims):
            outScatter.append(throw)
    return np.array(outScatter)

def __fMap(f, scatter):
    return [f(*throw) for throw in scatter]

def boxSample(f, corner,boxSize,n,lims):
    scatter = __filterScatter(__scatter(corner, boxSize, len(lims), n),lims)
    fMapping = sum(__fMap(f, scatter))
    return len(scatter), fMapping

