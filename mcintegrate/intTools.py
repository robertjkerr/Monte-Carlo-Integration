# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:51:40 2021

@author: Robert Kerr
"""

import multiprocessing as mp
import mcintegrate.allocateTools as __tools
from numpy import zeros as __zeros
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



"""    
    `__intBoxes` integrates a set of boxes.
    `__intStep` integrates a layer of boxes at radius r
    'integrate' main function. Integrates full shape
"""


def __intBoxes(boxes, f, boxSize, n, lims):
    totalScatter = 0
    totalFMap = 0
    
    for box in boxes:
        scatter, fMap = boxSample(f, box, boxSize, n, lims)
        totalScatter += scatter
        totalFMap += fMap
       
    return (totalFMap/n)*(boxSize**len(lims))



def __intStep(cores, r, start, f, boxSize, n, lims):
    dimensions = len(lims)
    boxes = __tools.allocate(cores, r, dimensions, start)

    def intBox(box):
        return __intBoxes(box, f, boxSize, n, lims)
    
    
    
    p = mp.Pool()
    results = p.map(intBox, boxes)
    print(results)
    integral = sum(results)
    
    
    
    
    return integral



def integrate(f,lims, n=10, start=None, boxSize=1):
    cores = mp.cpu_count()
    if start == None:
        start = list(__zeros(len(lims)))

    intStep = lambda r: __intStep(cores,r,start,f,boxSize,n,lims)
    r = 0
    integral = 0
    nextIntStep = intStep(0)

    while nextIntStep != 0:
        r += 1
        nextIntStep = intStep(r)
        integral += nextIntStep

    return integral


def f(*q):
    return 1

if __name__=='__main__':
    lims = [[-1,1],[lambda *q:-(1-q[0]**2)**0.5,lambda *q:(1-q[0]**2)**0.5]]

    print(integrate(f,lims,1000,[0,0],0.1))

