# -*- coding: utf-8 -*-
"""
@author: Robert Kerr

Monte Carlo Integration function 
"""

import numpy as _np
from itertools import product as _product

"""
Throw tools. Used for Monte Carlo random throwing.

    `_testType` checks if input is a number or (by assumption) a function
    `_throwCheck` checks if throw is within limits
    `_throw` throws point randomly onto space of size boxSize^d
    `_scatter` throws n throws into the same space
    `_filterScatter` filters out all throws in scatter not within limits
    `_fMap` applies function f to all points in scatter
    `_boxSample` returns a scatter and its f mapping
"""

def _testType(l):
    return isinstance(l,int) or isinstance(l,float)

def _throwCheck(throw,lims):
    d = len(lims)
    for i in range(d):#Check each dimension
        l = lims[i]
        if _testType(l[0]):#Find lower limit
            a = l[0]
        else:
            a = l[0](*throw)
        
        if _testType(l[1]):#Find upper limit
            b = l[1]
        else:
            b = l[1](*throw)
        
        if throw[i]>=b or throw[i]<=a:#Check limits
            return False
    return True

def _throw(corner, boxSize, dimensions):
    throw = [float(_np.random.uniform(corner[d]*boxSize, (corner[d]+1)*boxSize)) for d in range(dimensions)]
    return _np.array(throw)

def _scatter(corner, boxSize, dimensions, n):
    scatter = [_throw(corner,boxSize,dimensions) for i in range(n)]
    return _np.array(scatter)

def _filterScatter(scatter,lims):
    outScatter = []
    for throw in scatter:
        if _throwCheck(throw,lims):
            outScatter.append(throw)
    return _np.array(outScatter)

def _fMap(f, scatter):
    return [f(*throw) for throw in scatter]

def _boxSample(f, corner,boxSize,n,lims):
    scatter = _filterScatter(_scatter(corner, boxSize, len(lims), n),lims)
    fMapping = sum(_fMap(f, scatter))
    return len(scatter), fMapping



"""
Allocation subroutines. Assist with parallelisation.

    `_getCombinations` gets all vectors within limits defined by extrema
    `_oneNorm` gets the one-norm of a vector
    `_getBoxes` gets all combinations of vectors within extrema that have the same one-norm
    `allocate` gets all vectors returned by _getBoxes and divides them into sublists for each core
"""

def _getCombinations(extrema):
    QList = []
    for d in extrema:
        QList.append(list(range(d[0],d[1]+1)))
    return list(_product(*QList))

def _oneNorm(start,vector):
    diff = _np.array(vector) - _np.array(start)
    return sum(abs(diff)) 

def _getBoxes(r, dimensions,start):
    extrema = [[-r,r] for i in range(dimensions)]
    combinations = _getCombinations(extrema)
    return [combination for combination in combinations if _oneNorm(start,combination) == r]

def _allocate(cores, r, dimensions, start):
    boxes = _getBoxes(r, dimensions, start)
    boxList = [[] for i in range(cores)]
    for b in range(len(boxes)):
        box = boxes[b]
        pool = b%cores
        boxList[pool].append(box)
    return boxList



"""
Integration subroutines. Main functions for performing integration.

    `_intBoxes` integrates a set of boxes.
    'integrateFunc' main integral function. Integrates full shape, or a wedge of a full shape
"""

def _intBoxes(boxes, f, boxSize, n, lims):
    totalScatter = 0
    totalFMap = 0
    
    for box in boxes:
        scatter, fMap = _boxSample(f, box, boxSize, n, lims)
        totalScatter += scatter
        totalFMap += fMap
       
    return (totalFMap/n)*(boxSize**len(lims))

def integrateFunc(f,lims,wedge,n,boxSize,start):
    dimensions = len(lims)
    if start == None:
        start = list(_np.zeros(len(lims)))

    r = 0
    integral, nextIntStep = 0, -1
    
    while nextIntStep != 0:        
        boxes = _allocate(wedge[1], r, dimensions, start)[wedge[0]-1]
        while boxes == []:
            r += 1
            boxes = _allocate(wedge[1], r, dimensions, start)[wedge[0]-1]

        nextIntStep = _intBoxes(boxes, f, boxSize, n, lims)
        integral += nextIntStep
        r += 1

    return integral

