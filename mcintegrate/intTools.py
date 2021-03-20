# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 23:51:40 2021

@author: Robert Kerr
"""

import multiprocessing as __mp
import throwTools as __tools
from numpy import zeros as __zeros



"""
    `__allocate` gets all vectors returned by __tools.getBoxes and divides them into sublists for each core
    `__intBoxes` integrates a set of boxes.
"""


def __allocate(cores, r, dimensions, start):
    boxes = __tools.getBoxes(r, dimensions, start)
    boxList = [[] for i in range(cores)]
    
    for b in range(len(boxes)):
        box = boxes[b]
        pool = b%cores
        boxList[pool].append(box)
        
    return boxList

def __intBoxes(boxes, f, boxSize, n, lims):
    totalScatter = 0
    totalFMap = 0
    
    for box in boxes:
        scatter, fMap = __tools.boxSample(f, box, boxSize, n, lims)
        
        totalScatter += scatter
        totalFMap += fMap
       
    return (totalFMap/n)*(boxSize**len(lims))


#pool = __mp.pool(processes=__cores)



def __intStep(cores, r, start, f, boxSize, n, lims):
    dimensions = len(lims)
    boxes = __allocate(cores, r, dimensions, start)

    integral = 0
    for core in boxes:
        """
        Code to be parallelised
        """
        integral += __intBoxes(core, f, boxSize, n, lims)

    return integral


def integrate(f,lims, n=10, start=None, boxSize=1):
    dimensions = len(lims)
    cores = __mp.cpu_count()
    if start == None:
        start = list(__zeros(dimensions))

    r = 0
    integral = 0
    intStep = lambda r: __intStep(cores,r,start,f,boxSize,n,lims)
    nextIntStep = intStep(0)

    while nextIntStep != 0:
        r += 1
        nextIntStep = intStep(r)
        integral += nextIntStep

    return integral

"""
f = lambda *q:1
lims = [[-1,1],[lambda *q:-(1-q[0]**2)**0.5,lambda *q:(1-q[0]**2)**0.5]]

print(integrate(f,lims,1000,[0,0],0.1))
"""
