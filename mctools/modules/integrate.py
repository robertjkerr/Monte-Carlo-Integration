# -*- coding: utf-8 -*-
"""
@author: Robert Kerr

Monte Carlo Integration function 
"""

import numpy as _np
from itertools import product as _product
from functools import lru_cache

"""
Allocation subroutines. Assists with parallelisation.

    `_getCombinations` gets all vectors within limits defined by extrema.
    `_getBoxes` gets all combinations of vectors within extrema that have the same one-norm.
    `allocate` gets all vectors returned by _getBoxes and divides them into sublists for each core.
"""

@lru_cache
def _getCombinations(extrema):
    QList = [tuple(range(d[0],d[1]+1)) for d in extrema]
    return set(_product(*QList))

def _getBoxes(r0, dimensions,start):
    extrema = lambda r: tuple([(-r+start[d],r+start[d]) for d in range(dimensions)])
    if r0 > 0:
        combinations = _getCombinations(extrema(r0))
        combinationsInner = _getCombinations(extrema(r0-1))
        return tuple(combinations-combinationsInner)
    else:
        return tuple(_getCombinations(extrema(0)))

def _allocate(cores, r, dimensions, start):
    boxes = _getBoxes(r, dimensions, start)
    boxList = [[] for i in range(cores)]
    for b in range(len(boxes)):
        box = boxes[b]
        pool = b%cores
        boxList[pool].append(box)
    return tuple(boxList)


"""
Throw tools. Used for Monte Carlo random throwing.

    `_testType` checks if input is a number or (by assumption) a function.
    `_throwCheck` checks if throw is within limits.
    `_throw` throws point randomly onto space of size boxSize^d.
    `_scatter` throws n throws into the same space.
    `_filterScatter` returns all throws in a scatter that are within the limits.
    `_filterBoxes` takes a selection of boxes, scatters over them and filters the throws.
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
     initThrow = _np.random.rand(dimensions)
     adjustedThrow = boxSize*(initThrow + _np.array(corner))
     return adjustedThrow

def _scatter(corner, boxSize, dimensions, n):
    scatter = tuple([_throw(corner,boxSize,dimensions) for i in range(n)])
    return _np.array(scatter)

def _filterScatter(scatter, lims):
    check = lambda throw: _throwCheck(throw, lims)
    filteredScatter = filter(check, tuple(scatter)) 
    return filteredScatter 

def _filterBoxes(boxes, boxSize, n, lims):
    makeScatter = lambda box: _scatter(box, boxSize, len(lims), n)
    filt = lambda box: _filterScatter(makeScatter(box), lims)
    numThrows = n*len(boxes)
    filteredThrows = map(filt, boxes)

    parsedThrows = []
    for part in filteredThrows:
        for throw in part:
            parsedThrows.append(throw)

    return tuple(parsedThrows), numThrows


"""
Integration subroutines. Main functions for integrating.

    `_converge` is main algorithm. Expands from start and throws scatters and filters them until the limits have been engulfed.
    `integrateFunc` maps all the filtered throws and finds the integral.
"""

def _converge(lims, wedge, n, boxSize, start, r, totalThrows, totalBoxes):
    dimensions = len(lims)
    diff = (_np.array(start)/boxSize).astype(int)
    boxes = _allocate(wedge[1], r, dimensions, diff)[wedge[0]-1]
    while boxes == []:
        r += 1
        boxes = _allocate(wedge[1], r, dimensions, start)[wedge[0]-1]

    numBoxes = len(boxes)
    filteredThrows, numThrows = _filterBoxes(boxes, boxSize, n, lims)
    if filteredThrows != ():
        return filteredThrows + _converge(lims, wedge, n, boxSize, start, r+1, totalThrows+numThrows, totalBoxes+numBoxes)
    else:
        return filteredThrows, totalThrows+numThrows, totalBoxes+numBoxes
 
def integrateFunc(f, lims, wedge, n, boxSize, start):
    if start == None:
        start = _np.zeros(len(lims))
    g = lambda throw: f(*throw)
    try:
        getThrows = _converge(lims,wedge,n,boxSize,start,0,0,0)
        l = len(getThrows)
        throws = tuple([throw for throw in getThrows[:(l-3)]])
        totalThrows, totalBoxes = getThrows[l-2], getThrows[l-1]
        fMap = map(g, throws)
        return (totalBoxes*boxSize**len(lims))*sum(fMap)/totalThrows
    except RecursionError as re:
        print('Suspected recursion depth exceeded. Try increasing "boxSize"')
